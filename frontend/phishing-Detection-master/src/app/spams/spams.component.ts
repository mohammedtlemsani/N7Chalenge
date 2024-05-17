import { Component } from '@angular/core';
import {Mail} from "../models/mail.model";
import {ApplicationStateService} from "../services/application-state.service";
import {HttpClient} from "@angular/common/http";
import {Router} from "@angular/router";

@Component({
  selector: 'app-spams',
  templateUrl: './spams.component.html',
  styleUrl: './spams.component.css'
})
export class SpamsComponent {
  spams: Array<Mail> = [
    {
      id: 1,
      _from: 'John Doe',
      object: 'John Doe',
      to: 'John Doe',
      subject: 'Hello, World!',
      content: 'Hello, World!',
      date: new Date(),
      checked: false
    },
    {
      id: 2,
      _from: 'Jane Doe',
      object: 'John Doe',
      to: 'John Doe',
      subject: 'Hello, World!',
      content: 'Hello, World!',
      date: new Date(),
      checked: false
    }
  ]
  constructor(
    protected appState: ApplicationStateService,
    public http: HttpClient,
    public router: Router
  ) {
  }
  deleteMail(mail: Mail) {
    if (confirm('Are you sure you want to delete this MAIL?')) {
      this.http.delete(`http://localhost:3000/mails/${mail.id}`)
        .subscribe({
          next: () => {
            this.spams = this.spams.filter((m) => m.id !== mail.id);
            this.appState.mailState.totalCount = this.spams.length;
          },
          error: (err) => {
            console.log(err);
          }
        });
    }
  }


  mailDetails(s: string, id: number) {
    this.router.navigate([`/template/mail`, id]);
  }

  goToPage(number: number) {

  }
}
