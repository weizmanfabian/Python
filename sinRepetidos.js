//dada una cadena de texto contar cuantas veces aparece cada una de las palábras en el mismo
const text = "Good day dear user te enviamos los temas de nuestros high 5 para que realices tus 3 programaciones mínimas. Recuerda realizar una programación balanceada Reading high 5 co-working y el READ training system la formula de trabajo en casa, donde debes avanzar 1 historia en el storybook y 2 unidades gramaticales en el workbook cada semana. Si se te presenta alguna duda, escríbenos a nuestro número de coordinación académica 3103692431. ¡Sigue Aprendiendo!"

const normalize = (word) => {
  // return word.toLowerCase().replace(',',"").replace(".","").replace("!","") //opción larga
  //expresión regular
  return word.toLowerCase().replace(/[.!,¡]/g, "")
}

const wordRepetitions = (text) => {
  let dic = {}
  let separatedWords = text.split(" ")
  for (let word of separatedWords) {
    if (normalize(word) in dic) {
      ++dic[normalize(word)]
    } else {
      dic[normalize(word)] = 1
    }
  }
  console.log(dic);
}

wordRepetitions(text)