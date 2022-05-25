/* Realice un algoritmo o pseudo-código que explique cómo resolver la siguiente situación: En un vector de enteros, 
no necesariamente ordenado, calcule el número de veces que aparece el máximo y el mínimo de sus elementos en una sola pasada 
(es decir recorriendo el vector una sola vez).
*/

let d = [2, 7, 2, 3, 7, 9, 2, 9]

let max = Math.max(...d)
let min = Math.min(...d)

// let cantMax = d.filter(x => x == max).length
// let cantMin = d.filter(x => x == min).length

let cantMax = 0
let cantMin = 0

for (let i = 0; i < d.length; i++) {
    cantMax += d[i] == max ? 1 : 0
    cantMin += d[i] == min ? 1 : 0
}

console.log(max + ' => ' + cantMax);
console.log(min + ' => ' + cantMin);



/*
Explique cómo resolvería el siguiente problema basado en una lógica de desarrollo: 
Existe una cola de mensajes que es usada para priorizar la ejecución de procesos; 
existiendo dos tipos de procesos, el primero dura 20 segundos y el segundo dura 1 minuto.  
Cómo haría para optimizar la atención de cada proceso y de manera que el tiempo de espera sea inferior a 2 minutos?



*/

let procesos = [
    { name: "first", time: 20, procesos: 6 },
    { name: "second", time: 60, procesos: 2 }
]
let colaMsg = 1

/*
desviaría todo al proceso 1, sin embargo a la cola para priorizar procesos le desviaría más el proceso de 1 minuto para agilizar todo, 
esto debido a que si el proceso si o si dura 1 minuto, no podemos cortar este tiempo
hay que disponer de más hilos o ejecuciones simultáneas para abastecer la demanda
*/

