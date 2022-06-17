import pathlib

import click
import logging

from notebook_helper import execute_notebook, inspect_notebook, read_notebook, chain_notebooks
logging.basicConfig(format=' %(asctime)-15s %(levelname)7s: %(message)s', level=logging.WARNING)

root_logger = logging.getLogger()


@click.group()
# @click.version_option(version=__version__)
@click.option('--debug/--no-debug', default=False, envvar='PAPER_DEBUG')
@click.pass_context
def cli(ctx, debug):
    # View as main entry point

    if debug:
        root_logger.setLevel(logging.DEBUG)

    ctx.obj = root_logger



@cli.command()
@click.pass_context
def hello(ctx):
    """
    Super Simple function for sanity checks

    :param ctx:
    :return:
    """
    click.echo(f'Hello.')


@cli.command()
@click.option('--some_name', type=click.STRING)
@click.option('--some_number', type=click.INT)
@click.argument('in_filepath', type=click.Path(exists=True, path_type=pathlib.Path))
@click.pass_context
def exec_nb(ctx, in_filepath, some_number, some_name):
    """
    Execute (papermill) a given notebook

    :param some_name:
    :param some_number:
    :param in_filepath:
    :param ctx:
    :return:
    """
    app_logger = ctx.obj
    app_logger.debug(f"ENTERING: run_notebook, in-path: {in_filepath!r}")
    execute_notebook(
        infile_path=in_filepath,
        params={'some_name': some_name,
                'some_number': some_number}
    )


@cli.command()
@click.argument('in_filepath', type=click.Path(exists=True, path_type=pathlib.Path))
@click.pass_context
def inspect_nb(ctx, in_filepath):
    """
    Inspect (papermill) an existing notebook

    :param in_filepath:
    :param ctx:
    :return:
    """
    app_logger = ctx.obj
    app_logger.debug(f"ENTERING: app_cli:inspect_nb, in-path: {in_filepath!r}")
    inspect_notebook(in_filepath)


@cli.command()
@click.argument('in_filepath', type=click.Path(exists=True, path_type=pathlib.Path))
@click.pass_context
def read_nb(ctx, in_filepath):
    """
    read (scrapbook) an existing notebook

    :param in_filepath:
    :param ctx:
    :return:
    """
    app_logger = ctx.obj
    app_logger.debug(f"ENTERING: app_cli:read_nb, nb-path: {in_filepath!r}")
    read_notebook(in_filepath)


@cli.command()
@click.option('--some_name', type=click.STRING)
@click.option('--some_number', type=click.INT)
@click.argument('nb_one_filepath', type=click.Path(exists=True, path_type=pathlib.Path))
@click.argument('nb_two_filepath', type=click.Path(exists=True, path_type=pathlib.Path))
@click.pass_context
def chain_nbs(ctx, nb_one_filepath, nb_two_filepath, some_number, some_name):
    """
    Chain two notebooks together

    :param some_name:
    :param some_number:
    :param nb_two_filepath:
    :param nb_one_filepath:
    :param ctx:
    :return:
    """
    app_logger = ctx.obj
    app_logger.debug(f"ENTERING: app_cli:chain_notebooks, nb1-path: {nb_one_filepath!r}"
                     f" nb2-path: {nb_two_filepath!r}")
    history = chain_notebooks(nb_one_filepath, nb_two_filepath,
                              {'some_name': some_name,
                               'some_number': some_number}
                              )
    click.echo(click.style("\n\nProcessing HISTORY\n", bold=True))
    for h in history:
        click.echo(f"{h}\n\n")

