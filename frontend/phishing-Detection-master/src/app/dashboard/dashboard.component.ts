import {Component, OnInit} from '@angular/core';
import {ApplicationStateService} from "../services/application-state.service";
import {AuthService} from "../services/auth-service.service";

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent implements OnInit{

  constructor(public state:ApplicationStateService,public authState:AuthService) {
  }
  totalEmailsProcessed: number = 10000;
  spamEmailsDetected: number = 2500;

  public calculateSpamDetectionRate(): number {
    if (this.totalEmailsProcessed === 0) return 0; // Avoid division by zero
    return (this.spamEmailsDetected / this.totalEmailsProcessed) * 100;
  }
  ngOnInit(): void {
  }

}
