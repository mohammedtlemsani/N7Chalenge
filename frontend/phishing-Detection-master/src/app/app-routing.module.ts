import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {DashboardComponent} from "./dashboard/dashboard.component";
import {BarChartComponent} from "./bar-chart/bar-chart.component";
import {LineChartComponent} from "./line-chart/line-chart.component";
import {LoginComponent} from "./login/login.component";
import {UsageComponent} from "./usage/usage.component";
import {TemplateComponent} from "./template/template.component";
import {MailsComponent} from "./mails/mails.component";
import {MailComponent} from "./mail/mail.component";
import {SpamsComponent} from "./spams/spams.component";
import {SpamComponent} from "./spam/spam.component";

const routes: Routes = [
  {path:'', redirectTo: '/usage', pathMatch: 'full'},
  { path: 'usage', component : UsageComponent},
  { path: 'login', component : LoginComponent},
  { path: 'template',component: TemplateComponent ,children:[
      { path: 'line-chart', component : LineChartComponent},
      { path: 'dashboard', component : DashboardComponent},
      { path: 'inbox', component : MailsComponent},
      { path: 'spams', component : SpamsComponent},
      { path: 'login', component : LoginComponent},
      { path: 'mail/:id', component : MailComponent},
      { path: 'spam/:id', component : SpamComponent},
  ]},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
