import { TestBed } from '@angular/core/testing';

import { GridBackendService } from './grid-backend.service';

describe('GridBackendService', () => {
    let service: GridBackendService;

    beforeEach(() => {
        TestBed.configureTestingModule({});
        service = TestBed.inject(GridBackendService);
    });

    it('should be created', () => {
        expect(service).toBeTruthy();
    });
});
