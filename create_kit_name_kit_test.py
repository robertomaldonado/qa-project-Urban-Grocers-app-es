from sender_stand_request import *
import sender_stand_request
import data

# Create a user and retrieve auth token


def create_new_user_token_on_success():
  user_response = sender_stand_request.post_new_user(data.user_body)
  return user_response.json()["authToken"]


""" 
Kit test 1.
El número permitido de caracteres (1): kit_body = { "name": "a"}
201
"""


def test_1():
  pass


""" 
Kit test 2.
El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
201
"""


def test_2():
  pass


"""
Kit test 3.
El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
400
"""


def test_3():
  pass


"""
Kit test 4.
El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }
400
"""


def test_4():
  pass


"""
Kit test 5.
Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
201
"""


def test_5():
  pass


"""
Kit test 6.
Se permiten espacios: kit_body = { "name": " A Aaa " }
201
"""


def test_6():
  pass


"""
Kit test 7.
Se permiten números: kit_body = { "name": "123" }
201
"""


def test_7():
  pass


"""
Kit test 8.
El parámetro no se pasa en la solicitud: kit_body = { }
400
"""


def test_8():
  pass


"""
Kit test 9.
Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
400
"""


def test_9():
  pass


if __name__ == "__main__":
  user_token = create_new_user_token_on_success()
