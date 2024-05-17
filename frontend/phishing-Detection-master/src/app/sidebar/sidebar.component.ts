import { Component } from '@angular/core';
import {ApplicationStateService} from "../services/application-state.service";
import {AuthService} from "../services/auth-service.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrl: './sidebar.component.css'
})
export class SidebarComponent {
  constructor(public state:ApplicationStateService,public authState:AuthService,public router:Router) {
  }
  ngOnInit(): void {
    this.state.setAuthState({user: {username:'Khaoula',mail:'khaoula@gmail.com'}});
  }

  logout() {
    this.router.navigateByUrl('/login');
  }
  goToUrl(url:string) {
    console.log("url:",url);
    this.router.navigateByUrl(`/template/${url}`);
  }

}
