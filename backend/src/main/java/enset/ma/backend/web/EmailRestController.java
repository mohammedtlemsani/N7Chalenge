package enset.ma.backend.web;
import enset.ma.backend.dtos.EmailsDTO;
import enset.ma.backend.entities.Email;
import enset.ma.backend.repositories.EmailRepository;
import enset.ma.backend.services.EmailServiceImpl;
import lombok.AllArgsConstructor;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
@RestController
@AllArgsConstructor
public class EmailRestController {
    private EmailServiceImpl emailService;
    private EmailRepository emailRepository;

    @GetMapping(value = "/fetch-emails", produces = MediaType.APPLICATION_JSON_VALUE)
    public EmailsDTO fetchEmails() {
        long timestamp=emailService.getNewest();
        EmailsDTO emailsDTO = new EmailsDTO();
        emailsDTO.setTimestamp(timestamp);
        List<Email> emails = emailService.fetchEmails(timestamp);
        emailRepository.saveAll(emails);
        emails.forEach(email -> {
            if (email.isSpam()) {
                emailsDTO.getSpamEmails().add(email);
            } else {
                emailsDTO.getHamEmails().add(email);
            }
        });
        emailsDTO.setCount(emailsDTO.getSpamEmails().size() + emailsDTO.getHamEmails().size());
        return emailsDTO;
    }
    @GetMapping("/emails")
    public List<Email> getEmails(@RequestParam Long timestamp) {
        return emailService.getEmails(timestamp);
    }

}
