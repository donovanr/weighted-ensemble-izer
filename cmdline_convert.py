# python script to take an mcell simulation that was exported from cellblender
# and output a ready-to-go WESTPA simulation, according to a single parameter file

from __future__ import print_function

import sys, os, shutil, fileinput

import yaml
import weightedensemblizer.convert as weconvert

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--configfile', required=True)
parser.add_argument('-m', '--modeldirectory', required=True)
args = parser.parse_args()


modeldirectory = os.path.abspath(os.path.realpath(args.modeldirectory))
configfile = os.path.abspath(os.path.realpath(args.configfile))

# call main weighted ensemblizer function with args parsed from cmd line input
weconvert.main(configfile,modeldirectory)
