import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { TournoiService } from '../services/tournoi.service';

@Component({
  selector: 'app-tournoi',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  providers: [TournoiService],
  templateUrl: './tournoi.component.html',
})
export class TournoiComponent {
  title = 'Projet';
  items: any;
  showItems = false;

  constructor(private tournoiService: TournoiService) {
    this.getItems();
  }

  getItems() {
    this.tournoiService.getTournois().subscribe(
      data => {
        this.items = data;
      },
      erreur => {
        console.error('Erreur!', erreur);
      }
    );
  }

  afficherTournois() {
    this.showItems = !this.showItems;
  }
}
