import yaml

with open("example_config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    print(section, cfg[str(section)])
