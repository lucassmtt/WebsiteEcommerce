package shop_ecommerce.models;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;

@Entity
@Setter
@Getter
@Table(name = "tb_user")
public class User {

    @Id
    private Long oid;

    private String name;

    private String email;

    private String phone;

    private String password;

    public User(){}

    public User(Long oid, String name, String email, String phone, String password) {
        this.oid = oid;
        this.name = name;
        this.email = email;
        this.phone = phone;
        this.password = password;
    }

    @Override
    public String toString() {
        return "User{" +
                "oid=" + oid +
                ", name='" + name + '\'' +
                ", email='" + email + '\'' +
                ", phone='" + phone + '\'' +
                ", password='" + password + '\'' +
                '}';
    }
}
