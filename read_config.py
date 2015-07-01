import yaml

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    print(section, cfg[str(section)])

python_loc = str(cfg['env']['python'])
westpa_loc = str(cfg['env']['westpa'])

obs1_name = str(cfg['model']['observable_1'])

we_iters = int(float(cfg['WE']['iters']))
we_stride = int(float(cfg['WE']['stride']))

int_pcoord = bool(cfg['WE']['bins']['int'])
min_pcoord = float(cfg['WE']['bins']['min_pcoord'])
max_pcoord = float(cfg['WE']['bins']['max_pcoord'])
bin_size = float(cfg['WE']['bins']['bin_size'])
if int_pcoord:
    min_pcoord = int(min_pcoord)
    max_pcoord = int(max_pcoord)
    bin_size = int(bin_size)

record_freq = int(float(cfg['data']['rec_freq']))
assert we_stride % record_freq == 0, "the frequency at which we record data must evenly divide the number of Mcell iterations per WE iteration (the stride setting)"

aux_data = bool(cfg['data']['log_all_species'])

vars = [python_loc,westpa_loc,obs1_name,we_iters,we_stride,min_pcoord,max_pcoord,bin_size,int_pcoord,record_freq,aux_data]

for var in vars:
    print str(var)
