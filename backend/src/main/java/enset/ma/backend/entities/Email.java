package enset.ma.backend.entities;

import jakarta.annotation.Nullable;
import jakarta.persistence.*;
import jakarta.validation.constraints.Size;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.NonNull;

import java.sql.Timestamp;

@Entity
@AllArgsConstructor @NoArgsConstructor @Data
public class Email {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String _from;
    @Column(name = "email_to")
    private String to;
    private String subject;
    @Size(max = 1000000)
    private String content;

    private Long date;
    private boolean isSpam;


}
