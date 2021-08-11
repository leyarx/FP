import json
import base64
import urllib.request


def get_png(link):
    contents = urllib.request.urlopen(link).read().decode()
    data = json.loads(contents[14:-1].replace('\n', ' '))
    url = data['meta']['thumbnail2d']['small']
    filename = url[url.rfind("/")+1:]  
    keys = data.keys()

    if 'under' in keys:
        with open(filename.replace(".png", "(under).png"), 'wb') as output_file:
            output_file.write(base64.b64decode(data['under'][22:]))

    if 'over' in keys:
        with open(filename.replace(".png", "(over).png"), 'wb') as output_file:
            output_file.write(base64.b64decode(data['over'][22:]))
            
    if 'color' in keys:
        with open(filename.replace(".png", "(color).png"), 'wb') as output_file:
            output_file.write(base64.b64decode(data['color'][22:]))


#get_png('https://d273csydae9vpp.cloudfront.net/assets/img_2ds/417/jsonp/Bed_Queensize.jsonp')

with open('in.txt') as fp:
    for line in fp:
        get_png(line.replace('thumb', 'jsonp').replace('.png', '.jsonp'))
