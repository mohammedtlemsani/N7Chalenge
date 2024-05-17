import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ApplicationStateService {
  spamState: any = {
    totalCount: 5,
    spamNumber: 0,
    currentPage: 1,
    size: 5,
    pages: 1,
    spams: []
  };
  constructor() { }

  public user: any = {
    username: '',
    isLoggedIn: false,
    isAdmin: false,
  };

  public authState: any = {
    isAuthenticated: false,
    user: this.user,
    token: undefined,
    roles: undefined
  };

  public mailState: any = {
    totalCount: 5,
    spamNumber: 0,
    currentPage: 1,
    size: 5,
    pages: 1,
    mails: []
  };

  public setAuthState(state: any) {
    this.authState = { ...this.authState, ...state };
  }

}
