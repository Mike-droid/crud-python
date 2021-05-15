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
