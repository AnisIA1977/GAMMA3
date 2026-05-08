import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { TableModule } from 'primeng/table';
import { InputTextModule } from 'primeng/inputtext';
import { ButtonModule } from 'primeng/button';
import { ItemService } from './item.service';

@Component({
  selector: 'app-catalogue',
  standalone: true,
  imports: [CommonModule, FormsModule, TableModule, InputTextModule, ButtonModule],
  templateUrl: './catalogue.component.html',
  styleUrls: ['./catalogue.component.css']
})
export class CatalogueComponent implements OnInit {
  
  itemService = inject(ItemService);
  items = this.itemService.items;

  private router = inject(Router);

  // Pagination
  currentPage = 0;
  pageSize = 25;
  searchTerm = '';
  private searchTimeout: any;

  ngOnInit(): void {
    this.itemService.fetchItems(0, this.pageSize);
  }

  onPageChange(event: any) {
    // PrimeNG p-table utilise event.first et event.rows
    this.currentPage = Math.floor(event.first / event.rows);
    this.pageSize = event.rows;
    this.itemService.fetchItems(this.currentPage, this.pageSize, this.searchTerm || undefined);
  }

  onSearch() {
    // Debounce pour ne pas appeler l'API à chaque frappe
    clearTimeout(this.searchTimeout);
    this.searchTimeout = setTimeout(() => {
      this.currentPage = 0;
      this.itemService.fetchItems(0, this.pageSize, this.searchTerm || undefined);
    }, 400);
  }

  onRowSelect(event: any) {
    if (event.data && event.data.id) {
      this.router.navigate(['/catalogue', event.data.id]);
    }
  }

}
