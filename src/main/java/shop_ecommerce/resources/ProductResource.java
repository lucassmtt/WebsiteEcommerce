package shop_ecommerce.resources;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import shop_ecommerce.services.ProductService;

@RestController
@RequestMapping("/product")
public class ProductResource {

    @Autowired ProductService productService;

    @GetMapping
    public ResponseEntity<>
}
