package shop_ecommerce.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import shop_ecommerce.models.User;

public interface UserRepository extends JpaRepository<User, Long> {
}
