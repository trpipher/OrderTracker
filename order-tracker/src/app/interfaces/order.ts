import {item} from './item'
export interface Order {
    customer: string, 
    date: string, 
    items: item[],
    request: string,
    total: number
}