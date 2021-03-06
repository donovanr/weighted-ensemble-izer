from __future__ import print_function

import os, shutil, fileinput

import numpy
import yaml
import read_config
import file_io


# get default timestep
def get_default_timestep(configs):
    this_file = 'Scene.main.mdl'
    this_path = os.path.join(configs['model_dir'],this_file)

    with open(this_path) as f:
        for line in f:
            if line.startswith('TIME_STEP =') or line.startswith('TIME_STEP='):
                deflt_timestep = float(line.split('=')[-1])
    return deflt_timestep


# intialize new westpa sim with template
def initialize_template(template_dir,output_dir):
    # delete previous copy of output_simulation
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
def copy_mcell_model(mod_dir,out_dir):
    shutil.copytree(os.path.join(mod_dir),os.path.join(out_dir,'bstates',os.path.basename(mod_dir)))

# move Scene.WE.mdl template into model folder
def mv_sceWEmdl(mod_name,out_dir):
    this_file = 'Scene.WE.mdl'
    shutil.move(os.path.join(out_dir,'bstates',this_file),os.path.join(out_dir,'bstates',mod_name,this_file))

# generic function to replace placeholder term in template file name with real term
def replace_all(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=True):
        print(line.replace(searchExp, replaceExp), end='')


# hard-coded into westpa_template
template_names = {}
template_names['model_name'] = 'template_model_dir_name'
template_names['west_python'] = 'template_west_python'
template_names['west_root'] = 'template_west_root'
template_names['observable_name'] = 'template_observable_name'
template_names['record_frequency'] = 'template_record_frequency'
template_names['bin_bounds'] = 'template_bin_bounds'
template_names['we_iters'] = 'template_we_iters'
template_names['we_stride'] = 'template_we_stride'
template_names['timestep'] = 'template_timestep'
template_names['bin_bounds'] = 'template_bin_bounds'
template_names['bin_target_count'] = 'template_bin_target_count'

# write new cleanup.sh
def write_new_cleanup(out_dir,configs):
    this_file = 'cleanup.sh'
    this_path = os.path.join(out_dir,this_file)
    replace_all(this_path,template_names['model_name'],configs['model_name'])

# write new env.sh
def write_new_env(out_dir,configs):
    this_file = 'env.sh'
    this_path = os.path.join(out_dir,this_file)
    replace_all(this_path,template_names['west_python'],configs['env']['python'])
    replace_all(this_path,template_names['west_root'],configs['env']['westpa'])

# write new runseg.sh
def write_new_runseg(out_dir,configs):
    this_file = 'runseg.sh'
    this_path = os.path.join(out_dir,this_file)
    replace_all(this_path,template_names['model_name'],configs['model_name'])
    replace_all(this_path,template_names['observable_name'],configs['model']['observable_1'])

# write new system.py
def write_new_system(out_dir,configs):
    this_file = 'system.py'
    this_path = os.path.join(out_dir,this_file)
    replace_all(this_path,template_names['record_frequency'],str(configs['data']['rec_freq']))
    replace_all(this_path,template_names['bin_target_count'],str(configs['WE']['bins']['target_count']))

    bin_min = configs['WE']['bins']['min_pcoord']
    bin_max = configs['WE']['bins']['max_pcoord']
    bin_step = configs['WE']['bins']['bin_size']
    new_bins = 'list(numpy.linspace({0} + {2}/2.0,{1} - {2}/2.0, ({1} - {0})/{2}))'.format(bin_min,bin_max,bin_step)
    replace_all(this_path,template_names['bin_bounds'],new_bins)


# write new west.cfg
def write_new_westcfg(out_dir,configs):
    this_file = 'west.cfg'
    this_path = os.path.join(out_dir,this_file)
    replace_all(this_path,template_names['we_iters'],str(configs['WE']['iters']))

# write new Scene.WE.mdl
def write_new_sceneWEmdl(out_dir,configs):
    this_file = 'Scene.WE.mdl'
    this_path = os.path.join(out_dir,'bstates',configs['model_name'],this_file)
    replace_all(this_path,template_names['we_iters'],str(configs['WE']['iters']))
    replace_all(this_path,template_names['we_stride'],str(configs['WE']['stride']))
    replace_all(this_path,template_names['record_frequency'],str(configs['data']['rec_freq']))
    replace_all(this_path,template_names['timestep'],str(configs['default_timestep']))


# write new Scene.WE.mdl
def write_new_scenemainmdl(out_dir,configs):
    this_file = 'Scene.main.mdl'
    this_path = os.path.join(out_dir,'bstates',configs['model_name'],this_file)

    for linenum,line in enumerate(fileinput.input(this_path, inplace=True)):
        if linenum==0:
            print('INCLUDE_FILE = "Scene.WE.mdl"')
            print(line, end='')
        elif line.startswith('ITERATIONS =') or line.startswith('ITERATIONS='):
            print('ITERATIONS = iterations')
        elif line.startswith('TIME_STEP =') or line.startswith('TIME_STEP='):
            print('TIME_STEP = timestep')
        else:
            print(line, end='')

# write new Scene.rxn_output.mdl
def write_new_scenerxn_outputmdl(out_dir,configs):
    this_file = 'Scene.rxn_output.mdl'
    this_path = os.path.join(out_dir,'bstates',configs['model_name'],this_file)
    for line in fileinput.input(this_path, inplace=True):
        if line.startswith('  STEP=') or line.startswith(' STEP=') or line.startswith('STEP=') or line.startswith('  STEP =') or line.startswith(' STEP =') or line.startswith('STEP ='):
            print('  STEP=record_freq')
        else:
            print(line.replace('/seed_" & seed & "',''), end='')
