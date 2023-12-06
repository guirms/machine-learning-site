import { Component } from '@angular/core';
import { HttpService } from './services/http.service';
import { HttpErrorResponse } from '@angular/common/http';
import { PredictResult } from './objects/PredictResult';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  textRequest!: string | null;
  textResponse!: string | null;

  predictResult: PredictResult[] = [
    {
      best_accuracy: 98.02,
      best_params: {
        c: 10,
        gamma: 1,
        kernel: "rbf"
      },
      classification_report: {
        f1_score: {
          accuracy: 0.98,
          b: 0.99,
          m: 0.98,
          macro_avg: 0.98,
          weighted_avg: 0.98
        },
        precision: {
          b: 0.97,
          m: 1.0,
          macro_avg: 0.99,
          weighted_avg: 0.98
        },
        recall: {
          b: 1.0,
          m: 0.95,
          macro_avg: 0.98,
          weighted_avg: 0.98
        },
        support: {
          accuracy: 114.0,
          b: 71.0,
          m: 43.0,
          macro_avg: 114.0,
          weighted_avg: 114.0
        }
      },
      model: "SVC"
    },
    {
      best_accuracy: 96.48,
      best_params: {
        metric: "euclidean",
        n_neighbors: 7,
        weights: "uniform"
      },
      classification_report: {
        f1_score: {
          accuracy: 0.96,
          b: 0.97,
          m: 0.94,
          macro_avg: 0.95,
          weighted_avg: 0.96
        },
        precision: {
          b: 0.96,
          m: 0.95,
          macro_avg: 0.96,
          weighted_avg: 0.96
        },
        recall: {
          b: 0.97,
          m: 0.93,
          macro_avg: 0.95,
          weighted_avg: 0.96
        },
        support: {
          accuracy: 114.0,
          b: 71.0,
          m: 43.0,
          macro_avg: 114.0,
          weighted_avg: 114.0
        }
      },
      model: "KNeighborsClassifier"
    },
    {
      best_accuracy: 94.07,
      best_params: {
        criterion: "entropy",
        min_samples_leaf: 5,
        min_samples_split: 5,
        splitter: "random"
      },
      classification_report: {
        f1_score: {
          accuracy: 0.96,
          b: 0.97,
          m: 0.94,
          macro_avg: 0.95,
          weighted_avg: 0.96
        },
        precision: {
          b: 0.96,
          m: 0.95,
          macro_avg: 0.96,
          weighted_avg: 0.96
        },
        recall: {
          b: 0.97,
          m: 0.93,
          macro_avg: 0.95,
          weighted_avg: 0.96
        },
        support: {
          accuracy: 114.0,
          b: 71.0,
          m: 43.0,
          macro_avg: 114.0,
          weighted_avg: 114.0
        }
      },
      model: "DecisionTreeClassifier"
    }
  ];

  constructor(private httpService: HttpService) { }

  getPredict(): void {
    if (!this.textRequest) {
      alert('Digita alguma coisa o seu chinelao');
      return;
    }

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
