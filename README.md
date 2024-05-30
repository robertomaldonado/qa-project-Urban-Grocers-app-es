![Python](https://img.shields.io/badge/python-3.11.3-blue?logo=python)
![Pytest](https://img.shields.io/badge/pytest-8.1.1-blue?logo=pytest)

# Quality Assurance Tests para Urban Grocers [Creacion de Kit]

Pruebas automatizadas para la aplicacion Urban Grocers, seccion de creacion de kits de comida.

## Para ejecutar las pruebas:

Requisitos Previos:

- Instalar librerias pytest y requests:
  > > pip3 install pytest  
  > > pip3 install requests
- o instalar desde requests.txt
  > > pip3 install -r requirements.txt

Formas de ejecutar las pruebas:

1.  python3 -m pytest <Path-to-test-file>.py -vv -s
2.  Ejecución por medio del IDE

## Fuente de documentacion:

- PDoc: Visita la documentacion de las pruebas realizadas en [Archivos de documentacion](docs/index.html)

## Tecnologias y Tecnicas aplicadas:

- Librerias de Python (Para un detalle y version de las librerias revisa [requirements.txt file](requirements.txt))
  pytest
  requests

## Descripcion de la prueba | Resultado esperado:

1. El número permitido de caracteres (1): kit_body = { "name": "a"}
   Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

2. El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
   Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud

3. El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
   Código de respuesta: 400

4. El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }
   Código de respuesta: 400

5. Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
   Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

6. Se permiten espacios: kit_body = { "name": " A Aaa " }
   Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

7. Se permiten números: kit_body = { "name": "123" }
   Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

8. El parámetro no se pasa en la solicitud: kit_body = { }
   Código de respuesta: 400

9. Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
   Código de respuesta: 400
