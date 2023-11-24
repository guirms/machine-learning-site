import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private http: HttpClient) { }

  getPredict(text: string): Observable<string> {
    const params = new HttpParams()
      .set('text_request', text);

    // const apiUrl = 'http://127.0.0.1:5000/getPredict';
    const apiUrl = 'https://machine-learning-api-slnh.onrender.com/';

    return this.http.get<string>(apiUrl + 'getPredict', { params });
  }
}
