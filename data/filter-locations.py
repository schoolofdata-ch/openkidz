import re

with open('locations.csv') as f:
    content = f.readlines()

r = re.compile('.+\<b>(.+?)\</b\>')

with open('locations-only.csv', 'w') as rfile:
    for l in content:
        line = l.strip()
        match = r.match(line)
        if match:
            name = match.groups()[0].replace('""', '"')
            lat, lng = line.split(',')[-2:]
            l = '%s,%s,%s\n' % (name, lat, lng)
            rfile.write(l)
