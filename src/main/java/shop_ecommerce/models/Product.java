package shop_ecommerce.models;


import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;

import java.io.Serial;
import java.io.Serializable;

@Getter
@Setter
@Entity
@Table(name = "tb_product")
public class Product implements Serializable {

    @Serial
    private static final long serialVersionUID = 1L;

    @Id
    private long oid;
    private String name;
    private String price;
    private String description;
    private String department;

    public Product(){}

    public Product(long oid, String name, String price, String description, String department) {
        this.oid = oid;
        this.name = name;
        this.price = price;
        this.description = description;
        this.department = department;
    }

    @Override
    public String toString() {
        return "Product{" +
                "oid=" + oid +
                ", name='" + name + '\'' +
                ", price='" + price + '\'' +
                ", description='" + description + '\'' +
                ", department='" + department + '\'' +
                '}';
    }
}
