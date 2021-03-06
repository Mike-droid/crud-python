import click
from tabulate import tabulate
from clients.services import ClientService
from clients.models import Client


@click.group()
def clients():
  """Manages the client lifecycle"""
  pass


@clients.command()
@click.option('-n', '--name', type=str, prompt=True, help="Client name")
@click.option('-c', '--compay', type=str, prompt=True, help="Client company")
@click.option('-e', '--email', type=str, prompt=True, help="Client email")
@click.option('-p', '--position', type=str, prompt=True, help="Client position")
@click.pass_context
def create(ctx, name, company, email, position):
  """Creates a new client"""
  client = Client(name, company, email, position) #No necesitamos escribir ID, lo genera automáticamente
  client_service = ClientService(ctx.obj['clients_table'])

  client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx): #el Contexto es un diccionario vacío
  """List all clients"""
  client_service = ClientService(ctx.obj['clients_table'])

  clients_list = client_service.list_clients()

  headers = [field.capitalize() for field in Client.schema()]
  table = []
  for client in clients_list:
    table.append([
      client['uid'],
      client['name'],
      client['company'],
      client['email'],
      client['position'],
    ])

  print(tabulate(table, headers))


@clients.command()
@click.pass_context
def update(ctx, client_uid):
  """Updates a client"""
  client_service = ClientService(ctx.obj['clients_table'])

  client_list = client_service.list_clients()

  client = [client for client in client_list if client['uid'] == client_uid]

  if client:
    client = _update_client_flow(Client(**client[0]))
    client_service.update_client(client)

    click.echo('client updated')
  else:
    click.echo('Client not found')


def _update_client_flow(client):
  click.echo('Leave empy if you do not want to modify the value')

  client.name = click.prompt('New name', type=str, default=client.name)
  client.company = click.prompt('New company', type=str, default=client.company)
  client.email = click.prompt('New email', type=str, default=client.email)
  client.position = click.prompt('New position', type=str, default=client.position)

  return client


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
  """Deletes a client"""
  client_service = ClientService(ctx.obj['clients_table'])

  client_list = client_service.list_clients()

  client = [client for client in client_list if client['uid'] == client_uid]

  if client:
    client_service.delete_client(client)
    click.echo('Client deleted')
  else:
    click.echo('Client not found')


def delete_client(self, client_to_be_deleted):
  clients_list = self.list_clients()
  clients_list.remove(client_to_be_deleted)
  self._save_to_disk(clients_list)


all = clients
