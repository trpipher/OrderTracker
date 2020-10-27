import {Item} from './item'
export interface Order {
    customer: string, 
    date: string, 
    items: Item[],
    request: string,
    total: number
}