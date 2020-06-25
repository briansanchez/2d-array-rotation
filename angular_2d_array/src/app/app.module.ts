import { BrowserModule }                            from '@angular/platform-browser';
import { NgModule }                                 from '@angular/core';
import { AppComponent }                             from './app.component';
import { BrowserAnimationsModule }                  from '@angular/platform-browser/animations';
import { GridListDynamicComponent }                 from './grid-list-dynamic/grid-list-dynamic.component';
import {MatSnackBarModule}                          from '@angular/material/snack-bar';
import {MatGridListModule}                          from '@angular/material/grid-list';
import { AppRoutingModule }                         from './app-routing.module'; // CLI imports AppRoutingModule

import { GridBackendService }                       from './services/grid-backend.service';
import { HttpClientModule, HTTP_INTERCEPTORS }      from '@angular/common/http';
import  {MatButtonModule }                            from '@angular/material/button';




@NgModule({
  declarations: [
    AppComponent,
    GridListDynamicComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatGridListModule,
    MatButtonModule,
    MatSnackBarModule,
    AppRoutingModule // CLI adds AppRoutingModule to the AppModule's imports array
    

  ],
  providers: [  GridBackendService ],
  bootstrap: [AppComponent ]
})
export class AppModule { }
