# read yaml config file and import settings as python dictionary
# convert types (sometimes gratuitously) as a safety measure

import yaml

def import_config(filename):
    with open(filename, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    # env vars
    cfg['env']['python'] = str(cfg['env']['python'])
    cfg['env']['westpa'] = str(cfg['env']['westpa'])

    # model vars
    cfg['model']['observable_1'] = str(cfg['model']['observable_1'])

    # WE vars
    cfg['WE']['iters'] = int(float(cfg['WE']['iters']))
    cfg['WE']['stride'] = int(float(cfg['WE']['stride']))

    # WE:bin vars
    cfg['WE']['bins']['int'] = bool(cfg['WE']['bins']['int'])
    cfg['WE']['bins']['min_pcoord'] = float(cfg['WE']['bins']['min_pcoord'])
    cfg['WE']['bins']['max_pcoord'] = float(cfg['WE']['bins']['max_pcoord'])
    cfg['WE']['bins']['bin_size'] = float(cfg['WE']['bins']['bin_size'])
    if cfg['WE']['bins']['int']:
        cfg['WE']['bins']['min_pcoord'] = int(cfg['WE']['bins']['min_pcoord'])
        cfg['WE']['bins']['max_pcoord'] = int(cfg['WE']['bins']['max_pcoord'])
        cfg['WE']['bins']['bin_size'] = int(cfg['WE']['bins']['bin_size'])

    # data vars
    cfg['data']['log_all_species'] = bool(cfg['data']['log_all_species'])
    cfg['data']['rec_freq'] = int(float(cfg['data']['rec_freq']))
    assert cfg['WE']['stride'] % cfg['data']['rec_freq'] == 0, "the frequency at which we record data must evenly divide the number of Mcell iterations per WE iteration (we_stride)"

    return cfg

# test the function
my_configs = import_config("config.yaml")
for item in my_configs.items():
    print item

with open('out_data.yml', 'w') as outfile:
    outfile.write( yaml.dump(my_configs,default_flow_style=False) )
