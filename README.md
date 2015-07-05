# weighted-ensemble-izer
script for getting an MCell simulation ready for WESTPA

## How to use
in the weighted-ensemble-izer directory, or anywhere if you put the weightedensembleizer module in your `$PYTHONPATH`

`python cmdline_convert.py -c config.yaml -m some_mcell_model`

- the `-c` or `--configfile` option set the configuration file, wher eyou can set all the WE parameters
- the `-m` or `--modeldirectory` option sets the directory containing your mcell model

TODO: double check quotes around all bash variables everywhere in my sh files
