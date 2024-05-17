import { Injectable } from '@angular/core';
import {ApplicationStateService} from "./application-state.service";
import {HttpClient} from "@angular/common/http";
import {Router} from "@angular/router";
import {Mail} from "../models/mail.model";

@Injectable({
  providedIn: 'root'
})
export class MailService {

  constructor(
    protected appState: ApplicationStateService,
    public http: HttpClient,
    public router: Router
  ){}

  loadMails(page: number = 1, size: number = 5) {
    return this.http.get('http://localhost:8080/fetch-emails')
  }

  delete(id: number) {
    return this.http.delete(`http://localhost:3000/mails/${id}`);

  }
}
