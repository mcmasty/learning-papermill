import pathlib
import os
import logging
import random
import string
from typing import List

import papermill as pm
import scrapbook as sb


def execute_notebook(infile_path: pathlib.Path, params: dict) -> str:
    my_log = logging.getLogger()
    my_log.debug(f"ENTERING: execute_notebook {infile_path!r}")
    basepath, basename = os.path.split(infile_path)
    # TODO: Maybe add timestamp or some other snippet if uniqueness is required ...
    outname = basename.replace('.', '_out.')
    my_log.debug(f" Output Filename: {outname!r} in path: {basepath!r}")
    out_path = os.path.join(basepath, outname)
    pm.execute_notebook(
        infile_path,
        out_path,
        parameters=params
    )
    return out_path


def inspect_notebook(nbfile_path: pathlib.Path) -> dict:
    my_log = logging.getLogger()
    my_log.debug(f"ENTERING: inspect_notebook {nbfile_path!r}")
    result = pm.inspect_notebook(nbfile_path)
    my_log.debug(f"Notebook Inspection: {result}")
    return result



def read_notebook(nbfile_path: pathlib.Path) -> dict:
    my_log = logging.getLogger()
    my_log.debug(f"ENTERING: read_notebook {nbfile_path!r}")
    result_nb = sb.read_notebook(str(nbfile_path))  # Requires String formatted path...
    my_log.info(result_nb.scraps.data_dict)
    # for k, v in result_nb.scraps.data_dict.items():
    #     print(f"Scrap: Key: {k}, Value: {v}")
    return result_nb.scraps.data_dict


def chain_notebooks(nb_one_path: pathlib.Path, nb_two_path: pathlib.Path, initial_params: dict) -> List:
    my_log = logging.getLogger()
    my_log.debug(f"ENTERING: chain_notebooks NB1: {nb_one_path!r} "
                 f"NB2: {nb_two_path!r} " 
                 f"Initial params: {initial_params}")

    history = list()

    history.append({'notebook_one_default_nb_params': inspect_notebook(nb_one_path)})
    history.append({'notebook_one_input_params': initial_params})

    # Execute Notebook One with init_params
    out_one_nb = execute_notebook(nb_one_path, initial_params)
    history.append({'notebook_one_out_nb_path': out_one_nb})
    history.append({'notebook_one_out_default_nb_params': inspect_notebook(out_one_nb)})


    # Read Results
    sb_scap_dict = read_notebook(out_one_nb)
    my_log.info(sb_scap_dict)
    history.append({'notebook_one_saved_scraps': sb_scap_dict})

    new_value = sb_scap_dict['number'] * random.randint(2, 10)

    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(18))
    new_params = {
        'some_name': random_string,
        'some_number': new_value
    }

    # Use as results from notebook_one as parameters to notebook two
    history.append({'notebook_twp_default_nb_params': inspect_notebook(nb_two_path)})
    history.append({'notebook_two_input_params': new_params})

    out_two_nb = execute_notebook(nb_two_path, new_params)
    history.append({'notebook_two_out_nb_path': out_two_nb})
    history.append({'notebook_two_out_default_nb_params': inspect_notebook(out_two_nb)})

    sb2_scrap_dict = read_notebook(out_two_nb)
    history.append({'notebook_two_saved_scraps': sb2_scrap_dict})

    my_log.info(sb_scap_dict)

    return history
