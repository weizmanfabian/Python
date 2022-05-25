let json = [
    { id: 4, nombre: "Fabian", apellido: 'Murcia' },
    { id: 2, nombre: "Fabian", apellido: 'Tacumá' },
    { id: 3, nombre: "Esteban", apellido: 'Herreño' },
    { id: 1, nombre: "Weizman", apellido: 'Castañeda' },
]

let data = ["8", "2", "5", "9", "1"]

console.log(data.sort()) //asc
console.log(data.sort().reverse()) //des


function fieldSorterOriginal(fields) {
    return function (a, b) {
        return fields
            .map(function (o) {
                let dir = 1;
                if (o[0] === '-') {
                    dir = -1;
                    o = o.substring(1);
                }
                if (a[o] > b[o]) return dir;
                if (a[o] < b[o]) return -(dir);
                return 0;
            })
            .reduce(function firstNonZeroValue(p, n) {
                return p ? p : n;
            }, 0);
    };
}

const sortCustomJson = (fields) => (a, b) => fields.map(o => {
    let dir = 1;
    if (o[0] === '-') { dir = -1; o = o.substring(1); }
    return a[o] > b[o] ? dir : a[o] < b[o] ? -(dir) : 0;
}).reduce((p, n) => p ? p : n, 0);

console.log(json.sort(sortCustomJson(['id'])))
console.log(json.sort(sortCustomJson(['-nombre', 'apellido'])))