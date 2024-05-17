package enset.ma.backend.repositories;

import enset.ma.backend.entities.Email;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface EmailRepository extends JpaRepository<Email,Long> {
    @Query("SELECT COALESCE(MAX(e.date), 0) FROM Email e")
    Long findMaxTimestamp();


@Query("SELECT e FROM Email e WHERE e.date > :timestamp")
    List<Email> findByDateGreaterThan(long timestamp);
}
