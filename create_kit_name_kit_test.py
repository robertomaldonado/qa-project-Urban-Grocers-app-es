from sender_stand_request import *
import sender_stand_request
import data

# Create a user and retrieve auth token


def create_new_user_token_on_success():
  user_response = sender_stand_request.post_new_user(data.user_body)
  return user_response.json()["authToken"]


def positive_assert(kit_body, auth_token):
  # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
  user_response = sender_stand_request.post_new_kit(kit_body, auth_token)

  # Comprueba si el código de estado es 201
  assert user_response.status_code == 201

  # Comprueba que el campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
  assert user_response.json()["name"] == kit_body["name"]


def negative_assert(kit_body, auth_token):
  # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
  user_response = sender_stand_request.post_new_kit(kit_body, auth_token)

  # Comprueba si el código de estado es 400
  assert user_response.status_code == 400


"""
Kit test 1.
El número permitido de caracteres (1): kit_body = { "name": "a"}
"""


def test_create_kit_1_letter_in_name_get_success_response():
  auth_token = create_new_user_token_on_success()
  positive_assert({"name": "a"}, auth_token)


"""
Kit test 2.
El número permitido de caracteres (511)
"""


def test_create_kit_511_letters_in_name_get_success_response():
  auth_token = create_new_user_token_on_success()
  positive_assert(data.kit_body_name_limit, auth_token)


"""
Kit test 3.
El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
"""


def test_create_kit_0_letters_in_name_get_error_response():
  auth_token = create_new_user_token_on_success()
  negative_assert({"name": ""}, auth_token)


"""
Kit test 4.
El número de caracteres es mayor que la cantidad permitida (512)
"""


def test_create_kit_512_letters_in_name_get_error_response():
  auth_token = create_new_user_token_on_success()
  negative_assert(data.kit_body_name_exceeds_limit, auth_token)


"""
Kit test 5.
Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
"""


def test_create_kit_special_chars_in_name_get_success_response():
  auth_token = create_new_user_token_on_success()
  positive_assert({"name": "\"№% @\","}, auth_token)


"""
Kit test 6.
Se permiten espacios: kit_body = { "name": " A Aaa " }
"""


def test_create_kit_whitespaces_in_name_get_success_response():
  auth_token = create_new_user_token_on_success()
  positive_assert({"name": " A Aaa "}, auth_token)


"""
Kit test 7.
Se permiten números: kit_body = { "name": "123" }
"""


def test_create_kit_numbers_as_string_in_name_get_success_response():
  auth_token = create_new_user_token_on_success()
  positive_assert({"name": "123"}, auth_token)


"""
Kit test 8.
El parámetro no se pasa en la solicitud: kit_body = { }
"""


def test_create_kit_empty_json_get_error_response():
  auth_token = create_new_user_token_on_success()
  negative_assert({}, auth_token)


"""_
Kit test 9.
Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
"""


def test_create_kit_different_param_type_in_name_get_error_response():
  auth_token = create_new_user_token_on_success()
  negative_assert({"name": 123}, auth_token)
