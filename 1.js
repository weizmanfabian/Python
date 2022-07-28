

// Realice un algoritmo o pseudo-código que permita ordenar de mayor a menor, cuatro números ingresados en cualquier orden. (no usar sort)
let data = [9, 7, 1, 5]

const newData = data.reduce((accEx, numEx) => {
    let mayor;
    const majorInterno = data.reduce((majorIn, numIn) => {
        if (mayorInterno < numIn) {
            if (newData.length == 0) {
                mayor = numIn
                majorIn = numIn
                continue
            }
            if (numIn < mayor) {
                mayorInterno = numIn
            }
        }
        if (numIn == mayor) {
            continue
        }
        return numIn
    }, mayor)
    return [...accEx, majorInterno]
}, [])
console.log(newData);
// for (let numEx of data) {
//     let mayorInterno
//     for (let numIn of data) {
//         if (mayorInterno < numIn) {
//             if (newData.length == 0) {
//                 mayor = numIn
//                 mayorInterno = numIn
//                 continue
//             }
//             if (numIn < mayor) {
//                 mayorInterno = numIn
//             }
//         }
//         if (numIn == mayor) {
//             continue
//         }
//     }
//     newData.push(mayorInterno)
//     mayor = mayorInterno
// }
// console.log(newData);