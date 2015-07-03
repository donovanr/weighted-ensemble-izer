# python script to take an mcell simulation that was exported from cellblender
# and output a ready-to-go WESTPA simulation, according to a single parameter file

from __future__ import print_function

import sys, os, subprocess, shutil, tempfile, fileinput

import yaml
import util.read_config as read_config
import util.file_io as file_io

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--configfile', required=True)
parser.add_argument('-s', '--submissiondirectory', required=True)
args = parser.parse_args()

config_file = args.configfile
submission_directory = args.submissiondirectory

# config_file = 'config.yaml'
# submission_directory = 'a_submission'
# output_directory = 'we_simulation'

template_directory = 'westpa_template'


# read in config file
my_configs = read_config.import_config(config_file)

# get submitted model name and set output directory
model_name = file_io.get_submitted_model_name(submission_directory)
output_directory = 'we_' + str(model_name)


# add model name to config dict
my_configs['model_name'] = str(model_name)

# get default timestep
default_timestep = file_io.get_default_timestep(submission_directory, my_configs)
my_configs['default_timestep'] = default_timestep

# intialize new westpa sim with template
file_io.initialize_tempelate(template_directory,output_directory)

# copy mcell model into template
file_io.copy_mcell_model(submission_directory,model_name,output_directory)

# move Scene.WE.mdl template into new twmplate/model directory
file_io.mv_sceWEmdl(template_directory,model_name,output_directory)

# write new files to output directory
file_io.write_new_cleanup(output_directory,my_configs)
file_io.write_new_env(output_directory,my_configs)
file_io.write_new_runseg(output_directory,my_configs)
file_io.write_new_system(output_directory,my_configs)
file_io.write_new_westcfg(output_directory,my_configs)
file_io.write_new_sceneWEmdl(output_directory,my_configs)
file_io.write_new_scenemainmdl(output_directory,my_configs)
file_io.write_new_scenerxn_outputmdl(output_directory,my_configs)
