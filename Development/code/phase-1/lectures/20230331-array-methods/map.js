/* 
Build a function named writeCards() that accepts two arguments: 
 - an array of string names, 
 - and an event name. 
 
Using the .map() method, construct an array of personalized messages for each 
of the names in the provided array including the passed-in event name.

Here is an example of what a call to the writeCards() function might look like:

writeCards(["Charlie", "Samip", "Ali"], "birthday");

If we were to call the function using this function call, it should produce the following array as the return value:

[
    "Thank you, Charlie, for the wonderful birthday gift!",
    "Thank you, Samip, for the wonderful birthday gift!",
    "Thank you, Ali, for the wonderful birthday gift!",
];
*/

// function writeCards(names, event) {
//   const cards = names.map((name) => (
//    `Thank you, ${name}, for the wonderful ${event} gift!`
//    )
//   )
//   return cards
// }


// console.log(writeCards(["Thompson", "Jay", "Oli"], "birthday"))







// ===================================================

const books = [
    { title: 'The Catcher in the Rye', author: 'J.D. Salinger' },
    { title: 'To Kill a Mockingbird', author: 'Harper Lee' },
    { title: '1984', author: 'George Orwell' }
  ];
  
  /*
    Use .map() to create an array of book titles only
  */
  
  books.map(function(book){
   return book.title
  })
  