# python script to take an mcell simulation that was exported from cellblender
# and output a ready-to-go WESTPA simulation, according to a single parameter file

from __future__ import print_function

import yaml
import read_config

import sys, os, subprocess, shutil, tempfile, fileinput

# read in config file
my_configs = read_config.import_config("config.yaml")


# get submitted model name
def get_submitted_model_name(submit_directory):
    mod_name_list = os.listdir(submit_directory)
    assert len(mod_name_list) == 1, "too many directories submitted"
    mod_name = mod_name_list[0]
    return mod_name

submission_directory = 'a_submission'
model_name = get_submitted_model_name(submission_directory)


# intialize new westpa sim with template
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

template_directory = 'westpa_template'
output_directory = 'output_simulation'
initialize_tempelate(template_directory,output_directory)

# copy mcell model into template
shutil.copytree(os.path.join(submission_directory,model_name),os.path.join(output_directory,'bstates',model_name))

# replace dummy model name with submitted model name

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=True):
        print(line.replace(searchExp, replaceExp), end='')


old_fake_name='some_model_dir_name' # hard caded into template
replaceAll(os.path.join(output_directory,'cleanup.sh'),old_fake_name,model_name)
