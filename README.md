# weighted-ensemble-izer
script for converting a CellBlender/MCell model into a weighted ensemble simulation, ready for use with WESTPA

## How to use
in the weighted-ensemble-izer directory, or anywhere if you put the weightedensembleizer module in your `$PYTHONPATH`

`python cmdline_convert.py -c config.yaml -m some_mcell_model`

- the `-c` or `--configfile` option sets the configuration file, where you specified the WE parameters
- the `-m` or `--modeldirectory` option sets the directory containing your MCell model

