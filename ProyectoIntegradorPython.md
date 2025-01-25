# *Proyecto Integrador de Python - Adivina la Palabra*
### Descripción de lo utilizado en el código:
* **Import random:** Ayudamos a cargar el módulo random en nuestro código, en este proyecto su función fue importar de manera aleatoria una palabra de manera que el usuario no supiese con certeza cual era.
* **Decoradores:** Es una función que toma a otra función como entrada, lo que le agrega funcionalidad y nos devuelve una nueva función al código. Me ayudó a extender y moodificar de una manera más "elegante" el comportamiento de las funciones de manera que no perjudica la original.
* **Args:** Se usa para pasar muchos argumentos a la función, guardando los elementos como una tupla.
* **Kwargs:** También usado para agregar varios elementos de palabra clave que se utilizan en la función, guardándose así como un diccionario.
* **Funciones:** Es básicamente un bloque reutilizable de código, que nos ahorra tiempo, aporta organización al código... Obtiene como palabra reservada el uso de "def" y seguidamente el nombre que desee agregarle a su función.
* **Continue:** Su utilidad es dentro de un bucle, para saltarse el resto del código de la iteración actual y pasar directamente a la iteración siguiente; En este proyecto su uso fue destinado a: En el momento que no se cumpliera la condición ya sea de que la entrada no era válida, era más de una letra, o si ya la letra ingresada ya estaba en la terminal, no me terminaba el bucle directamente, sino, que me daba la oportunidad de volver a preguntar cual letra era de mi interés agregar en la terminal.
* **Break:** Permite salirse del bucle (for o while) en el momento que se cumpliera una condición, por ejemplo, acá su uso fue directamente, si ya el jugador había adivinado por completo la palabra, o si su deseo era no jugar nuevamente, entonces ya el bucle se quebraba.
* **For con Range:** Esta estructura es utilizada cuando sabemos la cantidad de repeticiones a efectuar. En este proyecto se usó solamente con un parámetro, donde el ciclo se repite mientras i sea menor que el largo de la palabra por adivinar.
* **List Comprehension:** Forma abreviada de crear listas en Python. Se pueden incluir condiciones.
* **Bucle While:** Bloque de código que permite repetir acciones con el programa de manera controlada, y se quiebra hasta que se cumpla la condición que usted desee. Ya sea true, false, break...
* **\n:** Nos ayuda a hacer saltos de línea para que todo se pueda ver de manera más organizada.
* **Listas:** Estructura de datos que nos permite almacenar una colección de elementos separado por comas, y encerrado entre corchetes [], acá fue utilizado para agregar las letras incorrectas, las correctas, y el grupo de palabras para adivinar del juego.
* **==:** Por si se quiere comparar si dos variables tienen el mismo valor.
* **!=:** Si desea verificar si las variables o cadenas de texto son distintas dé.
