package shop_ecommerce.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import shop_ecommerce.models.Department;
import shop_ecommerce.repositories.DepartmentRepository;

import java.util.List;
import java.util.Optional;

@Service
public class DepartmentService {
    @Autowired
    private DepartmentRepository departmentRepository;

    public List<Department> findAll(){
        return departmentRepository.findAll();
    }

    public Optional<Department> findByOid(Long oid){
        return departmentRepository.findById(oid);
    }

    public void addDepartment(Department department){
        departmentRepository.save(department);
    }

    public void deleteByOid(Long oid){
        departmentRepository.deleteById(oid);
    }
}
