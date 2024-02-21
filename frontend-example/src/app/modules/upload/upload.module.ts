import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UploadComponent } from './upload.component';
import { DefaultLayoutModule } from '../../layouts/default-layout/default-layout.module';
import { HttpClientModule } from '@angular/common/http';
import { UploadRoutes } from './upload.routing';




@NgModule({
  imports: [
    CommonModule,
    DefaultLayoutModule,
    HttpClientModule,
    UploadRoutes
  ],
  declarations: [UploadComponent]
})
export class UploadModule { }
