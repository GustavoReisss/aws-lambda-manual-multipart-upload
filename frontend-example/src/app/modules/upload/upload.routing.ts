import { Routes, RouterModule } from '@angular/router';
import { DefaultLayoutComponent } from '../../layouts/default-layout/default-layout.component';
import { UploadComponent } from './upload.component';

const routes: Routes = [
  {
    path: '',
    component: DefaultLayoutComponent,
    children: [
      {
        path: '',
        component: UploadComponent
      }
    ]
  }
];

export const UploadRoutes = RouterModule.forChild(routes);
