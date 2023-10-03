package shop_ecommerce.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import shop_ecommerce.models.Product;
import shop_ecommerce.repositories.ProductRepository;

import java.util.List;
import java.util.Optional;

@Service
public class ProductService {

    @Autowired
    private ProductRepository productRepository;

    public List<Product> findAll(){
        return productRepository.findAll();
    }

    public Optional<Product> findByOid(Long oid){
        return productRepository.findById(oid);
    }

    public void addProduct(Product product){
        productRepository.save(product);
    }

    public void deleteByOid(Long oid){
        productRepository.deleteById(oid);
    }
}
