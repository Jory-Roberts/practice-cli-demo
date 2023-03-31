/* 
Example 1 - Basic usage
Loop through the cart array and log each item to the console
*/

const cart = ['Apple', 'Banana', 'Orange', 'Mango', 'Grapes']

// cart.forEach(function(fruit){
//     console.log(fruit)
// })





// ====================================
/*

Example 2 - Calculate total price
Loop through the orders array and calculate the total price of 
all the items

*/

const orders = [ 
    {id: 1, product: 'Laptop', price: 1000}, 
    {id: 2, product: 'Smartphone', price: 800}, 
    {id: 3, product: 'Tablet', price: 500}, 
    {id: 4, product: 'Camera', price: 700}, 
    {id: 5, product: 'Smartwatch', price: 300} 
]

function totalPrice(orders){
    let total = 0
    orders.forEach(function(product){
        debugger
        total += product.price
    })
    return total
}





// ==================================
/*
Example 3 - Manipulate elements of the array
Loop through the orders array and reduce the price of each order by 100 if order price is over 500
*/


