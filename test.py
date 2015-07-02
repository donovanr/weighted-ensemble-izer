from __future__ import print_function

import sys, os, subprocess, shutil, tempfile, fileinput

import yaml
import read_config
import file_io

#test the import config function
my_configs = read_config.import_config("config.yaml")
#for item in my_configs.items():
#   print item

# test writing out a yaml file
#with open('out_data.yml', 'w') as outfile:
#   outfile.write( yaml.dump(my_configs,default_flow_style=False) )



dirpath = tempfile.mkdtemp()
with open(dirpath + '/out_data.yml', 'w') as outfile:
   outfile.write( yaml.dump(my_configs,default_flow_style=False) )

my_cmd = 'cat {0}/out_data.yml'.format(dirpath)
os.system(my_cmd)
shutil.rmtree('/path/to/folder')
