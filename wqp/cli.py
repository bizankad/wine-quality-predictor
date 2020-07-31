import click
from wqp import __version__

@click.group(name = 'wqp') 
@click.version_option(__version__) 
def wqp():
    pass
