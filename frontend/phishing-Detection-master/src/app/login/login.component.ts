import { Component } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {Router} from "@angular/router";
import { AuthService } from '../services/auth-service.service';
import {ApplicationStateService} from "../services/application-state.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
    loginForm!:FormGroup;

  constructor(private fb:FormBuilder ,private router:Router ,private authService:AuthService,private appState:ApplicationStateService) {}
  ngOnInit(): void {
    this.loginForm=this.fb.group({
      username:this.fb.control(''),
      password:this.fb.control('')
    })
  }

    login() {
      this.authService.login(this.loginForm.value.username, this.loginForm.value.password).subscribe(
        (data:any)=>{
          console.log(localStorage.getItem("accessToken" ));
          this.appState.setAuthState({isAuthenticated:true,user:data.user,token:data.token,roles:data.roles});
          this.router.navigateByUrl('/template/dashboard');
        },
        (error:any)=>{
          console.log(error);
        }
      )
      this.router.navigateByUrl('/template/dashboard');
    }
}
