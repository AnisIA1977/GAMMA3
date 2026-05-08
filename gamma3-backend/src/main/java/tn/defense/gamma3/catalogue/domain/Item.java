package tn.defense.gamma3.catalogue.domain;

import jakarta.persistence.*;
import lombok.*;
import org.hibernate.annotations.BatchSize;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

/**
 * Entity representing a physical Item in the inventory.
 * Maps to the legacy "Item" table from Gamma 2.
 */
@Entity
@Table(name = "items")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Item {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(name = "id", updatable = false, nullable = false)
    private UUID id;

    // Nomenclature éclatée (Legacy Gamma 2) - Décision D-008
    @Column(name = "classe_code", length = 2, nullable = false)
    private String classeCode;

    @Column(name = "sous_classe_code", length = 2, nullable = false)
    private String sousClasseCode;

    @Column(name = "categorie_code", length = 2, nullable = false)
    private String categorieCode;

    @Column(name = "serie_code", length = 2, nullable = false)
    private String serieCode;

    @Column(name = "item_code", length = 4, nullable = false)
    private String itemCode;

    /**
     * Helper pour regrouper la nomenclature à la volée.
     * @return La nomenclature intelligente au format "100MT010001"
     */
    public String getNomenclature() {
        return this.classeCode + this.sousClasseCode + this.categorieCode + this.serieCode + this.itemCode;
    }

    @Column(name = "designation", length = 254)
    private String designation;

    @Column(name = "prix_unitaire", precision = 18, scale = 3)
    private BigDecimal prixUnitaire;

    @Column(name = "stock_securite", precision = 10, scale = 2)
    private BigDecimal stockSecurite;

    @Column(name = "unite_gestion_code", length = 2)
    private String uniteGestionCode;

    @Column(name = "photo_url")
    private String photoUrl;

    @Column(name = "technical_doc_url")
    private String technicalDocUrl;

    @Enumerated(EnumType.STRING)
    @Column(name = "danger_class")
    private DangerClass dangerClass;

    @OneToMany(mappedBy = "item", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @BatchSize(size = 50)
    private List<ItemDocument> documents = new ArrayList<>();

    @CreationTimestamp
    @Column(name = "created_at", updatable = false)
    private LocalDateTime createdAt;

    @UpdateTimestamp
    @Column(name = "updated_at")
    private LocalDateTime updatedAt;

}
