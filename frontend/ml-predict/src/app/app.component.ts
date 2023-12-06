import { Component, OnInit } from '@angular/core';
import { HttpService } from './services/http.service';
import { HttpErrorResponse } from '@angular/common/http';
import { PredictResult } from './objects/PredictResult';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  predictResult!: PredictResult[];
  isLoading = false;

  constructor(private httpService: HttpService) { }

  ngOnInit(): void {
    this.getPredict();
  }

  getPredict(): void {
    this.isLoading = true;

    this.httpService.getPredict()
      .subscribe({
        next: (result) => {
          this.isLoading = false;

          this.predictResult = result;
        },
        error: (error: HttpErrorResponse) => {
          this.isLoading = false;

          alert('Erro na requsição: ' + error.status);
        }
      });
  }
}
