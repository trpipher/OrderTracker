import { Component, OnInit, Input } from '@angular/core';
import {Order} from '../interfaces/order';
import {Item} from '../interfaces/item';
@Component({
  selector: 'order-detail',
  templateUrl: './order-detail.component.html',
  styleUrls: ['./order-detail.component.css']
})
export class OrderDetailComponent implements OnInit {

  
  @Input() order: Order
  constructor() { }

  ngOnInit(): void {
  }

  onSelect(item: Item): void{
    item.completed = !item.completed
  }
}
