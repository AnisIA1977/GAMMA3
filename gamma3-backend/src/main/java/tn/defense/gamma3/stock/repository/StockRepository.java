package tn.defense.gamma3.stock.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import tn.defense.gamma3.stock.domain.Stock;

import java.util.List;
import java.util.Optional;

public interface StockRepository extends JpaRepository<Stock, Long> {
    Optional<Stock> findByItem_IdAndMagasin_Id(java.util.UUID itemId, Long magasinId);
    List<Stock> findByItem_Id(java.util.UUID itemId);
}
