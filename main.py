# python script to take an mcell simulation that was exported from cellblender
# and output a ready-to-go WESTPA simulation, according to a single parameter file


import yaml
import read_config

import os, subprocess, shutil, tempfile

template_directory = 'westpa_template'
output_directory = 'output_simulation'

def initialize_tempelate(template_dir,output_dir):
    # delete previous copy of output_simulationr
    try:
       shutil.rmtree(output_dir)
    except OSError:
       if not os.path.isdir(output_dir):
           pass

    # make new copy of output_simulation
    try:
        shutil.copytree(template_dir,output_dir)
    except OSError:
        if os.path.isdir(output_dir):
            pass

initialize_tempelate(template_directory,output_directory)
