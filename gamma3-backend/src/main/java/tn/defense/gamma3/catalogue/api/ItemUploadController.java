package tn.defense.gamma3.catalogue.api;

import org.springframework.http.ResponseEntity;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import tn.defense.gamma3.catalogue.domain.DangerClass;
import tn.defense.gamma3.catalogue.domain.Item;
import tn.defense.gamma3.catalogue.domain.ItemDocument;
import tn.defense.gamma3.catalogue.repository.ItemRepository;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.UUID;

@RestController
@RequestMapping("/api/v1/items")
@CrossOrigin(origins = "http://localhost:4200")
public class ItemUploadController {

    private final ItemRepository itemRepository;
    private final String UPLOAD_DIR = "uploads/";

    public ItemUploadController(ItemRepository itemRepository) {
        this.itemRepository = itemRepository;
    }

    @PostMapping("/{id}/upload-photo")
    public ResponseEntity<Item> uploadPhoto(@PathVariable UUID id, @RequestParam("file") MultipartFile file) {
        return handleFileUpload(id, file, "photos", "photoUrl");
    }

    @PostMapping("/{id}/upload-doc")
    public ResponseEntity<Item> uploadDocument(@PathVariable UUID id, @RequestParam("file") MultipartFile file) {
        return handleFileUpload(id, file, "documents", "technicalDocUrl");
    }

    @PutMapping("/{id}/danger-class")
    public ResponseEntity<Item> updateDangerClass(@PathVariable UUID id, @RequestBody DangerClassRequest request) {
        return itemRepository.findById(id).map(item -> {
            item.setDangerClass(request.getDangerClass());
            Item updatedItem = itemRepository.save(item);
            return ResponseEntity.ok(updatedItem);
        }).orElse(ResponseEntity.notFound().build());
    }

    private ResponseEntity<Item> handleFileUpload(UUID id, MultipartFile file, String subDir, String fieldType) {
        return itemRepository.findById(id).map(item -> {
            try {
                String originalFilename = file.getOriginalFilename();
                if (originalFilename == null) {
                    return ResponseEntity.badRequest().<Item>build();
                }

                String fileName = StringUtils.cleanPath(originalFilename);
                if (fileName.contains("..")) {
                    return ResponseEntity.badRequest().<Item>build();
                }

                String uniqueFileName = UUID.randomUUID().toString() + "_" + fileName;
                Path uploadPath = Paths.get(UPLOAD_DIR + subDir).toAbsolutePath().normalize();
                
                if (!Files.exists(uploadPath)) {
                    Files.createDirectories(uploadPath);
                }

                Path filePath = uploadPath.resolve(uniqueFileName).normalize();
                if (!filePath.startsWith(uploadPath)) {
                    return ResponseEntity.badRequest().<Item>build();
                }

                Files.copy(file.getInputStream(), filePath, StandardCopyOption.REPLACE_EXISTING);

                String fileUrl = "http://localhost:8080/uploads/" + subDir + "/" + uniqueFileName;
                
                if (fieldType.equals("photoUrl")) {
                    item.setPhotoUrl(fileUrl);
                } else if (fieldType.equals("technicalDocUrl")) {
                    ItemDocument doc = new ItemDocument();
                    doc.setFileName(fileName);
                    doc.setFileUrl(fileUrl);
                    doc.setItem(item);
                    item.getDocuments().add(doc);
                }
                
                Item updatedItem = itemRepository.save(item);
                return ResponseEntity.ok(updatedItem);

            } catch (IOException ex) {
                return ResponseEntity.internalServerError().<Item>build();
            }
        }).orElse(ResponseEntity.notFound().build());
    }

    public static class DangerClassRequest {
        private DangerClass dangerClass;
        public DangerClass getDangerClass() { return dangerClass; }
        public void setDangerClass(DangerClass dangerClass) { this.dangerClass = dangerClass; }
    }
}
