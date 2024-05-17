import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor
} from '@angular/common/http';
import {catchError, finalize, Observable} from 'rxjs';
import {AuthService} from "../services/auth-service.service";

@Injectable()
export class AppHttpInterceptor implements HttpInterceptor {

  constructor(private authService : AuthService) {}

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    if(!request.url.includes('auth/login')) {
      let req = request.clone({

        headers: request.headers.set('Authorization', 'Bearer ' + localStorage.getItem("accessToken"))
      })
      return next.handle(req);
    }
    else {
      return next.handle(request);
    }

  }
}
