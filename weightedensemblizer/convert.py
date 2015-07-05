# python script to take an mcell simulation that was exported from cellblender
# and output a ready-to-go WESTPA simulation, according to a single parameter file

from __future__ import print_function

import sys, os, shutil, fileinput

import yaml
import read_config
import file_io

def main(config_file,model_dir):

    # the dir this script is in
    # __file is where *this* file lives__
    we_script_dir = os.path.dirname(os.path.realpath(__file__))

    # abs path of model dir gets passed, grab just the dir name
    model_name = os.path.basename(model_dir)

    # set output directory name based on input model directory, but keep abs path
    # sys.argv[0] is where the parent script is called from
    output_directory = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'we_'+str(model_name))

    # template directory should never change
    template_directory = os.path.join(we_script_dir,'westpa_template')

    # read in config file
    my_configs = read_config.import_config(config_file)
    # add model name and model dir to config dict
    my_configs['model_dir'] = str(model_dir)
    my_configs['model_name'] = str(model_name)

    # get default timestep
    default_timestep = file_io.get_default_timestep(my_configs)
    my_configs['default_timestep'] = default_timestep

    # intialize new westpa sim with template
    file_io.initialize_template(template_directory,output_directory)

    # copy mcell model into template
    file_io.copy_mcell_model(model_name,output_directory)

    # move Scene.WE.mdl template into new template/model directory
    file_io.mv_sceWEmdl(model_name,output_directory)

    # write new files to output directory
    file_io.write_new_cleanup(output_directory,my_configs)
    file_io.write_new_env(output_directory,my_configs)
    file_io.write_new_runseg(output_directory,my_configs)
    file_io.write_new_system(output_directory,my_configs)
    file_io.write_new_westcfg(output_directory,my_configs)
    file_io.write_new_sceneWEmdl(output_directory,my_configs)
    file_io.write_new_scenemainmdl(output_directory,my_configs)
    file_io.write_new_scenerxn_outputmdl(output_directory,my_configs)
