import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SpamComponent } from './spam.component';

describe('SpamComponent', () => {
  let component: SpamComponent;
  let fixture: ComponentFixture<SpamComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SpamComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SpamComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
