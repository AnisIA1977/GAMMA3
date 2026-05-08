package tn.defense.gamma3.config;

import lombok.RequiredArgsConstructor;
import org.springframework.boot.CommandLineRunner;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;
import tn.defense.gamma3.auth.domain.Role;
import tn.defense.gamma3.auth.domain.User;
import tn.defense.gamma3.auth.repository.UserRepository;
import tn.defense.gamma3.catalogue.domain.Item;
import tn.defense.gamma3.catalogue.repository.ItemRepository;
import tn.defense.gamma3.stock.domain.Magasin;
import tn.defense.gamma3.stock.repository.MagasinRepository;

import java.math.BigDecimal;
import java.time.LocalDateTime;

@Component
@RequiredArgsConstructor
public class DataSeeder implements CommandLineRunner {

    private final UserRepository userRepository;
    private final MagasinRepository magasinRepository;
    private final ItemRepository itemRepository;
    private final PasswordEncoder passwordEncoder;

    @Override
    public void run(String... args) throws Exception {
        if (userRepository.count() == 0) {
            User admin = User.builder()
                    .matricule("admin")
                    .fullName("Administrateur Système")
                    .password(passwordEncoder.encode("admin"))
                    .role(Role.ADMIN)
                    .build();
            userRepository.save(admin);
            System.out.println("✅ Administrateur par défaut créé : admin/admin");
        }

        if (magasinRepository.count() == 0) {
            magasinRepository.save(Magasin.builder().code("SGS").nom("Service de Gestion des Stocks").localisation("Bâtiment Central").build());
            magasinRepository.save(Magasin.builder().code("SM1").nom("Soute à Munitions 1").localisation("Zone Nord").build());
            magasinRepository.save(Magasin.builder().code("SM2").nom("Soute à Munitions 2").localisation("Zone Sud").build());
            magasinRepository.save(Magasin.builder().code("M_MEC").nom("Magasin Mécanique").localisation("Atelier B").build());
            System.out.println("✅ Magasins par défaut créés.");
        }

        if (itemRepository.count() == 0) {
            itemRepository.save(Item.builder()
                    .classeCode("13")
                    .sousClasseCode("05")
                    .categorieCode("14")
                    .serieCode("12")
                    .itemCode("3456")
                    .designation("MUNITION 5.56 MM OTAN")
                    .prixUnitaire(new BigDecimal("1.250"))
                    .stockSecurite(new BigDecimal("5000"))
                    .dangerClass(tn.defense.gamma3.catalogue.domain.DangerClass.EXPLOSIVE)
                    .build());

            itemRepository.save(Item.builder()
                    .classeCode("28")
                    .sousClasseCode("05")
                    .categorieCode("14")
                    .serieCode("98")
                    .itemCode("7654")
                    .designation("FILTRE A HUILE MOTEUR MTU")
                    .prixUnitaire(new BigDecimal("145.500"))
                    .stockSecurite(new BigDecimal("50"))
                    .dangerClass(tn.defense.gamma3.catalogue.domain.DangerClass.NONE)
                    .build());

            itemRepository.save(Item.builder()
                    .classeCode("91")
                    .sousClasseCode("11")
                    .categorieCode("23")
                    .serieCode("44")
                    .itemCode("0001")
                    .designation("CABLE ELECTRIQUE HTA 630MM2")
                    .prixUnitaire(new BigDecimal("89.900"))
                    .stockSecurite(new BigDecimal("200"))
                    .dangerClass(tn.defense.gamma3.catalogue.domain.DangerClass.NONE)
                    .build());
            System.out.println("✅ Articles de test créés dans le catalogue.");
        }
    }
}
