package shop_ecommerce.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import shop_ecommerce.models.User;
import shop_ecommerce.repositories.UserRepository;

import java.util.List;
import java.util.Optional;

@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    public List<User> findAll(){
        return userRepository.findAll();
    }

    public Optional<User> findByOid(Long oid){
        return userRepository.findById(oid);
    }

    public void addUser(User user){
        userRepository.save(user);
    }

    public void deleteByOid(Long oid){
        userRepository.deleteById(oid);
    }
}
