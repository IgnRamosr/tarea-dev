# tarea-dev
Evidencia de tarea para postulación en ruuf solar


Pasos para resolver el problema:

- Primero lo que hice fue investigar sobre qué trataba el problema, debido a que desconocía a qué tipo de problema
pertenecía este y no sabía cuáles pasos eran los que debía seguir o qué operaciones debía hacer.

- Después supe que el problema a resolver era del tipo "Packing" o de empaquetamiento y que en estos problemas hay que
optimizar el espacio de la mejor manera posible. Entonces lo primero que me salía que debía hacer era obtener cuántos objetos
caben tanto a lo ancho como en el largo y es aquí donde aplicamos la división, en este caso entera para que no nos quedara un
resultado con decimales.

- Una vez se haga la división del ancho del techo con el ancho del panel y el alto del techo con el ancho del panel multiplicamos el resultado
de estas divisiones y así es como nos da la cantidad de paneles que caben, al menos en esa orientación, ya que como tal podemos rotar los paneles
y en vez de multiplicar el ancho del techo por el ancho del panel, podemos reemplazar el ancho del panel por el alto y sucesivamente el alto del techo
por el ancho del panel, aunque esto no lo descubrí hasta más adelante.

- Ahora, una vez teniendo ese primer resultado, cuando probé los resultados ejecutando en la terminal "py manage.py" se me mostraron los inputs y fue aquí
donde pude obtener los primeros resultados y en el test 1 como en el test 3 salieron correctos, pero el test 2 salió erroneo. Entonces fue aquí donde yo me
preguntaba como podría rellenar ese espacio faltante.

- Fue entonces que lo que pensé es que debido a que me faltaba por rellenar era el alto, tenía que de alguna manera saber cuánto espacio fue el que se utilizó
y para esto multipliqué la cantidad de paneles colocados a lo alto por el alto de los paneles, quise intentar lo mismo con el ancho, sin embargo para el test 2 en específico
no tenía sentido ya que me daba como resultado 0 y es por eso que no lo utilicé para sacar un posible ancho restante. Por ende, para sacar el restante lo que hice fue
restar el alto del techo con el espacio utilizado y fue aquí que se me ocurrió crear una condicional en la que se evaluara que si el espacio restante en lo alto fuera
mayor o igual que el ancho del panel, se hiciera la misma operación que se hizo anteriormente, pero ahora con los paneles "rotados", o sea que como mencioné, en vez que sea
ancho dividido ancho y alto por alto, ahora iba a ser el ancho dividido por el alto y el alto por el ancho, pero en este caso el espacio restante que nos quedaba del techo.

- Por último al total que habíamos creado anteriormente se le suma y se le asigna la cantidad de paneles rotados que se podían colocar en el espacio restante que fue 1
y es así como logré obtener ese esperado 7.
