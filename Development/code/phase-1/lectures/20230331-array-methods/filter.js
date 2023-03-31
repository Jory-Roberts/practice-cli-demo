// Use the filer method to create an array of only even numbers

const nums = [8, 1, 9, 4, 5, 6, 7, 3, 2, 11, 15, 13, 14, 10, 12]

const evens = nums.filter(function(num){
    return num % 2 === 0
})


// Use filter to create an array of characters whose name begins with 'M'
const characters = [
  { name: 'Mario', x: 100, y: 100 },
  { name: 'Luigi', x: 200, y: 100 },
  { name: 'Peach', x: 300, y: 100 },
  { name: 'Bowser', x: 400, y: 100 },
  { name: 'Wario', x: 500, y: 100 },
  { name: 'Yoshi', x: 100, y: 200 },
  { name: 'Donkey Kong', x: 200, y: 200 },
  { name: 'Diddy Kong', x: 300, y: 200 },
  { name: 'Link', x: 400, y: 200 },
  { name: 'Zelda', x: 500, y: 200 },
  { name: 'Kirby', x: 100, y: 300 },
  { name: 'Meta Knight', x: 200, y: 300 },
  { name: 'King Dedede', x: 300, y: 300 },
  { name: 'Samus', x: 400, y: 300 },
  { name: 'Captain Falcon', x: 500, y: 300 },
  { name: 'Sonic', x: 100, y: 400 },
  { name: 'Tails', x: 200, y: 400 },
  { name: 'Knuckles', x: 300, y: 400 },
  { name: 'Dr. Eggman', x: 400, y: 400 },
  { name: 'Shadow', x: 500, y: 400 },
  { name: 'Pikachu', x: 100, y: 500 },
  { name: 'Charizard', x: 200, y: 500 },
  { name: 'Mewtwo', x: 300, y: 500 },
  { name: 'Greninja', x: 400, y: 500 },
  { name: 'Incineroar', x: 500, y: 500 },
  { name: 'Isabelle', x: 100, y: 600 },
  { name: 'Tom Nook', x: 200, y: 600 },
  { name: 'Digby', x: 300, y: 600 },
  { name: 'Waldo', x: 400, y: 600 },
  { name: 'Wenda', x: 500, y: 600 }
];


const mCharacters = characters.filter(character => character.name[0].toLowercase() === "m")