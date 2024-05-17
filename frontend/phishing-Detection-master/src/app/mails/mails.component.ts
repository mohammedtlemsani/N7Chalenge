import {Component, OnInit} from '@angular/core';
import { Mail } from '../models/mail.model';
import { ApplicationStateService } from '../services/application-state.service';
import { HttpClient } from '@angular/common/http';
import {Router} from "@angular/router";
import {MailService} from "../services/mail.service";

@Component({
  selector: 'app-mails',
  templateUrl: './mails.component.html',
  styleUrls: ['./mails.component.css']
})
export class MailsComponent implements OnInit {

  constructor(
    protected appState: ApplicationStateService,
    public router: Router,
    public mailService: MailService
  ) {
    this.loadMails();
  }

  ngOnInit(): void {
        this.loadMails();
    }

  mails!: any;

  loadMails() {
    this.mailService.loadMails()
      .subscribe({
        next: (response) => {
          this.mails = response;
          console.log(this.mails);
          this.appState.mailState.totalCount = this.mails.length;
        },
        error: (err) => {
          console.log(err);
        }
      });
  }

  handleCheck(mail: Mail) {
    mail.checked = !mail.checked;
  }

  deleteMail(mail: Mail) {
    if (confirm('Are you sure you want to delete this MAIL?')) {
      this.mailService.delete(mail.id)
        .subscribe({
          next: () => {

            this.appState.mailState.totalCount = this.mails.length;
          },
          error: (err) => {
            console.log(err);
          }
        });
    }
  }

  goToPage(page:number){
    let currentPage_appState=page;
    this.mailService.loadMails(this.appState.mailState.currentPage,this.appState.mailState.size)
      .subscribe({
        next: (response) => {
          this.mails = response;
          this.appState.mailState.totalCount = this.mails.length;
        },
        error: (err) => {
          console.log(err);
        }
    });
  }
  goToUrl(url:string) {
    // Implement pagination logic here
  }

  mailDetails(url: string, id: number) {
    this.router.navigate([`/template/mail`, id]);  }
}
