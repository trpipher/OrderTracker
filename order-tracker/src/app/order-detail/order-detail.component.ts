import { Component, OnInit, Input } from '@angular/core';
import {Order} from '../interfaces/order'
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

  onSelect(item){
    item.completed = !item.completed
  }
}
