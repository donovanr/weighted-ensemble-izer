# python script to take an mcell simulation that was exported from cellblender
# and output a ready-to-go WESTPA simulation, according to a single parameter file

from __future__ import print_function

import sys, os, subprocess, shutil, tempfile, fileinput

import yaml
import read_config
import file_io


config_file = 'config.yaml'
submission_directory = 'a_submission'
template_directory = 'westpa_template'
output_directory = 'output_simulation'


# read in config file
my_configs = read_config.import_config(config_file)

# get submitted model name
model_name = file_io.get_submitted_model_name(submission_directory)

# intialize new westpa sim with template
file_io.initialize_tempelate(template_directory,output_directory)

# copy mcell model into template
file_io.copy_mcell_model(submission_directory,model_name,output_directory)

# move Scene.WE.mdl template into new twmplate/model directory
file_io.mv_sceWEmdl(template_directory,model_name,output_directory)

# write new cleanup.sh
file_io.write_new_cleanup(output_directory,model_name)

# write new env.sh
file_io.write_new_env(output_directory,my_configs['env']['python'],my_configs['env']['westpa'])

# write new runseg.sh
file_io.write_new_runseg(output_directory,model_name,my_configs['model']['observable_1'])

# write new system.py
file_io.write_new_system(output_directory,my_configs['data']['rec_freq'])

# write new west.cfg
file_io.write_new_westcfg(output_directory,my_configs['WE']['iters'])

# write new Scene.WE.mdl
file_io.write_new_sceneWEmdl(output_directory,model_name,my_configs['WE']['iters'],my_configs['WE']['stride'],my_configs['data']['rec_freq'])
