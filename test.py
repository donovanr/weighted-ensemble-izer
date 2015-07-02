#test the import config function
my_configs = read_config.import_config("config.yaml")
for item in my_configs.items():
   print item

# test writing out a yaml file
with open('out_data.yml', 'w') as outfile:
   outfile.write( yaml.dump(my_configs,default_flow_style=False) )
