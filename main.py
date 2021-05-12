import sys

clients = 'Miguel,Daniel,'


def create_client(client_name):
  global clients

  if client_name not in clients:
    clients += client_name
    _add_comma()
  else:
    print('client is already is the client\'s list')


def list_clients():
  global clients

  print(clients)


def update_client(client_name, updated_client_name):
  global clients

  if client_name in clients:
    clients = clients.replace(client_name + ',' , updated_client_name)
  else:
    client_not_found()


def delete_client(client_name):
  global clients

  if client_name in clients:
    clients = clients.replace(client_name + '+' , '')
  else:
    client_not_found()


def search_client(client_name):
  clients_list = clients.split(',')

  for client in clients_list:
    if client != client_name:
      continue
    else:
      return True #return siempre termina la ejecución de una función


def _add_comma():
  global clients

  clients += ','


def client_not_found():
  print('Client is not in clients list')


def _print_welcome():
  print('WELCOME TO PLATZI SALES')
  print('*' * 50)
  print('[C]reate client')
  print('[R]ead clients')
  print('[U]pdate client')
  print('[D]elete client')
  print('[S]earch client')
  print('[E]xit program')


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


if __name__ == '__main__':
  _print_welcome()

  command = input('What would you like to do today?: ')
  command = command.upper()


  if command == 'C':
    client_name = _get_client_name()
    create_client(client_name)
    list_clients()
  elif command == 'R':
    list_clients()
  elif command == 'U':
    client_name = _get_client_name()
    updated_client_name = input('What is the updated client name?: ')
    update_client(client_name, updated_client_name)
    list_clients()
  elif command == 'D':
    client_name = _get_client_name()
    delete_client(client_name)
    list_clients()
  elif command == 'S':
    client_name = _get_client_name()
    found = search_client(client_name)

    if found:
      print('the client is in the client\'s list')
    else:
      print(f'The client {client_name} is not in our client\'s list')
  elif command == 'E':
    sys.exit()
  else:
    print('Invalid command')
