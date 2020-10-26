import { Component } from '@angular/core';
import { Order } from './interfaces/order';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'order-tracker';

  orders: Order[] = [
  {items: [
  {count: 2, name: "Salmon [FS]", flavor: "", request: "Plain, with just a little lemon. Low sodium, no pepper. ", addition: "Lemon Pepper", price: 36, portion: "", sides: ""}, 
  {count: 1, name: "Green Beans [FS]", flavor: "", request: "", addition: "", price: 7, portion: "", sides: ""},
  {count: 2, name: "Custom Menu Item", flavor: "", request: "Two petite filet mignons, 6-8 oz each, cooked medium rare. Very little salt and pepper. In the meat juice, no sauces. I understand the price will be higher than $14. ", addition: "", price: 28, portion: "", sides: ""}, 
  {count: 1, name: "Custom Menu Item", flavor: "", request: "mesclun salad with pecans and a little goat cheese. Balsamic vinegarette. ", addition: "", price: 14, portion: "", sides: ""}, 
  {count: 1, name: "Grilled Chicken Breast", flavor: "", request: "Keep it plain. Low sodium. A pinch of salt, a pinch of pepper. A bit of lemon is ok. ", addition: "Chef's Choice", price: 15, portion: "DoulePortion($5)", sides: ""},
  {count: 2, name: "Red Potatoes", flavor: "", request: "", addition: "", price: 7, portion: "", sides: ""}, 
  {count: 1, name: "Jasmine Rice", flavor: "", request: "", addition: "", price: 3, portion: "", sides: ""}, 
  {count: 1, name: "Carrots", "flavor": "", request: "", addition: "", price: 3.50, portion: "", sides: ""}], 
  request: "Keep everything low sodium. If when you are shopping you come across one piece of cheesecake, can you please include that? I can send a separate PayPal. ",
  total: 129.36, 
  customer: "Mari Vasan", 
  date: "Tuesday 10/20/2020"},
  {items: [
    {count: 1, name: "Grilled Chicken Breast", flavor: "", request: "", addition: "Jamaican Jerk", price: 10, portion: "Single Portion", sides: "Steamed Broccoli, Roasted Red Potatoes"}, 
    {count: 2, name: "Custom Menu Item", flavor: "", request: "Meatloaf/hamburger steak, with brown gravy on meat & on mashed potatoes, cauliflower mac & cheese ", addition: "", price: 28, portion: "", sides: ""}, 
    {count: 2, name: "Beef Flank Steak", flavor: "", request: "pico de gallo and tortillas ", addition: "Latin/Mexican", price: 24, portion: "Single Portion", sides: "Sauteed Peppers & Onions"}, 
    {count: 1, name: "Pork Loin", flavor: "", request: "", addition: "Fresh Herbs", price: 10, portion: "Single Portion", sides: "Rainbow Carrots, Roasted Red Potatoes"}, 
    {count: 1, name: "Frittata Mushroom & Onion Egg Bites", flavor: "", request: "", addition: "", price: 5, portion: "", sides: ""}, 
    {count: 1, name: "Frittata Broccoli, Cheese & Ham Egg Bites", flavor: "", request: "", addition: "", price: 5, portion: "", sides: ""}], 
    request: "", 
    total: 94.83, 
    customer: "DEIDRE ROBICHEAUX", 
    date: "Tuesday 10/27/2020"}]
  
}
