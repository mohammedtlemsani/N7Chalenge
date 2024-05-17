import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { BarChartComponent } from './bar-chart/bar-chart.component';
import { LineChartComponent } from './line-chart/line-chart.component';
import { LoginComponent } from './login/login.component';
import {ReactiveFormsModule} from "@angular/forms";
import {HTTP_INTERCEPTORS, HttpClient, HttpClientModule} from "@angular/common/http";
import { SidebarComponent } from './sidebar/sidebar.component';
import { TemplateComponent } from './template/template.component';
import { UsageComponent } from './usage/usage.component';
import {AppHttpInterceptor} from "./interceptors/http.interceptor";
import { MailsComponent } from './mails/mails.component';
import { MailComponent } from './mail/mail.component';
import { SpamsComponent } from './spams/spams.component';
import { SpamComponent } from './spam/spam.component';

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    BarChartComponent,
    LineChartComponent,
    LoginComponent,
    SidebarComponent,
    TemplateComponent,
    UsageComponent,
    MailsComponent,
    MailComponent,
    SpamsComponent,
    SpamComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule,
  ],
  providers: [
    {provide :HTTP_INTERCEPTORS,useClass : AppHttpInterceptor,multi:true}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
