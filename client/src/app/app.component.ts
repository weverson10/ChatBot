import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { map, catchError } from 'rxjs/operators';
import { environment } from '@env/environment';
import { throwError } from 'rxjs';
import { AbstractControl, FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  })
};
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  submitted: Boolean = false;
  authForm: FormGroup;
  messagesList: Array<any> = [];
  constructor(
    private http: HttpClient,
    private _fb: FormBuilder
  ) {
    this.authForm = this._fb.group({
      'message': ['', [Validators.required, Validators.minLength(2)]]
    });
  }
  botMessage(value: string) {
    return this.searchMessage(value).pipe(
      map(res => {
        // console.log(res);
        this.messagesList.push(res['data']);
      }),
      catchError(err => {
        console.log(err);
        return throwError(new Error());
      })
    );
  }
  searchMessage(value: string) {
    return this.http.get(`${environment.api}/bot?message=${value}`, httpOptions);
  }
  get f() {
    return this.authForm.controls;
  }
  onSubmit(value) {
    this.submitted = true;
    const message = value['message'];
    if (this.authForm.invalid) {
      return;
    }
    this.botMessage(message).subscribe();
    this.authForm.reset();
  }
}
