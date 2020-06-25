import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router'; // CLI imports router

import { GridListDynamicComponent }       from './grid-list-dynamic/grid-list-dynamic.component';



 

const routes: Routes = [
    { path: '',                  component: GridListDynamicComponent }
  ];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }