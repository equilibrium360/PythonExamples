import yaml
with open('resources/conf.yml', 'r') as f:
    doc = yaml.load(f)
txt = doc["treeroot"]["branch1"]
print(txt)