import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DefaultLayoutComponent } from './default-layout.component';
import { RouterModule } from '@angular/router';

@NgModule({
  imports: [
    CommonModule,
    RouterModule
  ],
  declarations: [DefaultLayoutComponent],
  exports: [
    DefaultLayoutComponent
  ]
})
export class DefaultLayoutModule { }
