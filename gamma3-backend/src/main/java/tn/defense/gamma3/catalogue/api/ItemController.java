package tn.defense.gamma3.catalogue.api;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import tn.defense.gamma3.catalogue.domain.Item;
import tn.defense.gamma3.catalogue.repository.ItemRepository;

import java.util.List;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/api/v1/items")
@CrossOrigin(origins = "http://localhost:4200")
public class ItemController {

    private final ItemRepository itemRepository;

    public ItemController(ItemRepository itemRepository) {
        this.itemRepository = itemRepository;
    }

    /**
     * Liste paginée des articles (DTO léger, sans documents).
     * Résout le problème N+1 qui chargeait la DB entière et ralentissait le serveur.
     */
    @GetMapping
    public ResponseEntity<Map<String, Object>> getAllItems(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "25") int size,
            @RequestParam(defaultValue = "classeCode") String sortBy,
            @RequestParam(required = false) String search
    ) {
        // Limiter la taille max à 100 pour protéger le serveur
        size = Math.min(size, 100);
        Pageable pageable = PageRequest.of(page, size, Sort.by(sortBy));

        Page<Item> pageResult;
        if (search != null && !search.isBlank()) {
            pageResult = itemRepository.findByDesignationContainingIgnoreCase(search, pageable);
        } else {
            pageResult = itemRepository.findAll(pageable);
        }

        // Mapper vers DTO léger (pas de documents)
        List<ItemSummaryDto> dtos = pageResult.getContent().stream()
                .map(item -> new ItemSummaryDto(
                        item.getId(),
                        item.getClasseCode(),
                        item.getSousClasseCode(),
                        item.getCategorieCode(),
                        item.getSerieCode(),
                        item.getItemCode(),
                        item.getNomenclature(),
                        item.getDesignation(),
                        item.getPrixUnitaire(),
                        item.getStockSecurite(),
                        item.getUniteGestionCode(),
                        item.getPhotoUrl(),
                        item.getDangerClass() != null ? item.getDangerClass().name() : null
                ))
                .toList();

        return ResponseEntity.ok(Map.of(
                "content", dtos,
                "totalElements", pageResult.getTotalElements(),
                "totalPages", pageResult.getTotalPages(),
                "currentPage", pageResult.getNumber(),
                "pageSize", pageResult.getSize()
        ));
    }

    @GetMapping("/{id}")
    public ResponseEntity<Item> getItemById(@PathVariable UUID id) {
        return itemRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<Item> createItem(@RequestBody Item item) {
        Item savedItem = itemRepository.save(item);
        return ResponseEntity.ok(savedItem);
    }
}
