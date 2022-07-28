//encontrar el mayor con la cantidad de veces que aparece
const list = [1, 2, 1, 3, 3, 8, 9, 9, 5]

const mayor = Math.max(...list)
let cantidadVeces = list.reduce((acc, v) => v == mayor ? acc + 1 : acc + 0, 0)
console.log(mayor);
console.log(cantidadVeces);


