from __future__ import print_function

import sys, os, subprocess, shutil, tempfile, fileinput

import yaml
import read_config
import file_io

# get submitted model name
def get_submitted_model_name(submit_directory):
    mod_name_list = os.listdir(submit_directory)
    assert len(mod_name_list) == 1, "too many directories submitted"
    mod_name = mod_name_list[0]
    return mod_name


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


# copy mcell model into template
def copy_mcell_model(submit_dir,mod_name,out_dir):
    shutil.copytree(os.path.join(submit_dir,mod_name),os.path.join(out_dir,'bstates',mod_name))

# move Scene.WE.mdl template into model folder
def mv_sceWEmdl(template_dir,mod_name,out_dir):
    this_file = 'Scene.WE.mdl'
    shutil.move(os.path.join(out_dir,'bstates',this_file),os.path.join(out_dir,'bstates',mod_name,this_file))

# replace placeholder term in template file name with real term
def replace_all(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=True):
        print(line.replace(searchExp, replaceExp), end='')


# hard-coded into template
# TODO: turn these into a dict
template_model_name = 'template_model_dir_name'
template_west_python = 'template_west_python'
template_west_root = 'template_west_root'
template_observable_name = 'template_observable_name'
template_record_frequency = 'template_record_frequency'
template_bin_bounds = 'template_bin_bounds'
template_we_iters = 'template_we_iters'
template_we_stride = 'template_we_stride'


# TODO: pass config params as dict and parse out needed params in each function

# write new cleanup.sh
def write_new_cleanup(out_dir,mod_name):
    this_file = 'cleanup.sh'
    replace_all(os.path.join(out_dir,this_file),template_model_name,mod_name)

# write new env.sh
def write_new_env(out_dir,west_python,west_root):
    this_file = 'env.sh'
    replace_all(os.path.join(out_dir,this_file),template_west_python,west_python)
    replace_all(os.path.join(out_dir,this_file),template_west_root,west_root)

# write new runseg.sh
def write_new_runseg(out_dir,mod_name,obs_name):
    this_file = 'runseg.sh'
    replace_all(os.path.join(out_dir,this_file),template_model_name,mod_name)
    replace_all(os.path.join(out_dir,this_file),template_observable_name,obs_name)

# write new system.py
def write_new_system(out_dir,rec_freq):
    this_file = 'system.py'
    replace_all(os.path.join(out_dir,this_file),template_record_frequency,str(rec_freq))
# TODO: edit bin info in system.py

# write new west.cfg
def write_new_westcfg(out_dir,we_iters):
    this_file = 'west.cfg'
    replace_all(os.path.join(out_dir,this_file),template_we_iters,str(we_iters))

# write new Scene.WE.mdl
def write_new_sceneWEmdl(out_dir,mod_name,we_iters,we_stride,rec_freq):
    this_file = 'Scene.WE.mdl'
    replace_all(os.path.join(out_dir,'bstates',mod_name,this_file),template_we_iters,str(we_iters))
    replace_all(os.path.join(out_dir,'bstates',mod_name,this_file),template_we_stride,str(we_stride))
    replace_all(os.path.join(out_dir,'bstates',mod_name,this_file),template_record_frequency,str(rec_freq))
