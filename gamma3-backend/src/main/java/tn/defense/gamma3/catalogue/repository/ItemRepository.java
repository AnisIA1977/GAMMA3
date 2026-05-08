package tn.defense.gamma3.catalogue.repository;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import tn.defense.gamma3.catalogue.domain.Item;

import java.util.Optional;
import java.util.UUID;

@Repository
public interface ItemRepository extends JpaRepository<Item, UUID> {

    // Custom query to find an item by its split nomenclature
    Optional<Item> findByClasseCodeAndSousClasseCodeAndCategorieCodeAndSerieCodeAndItemCode(
            String classeCode, String sousClasseCode, String categorieCode, String serieCode, String itemCode
    );

    // Recherche par désignation avec pagination
    Page<Item> findByDesignationContainingIgnoreCase(String designation, Pageable pageable);

}

