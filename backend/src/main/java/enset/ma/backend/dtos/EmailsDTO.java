package enset.ma.backend.dtos;

import enset.ma.backend.entities.Email;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.List;
@AllArgsConstructor@NoArgsConstructor@Data
public class EmailsDTO {
    private long timestamp;
    private int count;
    private List<Email> spamEmails=new ArrayList<>();
    private List<Email> hamEmails=new ArrayList<>();
}

