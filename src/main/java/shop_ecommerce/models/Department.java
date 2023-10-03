package shop_ecommerce.models;


import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;

@Entity
@Getter
@Setter
@Table(name = "tb_deparment")
public class Department {

    @Id
    private Long oid;

    private String name;

    private String description;

    public Department(){}

    public Department(Long oid, String name, String description) {
        this.oid = oid;
        this.name = name;
        this.description = description;
    }

    @Override
    public String toString() {
        return "Department{" +
                "oid=" + oid +
                ", name='" + name + '\'' +
                ", description='" + description + '\'' +
                '}';
    }
}
