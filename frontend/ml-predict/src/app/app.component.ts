import { Component } from '@angular/core';
import { HttpService } from './services/http.service';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  textRequest!: string | null;
  textResponse!: string | null;

  constructor(private httpService: HttpService) { }

  getPredict(): void {
    this.httpService.getPredict(this.textRequest!)
      .subscribe({
        next: (result) => {
          this.textResponse = result;
        },
        error: (error: HttpErrorResponse) => {
          alert('Erro na requsição: ' + error.status);
        }
      });
  }

  clear(): void {
    this.textRequest = this.textResponse = null;
  }
}
