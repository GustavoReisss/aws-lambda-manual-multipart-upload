import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: 'upload',
        loadChildren: () => import('./modules/upload/upload.module').then(m => m.UploadModule)
    },
    {
        path: '',
        redirectTo: 'upload',
        pathMatch: 'full'
    }
];
