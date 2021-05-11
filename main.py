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


def _add_comma():
  global clients

  clients += ','


def _print_welcome():
  print('WELCOME TO PLATZI SALES')
  print('*' * 50)
  print('[C]reate client')
  print('[D]elete client')


if __name__ == '__main__':
  _print_welcome()

  command = input('What would you like to do today?: ')
  if command == 'C' or command == 'c':
    client_name = input('What is the client name?: ')
    create_client(client_name)
    list_clients()
  elif command == 'D' or command == 'd':
    pass
  else:
    print('Invalid command')