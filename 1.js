

// Realice un algoritmo o pseudo-código que permita ordenar de mayor a menor, cuatro números ingresados en cualquier orden. (no usar sort)
let data = [1, 7, 2, 3]

let newData = []
let mayor = 0
for (let i = 0; i < data.length; i++) {
    let mayorInterno = 0
    for (let y = 0; y < data.length; y++) {
        if (mayorInterno < data[y]) {
            if (newData.length == 0) {
                mayor = data[y]
                mayorInterno = data[y]
                continue
            }
            if (data[y] < mayor) {
                mayorInterno = data[y]
            }
        }
        if (data[y] == mayor) {
            continue
        }
    }
    newData.push(mayorInterno)
    mayor = mayorInterno
}

console.log(newData);