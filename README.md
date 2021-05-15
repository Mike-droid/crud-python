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

## Estructuras de datos

### Uso de listas

Los Strings son inmutables.

***PELIGRO, FUENTE DE BUGS:*** Si hacemos algo como:

```python
paises = ['México','Colombia','Ecuador']
countries = paises
```

Ahora ambas listas apuntan a la misma dirección en memoria y tienen los mismos valores, **SI MODIFICAMOS UNA SE MODIFICARÁ LA OTRA TAMBIÉN**

¿Cómo solucionar esto? Simplemente haciendo una copia de la lista.

```python
paises = ['México','Colombia','Ecuador']
countries = paises[:]
```

Con esto ambas listas apuntan a una dirección en memoria diferente. Ya podemos modificarlas sin que la otra se vea afectada.

### Operaciones con listas

El método `remove()` solamente elimina el primer elemento que encuentra en una lista o tupla, no los repetidos.

### Diccionarios

### Agregando diccionarios a nuestro proyecto

### Tuplas y conjuntos

Iguales a las listas pero son inmutables.

Los conjuntos usan `sets()`.

### Tuplas y conjuntos en código

Podemos declarar sets de la forma:

```python
a = set([1, 2, 3])
b = {3, 4, 5}
```

Si tratamos de hacer: `a.add(3)` no funcionará porque los sets no pueden tener valores repetidos, en este caso sí podemos hacer, por ejemplo `a.add(20)`.

```python
A = {1, 2, 3} # conjunto A
B = {3, 4 ,5} # conjunto B
A | B #unión
{1, 2, 3, 4, 5}
A & B # intersección
{3}
A - B # diferencia entre A y B
{1, 2}
B - A # diferencia entre B y A
{4, 5}
```

