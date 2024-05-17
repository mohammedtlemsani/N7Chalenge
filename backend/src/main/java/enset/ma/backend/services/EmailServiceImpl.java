package enset.ma.backend.services;

import enset.ma.backend.entities.Email;
import enset.ma.backend.repositories.EmailRepository;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.*;
import org.springframework.http.converter.HttpMessageConverter;
import org.springframework.http.converter.StringHttpMessageConverter;
import org.springframework.http.converter.json.MappingJackson2HttpMessageConverter;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;


import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

@Service
@AllArgsConstructor
public class EmailServiceImpl {
    private RestTemplate restTemplate;
    @Autowired
    private EmailRepository emailRepository;

    /*public List<Email> fetchEmails(long timestamp) {
        String flaskUrl = "http://172.17.1.86:105/api/emails?timestamp=" + timestamp;
        HttpHeaders headers = new HttpHeaders();
        headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
        headers.add("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36");

        HttpEntity<String> entity = new HttpEntity<>("parameters", headers);
        List<HttpMessageConverter<Email>> messageConverters = new ArrayList<HttpMessageConverter<E>>();
        //Add the Jackson Message converter
        MappingJackson2HttpMessageConverter converter = new MappingJackson2HttpMessageConverter();

        // Note: here we are making this converter to process any kind of response,
        // not only application/*json, which is the default behaviour
        converter.setSupportedMediaTypes(Collections.singletonList(MediaType.ALL));
        messageConverters.add(converter);
        restTemplate.setMessageConverters(messageConverters);
        ResponseEntity<List> result =
                restTemplate.exchange(flaskUrl, HttpMethod.GET, entity, List.class);
        return result.getBody();
    }

     */
    public EmailServiceImpl() {
        this.restTemplate = new RestTemplate();
        List<HttpMessageConverter<?>> messageConverters = new ArrayList<>();
        MappingJackson2HttpMessageConverter converter = new MappingJackson2HttpMessageConverter();
        converter.setSupportedMediaTypes(Collections.singletonList(MediaType.APPLICATION_JSON));
        messageConverters.add(converter);
        restTemplate.setMessageConverters(messageConverters);
    }

    public List<Email> fetchEmails(long timestamp) {
        String flaskUrl = "http://172.17.1.86:105/api/emails?timestamp=" + timestamp;
        HttpHeaders headers = new HttpHeaders();
        headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
        headers.add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36");

        HttpEntity<String> entity = new HttpEntity<>("parameters", headers);

        ResponseEntity<List<Email>> response = restTemplate.exchange(
                flaskUrl,
                HttpMethod.GET,
                entity,
                new ParameterizedTypeReference<List<Email>>() {}
        );

        return response.getBody();
    }

    /*public List<Email> fetchEmails(long timestamp) {
        String flaskUrl = "http://172.17.1.86:105/api/emails?timestamp=" + timestamp;
        HttpHeaders headers = new HttpHeaders();
        headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
        headers.add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36");

        HttpEntity<String> entity = new HttpEntity<>("parameters", headers);

        ResponseEntity<List<Email>> response = restTemplate.exchange(
                flaskUrl,
                HttpMethod.GET,
                entity,
                new ParameterizedTypeReference<List<Email>>() {}
        );

        return response.getBody();
    }

     */
    public List<Email> getEmails(long timestamp) {
        Long max=emailRepository.findMaxTimestamp();
        List<Email> emails=emailRepository.findByDateGreaterThan(timestamp);
        if (emails.isEmpty()) {
            return new ArrayList<>();
        }else {
            return emails;
        }
    }

    public boolean getScanUrl(String url) {
        String flaskUrl = "http://172.17.1.86:105/api/scan?url=" + url;
        return Boolean.TRUE.equals(restTemplate.getForObject(flaskUrl, Boolean.class));
    }

    public long getNewest() {
        return emailRepository.findMaxTimestamp();
    }
}
