import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { ItemService, Item } from '../item.service';
import { CardModule } from 'primeng/card';
import { PanelModule } from 'primeng/panel';
import { DividerModule } from 'primeng/divider';
import { ButtonModule } from 'primeng/button';
import { TagModule } from 'primeng/tag';
import { FileUploadModule } from 'primeng/fileupload';
import { DropdownModule } from 'primeng/dropdown';
import { FormsModule } from '@angular/forms';
import { MessageService } from 'primeng/api';
import { ToastModule } from 'primeng/toast';
import { QRCodeModule } from 'angularx-qrcode';
import { DialogModule } from 'primeng/dialog';
import { TableModule } from 'primeng/table';
import { InputTextModule } from 'primeng/inputtext';
import { InputTextareaModule } from 'primeng/inputtextarea';
import { StockService } from '../../stock/stock.service';
import { Stock, MouvementDto } from '../../../core/models/stock.model';
import * as JsBarcode from 'jsbarcode';

@Component({
  selector: 'app-item-detail',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule, CardModule, PanelModule, DividerModule, ButtonModule, TagModule, FileUploadModule, DropdownModule, ToastModule, QRCodeModule, DialogModule, TableModule, InputTextModule, InputTextareaModule],
  providers: [MessageService],
  templateUrl: './item-detail.component.html',
  styleUrls: ['./item-detail.component.css']
})
export class ItemDetailComponent implements OnInit {
  private route = inject(ActivatedRoute);
  private itemService = inject(ItemService);
  private stockService = inject(StockService);
  private messageService = inject(MessageService);
  
  item: Item | null = null;
  loading: boolean = true;
  error: string | null = null;
  today: Date = new Date();

  // Variables de Stock
  stocks: Stock[] = [];
  stockTotal: number = 0;
  displayMouvementModal: boolean = false;
  mouvementDto: Partial<MouvementDto> = { typeMouvement: 'ENTREE', quantite: 1 };

  dangerClasses = [
    { label: 'Aucun', value: 'NONE', image: null },
    { label: 'Explosif', value: 'EXPLOSIVE', image: 'assets/danger/picto-danger-1.png' },
    { label: 'Inflammable', value: 'FLAMMABLE', image: 'assets/danger/picto-danger-2.png' },
    { label: 'Toxique', value: 'TOXIC', image: 'assets/danger/picto-danger-6.png' },
    { label: 'Corrosif', value: 'CORROSIVE', image: 'assets/danger/GHS-pictogram-acid.svg.png' },
    { label: 'Nocif / Irritant', value: 'HARMFUL', image: 'assets/danger/webpc-passthru.webp' },
    { label: 'Danger pour l\'environnement', value: 'ENVIRONMENTAL_HAZARD', image: 'assets/danger/SGH-09.png' }
  ];

  selectedDangerClass: string = 'NONE';
  editDangerMode: boolean = false;

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.itemService.getItemById(id).subscribe({
        next: (data) => {
          this.item = data;
          this.selectedDangerClass = data.dangerClass || 'NONE';
          this.loading = false;
          this.loadStock();
          // Render Barcodes
          setTimeout(() => {
            if (this.item) {
               try {
                 const renderBarcode = (JsBarcode as any).default || JsBarcode;
                 const svgElements = document.querySelectorAll('.barcode-svg');
                 svgElements.forEach(el => {
                   renderBarcode(el, this.item!.nomenclature, {
                      format: "CODE128",
                      lineColor: "#000",
                      width: 2,
                      height: 40,
                      displayValue: true
                   });
                 });
               } catch(e) { console.error('Erreur JsBarcode', e); }
            }
          }, 100);
        },
        error: (err) => {
          this.error = 'Impossible de charger l\'article.';
          this.loading = false;
          console.error(err);
        }
      });
    } else {
      this.error = 'Identifiant introuvable.';
      this.loading = false;
    }

    // Cleanup print classes after print dialog closes
    window.addEventListener('afterprint', () => {
      document.body.classList.remove('print-document-mode');
      document.body.classList.remove('print-label-mode');
    });
  }

  getStockSeverity(stock: number): 'success' | 'warning' | 'danger' {
    if (stock > 50) return 'success';
    if (stock > 10) return 'warning';
    return 'danger';
  }

  getDangerImage(value: string): string | null {
    const found = this.dangerClasses.find(d => d.value === value);
    return found ? found.image : null;
  }

  getDangerLabel(value: string): string {
    const found = this.dangerClasses.find(d => d.value === value);
    return found ? found.label : 'Aucun';
  }

  saveDangerClass() {
    if (this.item) {
      this.itemService.updateDangerClass(this.item.id, this.selectedDangerClass).subscribe({
        next: (res) => {
          this.item = res;
          this.editDangerMode = false;
          this.messageService.add({severity:'success', summary:'Succès', detail:'Classe de danger mise à jour'});
        },
        error: () => this.messageService.add({severity:'error', summary:'Erreur', detail:'Impossible de mettre à jour'})
      });
    }
  }

  onPhotoUpload(event: any) {
    if (this.item && event.files && event.files.length > 0) {
      const file = event.files[0];
      this.itemService.uploadPhoto(this.item.id, file).subscribe({
        next: (res) => {
          this.item = res;
          this.messageService.add({severity:'success', summary:'Succès', detail:'Photo uploadée avec succès'});
        },
        error: () => this.messageService.add({severity:'error', summary:'Erreur', detail:'Impossible d\'uploader la photo'})
      });
    }
  }

  onDocUpload(event: any) {
    if (this.item && event.files && event.files.length > 0) {
      const file = event.files[0];
      this.itemService.uploadDoc(this.item.id, file).subscribe({
        next: (res) => {
          this.item = res;
          this.messageService.add({severity:'success', summary:'Succès', detail:'Document ajouté avec succès'});
        },
        error: () => this.messageService.add({severity:'error', summary:'Erreur', detail:'Impossible d\'ajouter le document'})
      });
    }
  }

  printPage() {
    document.body.classList.add('print-document-mode');
    setTimeout(() => {
      window.print();
    }, 100);
  }

  printLabel() {
    document.body.classList.add('print-label-mode');
    setTimeout(() => {
      window.print();
    }, 100);
  }

  loadStock() {
    if (this.item) {
      this.stockService.getStockByItemId(this.item.id).subscribe({
        next: (res) => {
          this.stocks = res;
          this.stockTotal = this.stocks.reduce((acc, curr) => acc + curr.quantite, 0);
        },
        error: () => console.error('Erreur chargement stock')
      });
    }
  }

  openMouvementModal() {
    this.mouvementDto = { typeMouvement: 'ENTREE', quantite: 1, magasinId: 1, itemId: this.item?.id, referenceBon: 'BE-' + new Date().getTime(), motif: '' };
    this.displayMouvementModal = true;
  }

  effectuerMouvement() {
    if (this.mouvementDto.quantite! <= 0) {
      this.messageService.add({severity:'error', summary:'Erreur', detail:'La quantité doit être supérieure à 0'});
      return;
    }
    this.stockService.effectuerMouvement(this.mouvementDto as MouvementDto).subscribe({
      next: () => {
        this.messageService.add({severity:'success', summary:'Succès', detail:'Mouvement enregistré'});
        this.displayMouvementModal = false;
        this.loadStock();
      },
      error: () => {
        this.messageService.add({severity:'error', summary:'Erreur', detail:'Impossible d\'enregistrer le mouvement'});
      }
    });
  }
}
