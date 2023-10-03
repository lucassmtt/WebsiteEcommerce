package shop_ecommerce.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import shop_ecommerce.models.Product;

public interface ProductRepository extends JpaRepository<Product, Long> {
}
