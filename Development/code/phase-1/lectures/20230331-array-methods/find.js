// Use the find method to find the first even number

const numbers = [7, 33, 11, 10, 12, 8];

const firstEven = numbers.find(function(num){
    return num % 2 === 0
})






// Use the find method to find the first student with a grade of 90

const students = [
  { name: 'Alice', grade: 85 },
  { name: 'Bob', grade: 72 },
  { name: 'Charlie', grade: 90 },
  { name: 'David', grade: 65 }
];

const overAchiever = students.find((student) => {
    return student.grade === 90
})



