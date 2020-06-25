import { Component, OnInit }       from '@angular/core';
import { interval, Subscription }  from 'rxjs';
import { GridBackendService }      from '../services/grid-backend.service';
import { MatSnackBar }              from '@angular/material/snack-bar';

export interface Tile {
    color:           string;
    background:      string;
    cols:            number;
    rows:            number;
    text:            string;
    opacity:         number;
}

@Component({
    selector:    'grid-list-dynamic',
    templateUrl: './grid-list-dynamic.component.html',
    styleUrls: [ './grid-list-dynamic.component.css']
})

export class GridListDynamicComponent implements OnInit {
    tiles          : Tile[] = [];
    columns        = 4;
    timer          = 0;
    opacity        = 0;
    subscription:  Subscription;
    timerOn        = true;
    timerLabel     = 'Pause Rotation';

    constructor( private GridBackendService: GridBackendService, private snackbar: MatSnackBar  ) { }

    UpdateGrid(res) {

        this.columns = res.data.cols;
        this.tiles   = [];
        for(let row of res.data.grid){
 
            for(let cell of row){

                let tile = {
                    text: cell,
                    cols: 1,
                    rows: 1,
                    color:      'white',
                    background: '#09233c',
                    opacity: 1
                }
                this.tiles.push(tile)
            }
        }
    }

    startTimer() {
        this.subscription = interval(1000).subscribe(n => {
            this.timer++;
                this.GridBackendService.rotate_now().subscribe(
                    res => {
                        this.UpdateGrid(res);
                    },
                    error => {
                        this.toggleTimer();
                        let error_text = 'Grid ' + error.statusText + ', please wait 3 seconds';

                        const snackBar = this.snackbar.open(error_text, 'Close', {
                            duration: 3000,
                           panelClass: ['red-snackbar']
                        });

                        snackBar.afterDismissed().subscribe(() => {
                            this.toggleTimer();
                            snackBar.dismiss();
                          })
                        

 
                        
                    }
                );
        });
    }

    
    toggleTimer()  {
        if (this.timerOn)  {
            this.timerOn      = false;
            this.timerLabel   = 'Resume Rotation';
            this.stopTimer()
        }
        else {
            this.timerOn = true;
            this.startTimer()
            this.timerLabel   = 'Pause Rotation';

            
        }
    }

    stopTimer() {
        this.subscription.unsubscribe();
    }

    ngOnInit() {

        this.GridBackendService.get_initial_arr().subscribe(
            res => {
                this.UpdateGrid(res);
                this.startTimer();
            },
            error => {
                console.log(error)
            }
        );

        
        

    }

}
