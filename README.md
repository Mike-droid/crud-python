# Curso práctico de Python - Creación de un CRUD

## Básicos del Lenguaje

### ¿Qué es la programación?

Combinación entre Ciencias de la computación (Matemáticas, Ingeniería, Ciencia). La habilidad más importante de un programador es **resolver problemas**.

Un programa es una secuencia de instrucciones lógica.

### ¿Por qué programar con Python?

- Comunidad
- Facilidad de uso
- Librerías
- Popularidad
- Industria

[Documentación oficial de Turtle en Python](https://docs.python.org/3/library/turtle.html#module-turtle)

### Operadores matemáticos

### Variables y expresiones

Las variables son contenedores de valores.

```python
message = 'Hello' #variable
_age = 20 #variable privada
PI = 3.14159 # convencion de constantes
__do_not_touch = 'Something important' # NO MODIFICAR POR FAVOR
```

- Expresiones: Es una combinación de valores, variables y operadores, ejemplo: 2+2
- Enunciado: es una unidad de código que tiene un efecto, ejemplo: age = 20

PEMDAS -> Paréntesis, Exponente, Multiplicación, División, Adición, Substracción

### Presentación del proyecto

[Creación de entornos virtuales en Windows](https://docs.python.org/es/3.8/library/venv.html)

En cmd -> `C:\> <venv>\Scripts\activate.bat`

### Usando funciones en nuestro proyecto

### Operadores lógicos

### Estructuras condicionales

## Uso de strings y ciclos

### Strings en Python

El método `id(objeto)` nos regresa la dirección de memoria donde se encuentra un valor de Python.

### Operaciones con Strings en Python

La función `dir(objeto)` nos muestra un listado de las cosas que podemos hacer con ese objeto.

`help(objeto)` nos regresa el mensaje que se encuentra en las 6 comillas dobles.

### Operaciones con strings y el comando Update

### Operaciones con strings y el comando Delete

### Operaciones con strings: Slices en Python

### Foor loops

### While loops

### Iterators and generators

Aunque no lo sepas, probablemente ya utilices iterators en tu vida diaria como programador de Python. Un iterator es simplemente un objeto que cumple con los requisitos del Iteration Protocol (protocolo de iteración) y por lo tanto puede ser utilizado en ciclos. Por ejemplo,

```python
for i in range(10):
  print(i)
```

En este caso, la función range es un iterable que regresa un nuevo valor en cada ciclo. Para crear un objeto que sea un iterable, y por lo tanto, implemente el protocolo de iteración, debemos hacer tres cosas:

- Crear una clase que implemente los métodos iter y next
- iter debe regresar el objeto sobre el cual se iterará
- next debe regresar el siguiente valor y aventar la excepción StopIteration cuando ya no hayan elementos sobre los cual iterar.

Por su parte, los generators son simplemente una forma rápida de crear iterables sin la necesidad de declarar una clase que implemente el protocolo de iteración. Para crear un generator simplemente declaramos una función y utilizamos el keyword yield en vez de return para regresar el siguiente valor en una iteración. Por ejemplo,

```python
def fibonacci(max):
  a, b = 0, 1
  while a < max:
    yield a
    a, b = b, a+b
```

Es importante recalcar que una vez que se ha agotado un generator ya no podemos utlizarlo y debemos crear una nueva instancia. Por ejemplo,

```python
fib1 = fibonacci(20)
fib_nums = [num for num in fib1]
...
double_fib_nums = [num * 2 for num in fib1] # no va a funcionar
double_fib_nums = [num * 2 for num in fibonacci(30)] # sí funciona
```
