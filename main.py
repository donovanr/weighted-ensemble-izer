import yaml
import read_config

import os, subprocess, shutil, tempfile


mypath = 'a_new_dir'
try:
    os.makedirs(mypath)
except OSError:
    if not os.path.isdir(mypath):
        raise
