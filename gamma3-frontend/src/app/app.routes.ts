import { Routes } from '@angular/router';
import { authGuard } from './core/guards/auth.guard';

export const routes: Routes = [
  { path: '', redirectTo: '/catalogue', pathMatch: 'full' },
  {
    path: 'login',
    loadComponent: () => import('./features/auth/login/login.component').then(m => m.LoginComponent)
  },
  { 
    path: 'catalogue', 
    loadComponent: () => import('./features/catalogue/catalogue.component').then(m => m.CatalogueComponent),
    canActivate: [authGuard]
  },
  { 
    path: 'catalogue/:id', 
    loadComponent: () => import('./features/catalogue/item-detail/item-detail.component').then(m => m.ItemDetailComponent),
    canActivate: [authGuard]
  }
];
