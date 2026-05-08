import { Injectable, signal } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Item {
  id: string;
  classeCode: string;
  sousClasseCode: string;
  categorieCode: string;
  serieCode: string;
  itemCode: string;
  nomenclature: string;
  designation: string;
  prixUnitaire: number;
  stockSecurite: number;
  uniteGestionCode?: string;
  photoUrl?: string;
  documents?: { id: string, fileName: string, fileUrl: string }[];
  dangerClass?: 'NONE' | 'EXPLOSIVE' | 'FLAMMABLE' | 'TOXIC' | 'CORROSIVE' | 'RADIOACTIVE' | 'ENVIRONMENTAL_HAZARD' | 'OXIDIZING' | 'COMPRESSED_GAS' | 'HARMFUL';
  createdAt?: string;
  updatedAt?: string;
}

export interface PagedResult {
  content: Item[];
  totalElements: number;
  totalPages: number;
  currentPage: number;
  pageSize: number;
}

@Injectable({
  providedIn: 'root'
})
export class ItemService {
  private apiUrl = 'http://localhost:8080/api/v1/items';
  
  // Signals Angular 17 pour la gestion d'état réactive
  items = signal<Item[]>([]);
  loading = signal<boolean>(false);
  totalElements = signal<number>(0);
  totalPages = signal<number>(0);

  constructor(private http: HttpClient) {}

  fetchItems(page: number = 0, size: number = 25, search?: string) {
    this.loading.set(true);
    let params = new HttpParams()
      .set('page', page.toString())
      .set('size', size.toString());
    
    if (search && search.trim()) {
      params = params.set('search', search.trim());
    }

    this.http.get<PagedResult>(this.apiUrl, { params }).subscribe({
      next: (data) => {
        this.items.set(data.content);
        this.totalElements.set(data.totalElements);
        this.totalPages.set(data.totalPages);
        this.loading.set(false);
      },
      error: (err) => {
        console.error('Erreur lors du chargement des articles', err);
        this.items.set([]);
        this.loading.set(false);
      }
    });
  }

  getItemById(id: string): Observable<Item> {
    return this.http.get<Item>(`${this.apiUrl}/${id}`);
  }

  updateDangerClass(id: string, dangerClass: string): Observable<Item> {
    return this.http.put<Item>(`${this.apiUrl}/${id}/danger-class`, { dangerClass });
  }

  uploadPhoto(id: string, file: File): Observable<Item> {
    const formData = new FormData();
    formData.append('file', file);
    return this.http.post<Item>(`${this.apiUrl}/${id}/upload-photo`, formData);
  }

  uploadDoc(id: string, file: File): Observable<Item> {
    const formData = new FormData();
    formData.append('file', file);
    return this.http.post<Item>(`${this.apiUrl}/${id}/upload-doc`, formData);
  }
}
