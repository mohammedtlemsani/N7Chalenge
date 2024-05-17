import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SpamsComponent } from './spams.component';

describe('SpamsComponent', () => {
  let component: SpamsComponent;
  let fixture: ComponentFixture<SpamsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SpamsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SpamsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
