package shop_ecommerce.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import shop_ecommerce.models.Department;

public interface DepartmentRepository extends JpaRepository<Department, Long> {
}