[Documentación para sets](https://www.w3schools.com/python/python_sets.asp)

[Más documentación para sets](https://realpython.com/python-sets/)

### Introducción al módulo collections

El módulo collections nos brinda un conjunto de objetos primitivos que nos permiten extender el comportamiento de las built-in collections que poseé Python y nos otorga estructuras de datos adicionales. Por ejemplo, si queremos extender el comportamiento de un diccionario, podemos extender la clase UserDict; para el caso de una lista, extendemos UserList; y para el caso de strings, utilizamos UserString.

Por ejemplo, si queremos tener el comportamiento de un diccionario podemos escribir el siguiente código:

```python
class SecretDict(collections.UserDict):


  def _password_is_valid:(self, password):
    ...


    def _get_item(self, key):
      ...


      def __getitem__(self, key):
        password, key = key.split(':')

        if self._password_is_valid(password):
          return self._get_item(key)

        return None


my_secret_dict = SecretDict(...)
my_secrect_dict['some_password:some_key'] # si el password es válido, regresa el valor
```

Otra estructura de datos que vale la pena analizar, es namedtuple. Hasta ahora, has utilizado tuples que permiten acceder a sus valores a través de índices. Sin embargo, en ocasiones es importante poder nombrar elementos (en vez de utilizar posiciones) para acceder a valores y no queremos crear una clase ya que únicamente necesitamos un contenedor de valores y no comportamiento.

```python
Coffee = collections.NamedTuple('Coffee', ('size', 'bean', 'price'))

def get_coffee(coffee_type):
  if coffe_type == 'houseblend':
    return Coffee('large', 'premium', 10)
```

[Documentación oficial de collections](https://docs.python.org/3/library/collections.html)

### Python comprehensions

Son como un bucle for en 1 línea de código.

- List comprehension -> `[element for element in element_list if element_meets_condition]`
- Dictionary comprehension -> `{key: element for element in element_list if element_meets_condition}`
- Set comprehensino -> `{element for element in element_list if element_meets_condition}`

```python
student_uid = [1, 2, 3]
students = ['Juan', 'José', 'Larsen']
students_with_uid = {uid: student for uid, student in zip(student_uid, students)}
print(students_with_uid) # -> {1: 'Juan', 2: 'José', 3: 'Larsen'}
```

```python
import random
random_numbers = []
for i in range(10):
 random_numbers.append(random.randint(1,3))

print(random_numbers) # -> [1, 3, 2, 2, 3, 2, 2, 2, 1, 2]

#Eliminando números repetidos con los sets
non_repeated = {number for number in random_numbers}
print(non_repeated) # -> {1, 2, 3}
```

### Búsquedas binarias

Al resolver algoritmos tenemos que pensar en la forma más sencilla.

`list_object.sort()` ordena la lista creada y `sorted(list_object)` ordena una lista en una nueva sin modificar la original.

### Continuando con las Búsquedas Binarias

Búsqueda binaria recursiva:

```python

#Búsqueda binaria recursiva

import random


def binary_search(data, target, low, high):
  if low > high:
    return False

  mid = (low + high) // 2

  if target == data[mid]:
    return True
  elif target < data[mid]:
    return binary_search(data, target, low, mid - 1)
  elif target > data[mid]:
    return binary_search(data, target, mid + 1, high)


if __name__ == '__main__':
  data = [random.randint(0,100) for i in range(10)]

  data.sort()

  print(data)

  target = int(input('What number would you like to find?: '))
  found = binary_search(data, target, 0, len(data)-1)

  print(found)
```

Búsqueda binaria iterativa:

```python

#Busqueda binaria iterativa
import random


def run():
  def binary_search(data, target, low, high):
    while low <= high:
      mid = (low + high) // 2

      if target == data[mid]:
        return True
      elif target < data[mid]:
        high = mid - 1
      elif target > data[mid]:
        low = mid + 1


  data = [random.randint(0,100) for i in range(10)]

  data.sort()
  print(data)

  target = int(input('What number would you like to find?: '))
  found = binary_search(data, target, 0, len(data)-1)

  print(found)

if __name__ == '__main__':
  run()
```

### Manipulación de archivos en Python 3

CRUD para csv en el disco duro:

```python
import sys
import csv
import os

CLIENT_TABLE = '.clients.csv' # Los archivos con punto inicial, hacen referencia a un archivo oculto.
CLIENT_SCHEMA = ['name','company','email','position']
clients = []


def _initialize_clients_from_storage():
  if not os.path.exists(CLIENT_TABLE):
    with open(CLIENT_TABLE, mode='w'):
      pass
  else:
    with open(CLIENT_TABLE, mode='r')as f:
      reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
      for row in reader:
        clients.append(row)


def _save_clients_to_storage():
  tmp_table_name = f'{CLIENT_TABLE}.tmp'
  with open(tmp_table_name, mode='w') as f:
    writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
    writer.writerows(clients)

  os.remove(CLIENT_TABLE)
  os.rename(tmp_table_name, CLIENT_TABLE)


def _get_client_field(field_name):
  field = None

  while not field:
    field = input(f'What is the client {field_name}?: ')
  return field


def create_client(client):
  global clients

  if client not in clients:
    clients.append(client)
  else:
    print('client is already is the client\'s list')


def list_clients():
  for idx, client in enumerate(clients):
    print(f'{idx} | {client["name"]} | {client["company"]} | {client["email"]} | {client["position"]}')


def update_client(client_name, updated_client_name, updated_company, updated_email, updated_position):
  global clients

  for i in clients:
    for key,value in i.items():
      if client_name == i['name']:
        i.update([('name', updated_client_name), ('company', updated_company), ('email', updated_email), ('position', updated_position)])
  return clients


def delete_client(client_name):
  global clients

  for client in clients:
    for key,value in client.items():
      if client_name == client[key]:
        clients.remove(client)


def search_client(client_name):
  for client in clients:
    for key,value in client.items():
      if client_name == client['name']:
        print(client.items())
        break


def client_not_found():
  print('Client is not in clients list')


def _get_client_name():
  client_name = None

  while not client_name:
    client_name = input('What is the client name?: ')
    if client_name == 'exit':
      client_name = None
      break
  if not client_name:
    sys.exit()
  return client_name


def _print_welcome():
  print('WELCOME TO PLATZI SALES')
  print('*' * 50)
  print('[C]reate client')
  print('[R]ead clients')
  print('[U]pdate client')
  print('[D]elete client')
  print('[S]earch client')
  print('[E]xit program')


if __name__ == '__main__':
  _initialize_clients_from_storage()
  _print_welcome()

  command = input('What would you like to do today?: ')
  command = command.upper()


  if command == 'C':
    client = {
      'name': _get_client_field('name'),
      'company': _get_client_field('company'),
      'email': _get_client_field('email'),
      'position': _get_client_field('position'),
    }
    create_client(client)
  elif command == 'R':
    list_clients()
  elif command == 'U':
    client_name = _get_client_name()
    updated_client_name = input('What is the updated client name?: ')
    updated_company = input('What is the updated company name?: ')
    updated_email = input('What is the updated email?: ')
    updated_position = input('What is the updated position?: ')
    update_client(client_name, updated_client_name, updated_company, updated_email, updated_position)
  elif command == 'D':
    client_name = _get_client_name()
    delete_client(client_name)
  elif command == 'S':
    client_name = _get_client_name()
    found = search_client(client_name)
  elif command == 'E':
    sys.exit()
  else:
    print('Invalid command')


_save_clients_to_storage()

```
