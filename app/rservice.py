import requests
import yaml
from time import time


def check_cache(source):
    out = load_cache()
    start_time = out['cache'][source]['mtime']
    end_time = time()
    if not start_time:
        start_time = 1
    seconds_elapsed = end_time - start_time

    if round(seconds_elapsed) > 1000 or start_time == None or load_cache_value(source) == None:
        start_time = time()
        make_cache(source, 'mtime', start_time)  
        return False
    else:
        return True

    print(round(seconds_elapsed))


def load_cache():
    f=open("conf/service-cache.yaml", 'r')
    out = yaml.load(f, Loader=yaml.Loader)
    f.close()
    return out


def make_cache(source, source_type, value):
    out = load_cache()
    out['cache'][source][source_type] = value
    writer=open('conf/service-cache.yaml','w')    
    yaml.dump(out, writer)
    writer.close()


def load_cache_value(source):
    with open("conf/service-cache.yaml", 'r') as stream:
        out = yaml.load(stream, Loader=yaml.Loader)
    value = out['cache'][source]['value']
    return value 


def load_airiq():
    if check_cache('airiq'):
        print('loading airiq cache')
        return load_cache_value('airiq')
    else:
        print('loading airiq because 600 secs have passed')
        endpoint = "https://api.airvisual.com/v2/city?city=Belgrade&state=central-serbia&country=serbia&key=a21a8af4-4e8e-4566-a53f-06abdbe4f254"
        r = requests.get(endpoint)    
        content = r.json()
        make_cache('airiq', 'value', content['data']['current']['pollution']['aqius'])
        return load_cache_value('airiq')


def load_weather():
    if check_cache('weather'):
        print('loading weather cache')
        return load_cache_value('weather')
    else:
        endpoint = "https://api.openweathermap.org/data/2.5/weather?id=792680&appid=d7672273f293e18bae7860fce2a5feed"
        r = requests.get(endpoint)    
        content = r.json()
        temp = content['main']['temp'] - 273.15
        make_cache('weather', 'value', round(temp))
        print('loading weather because 16 secs have passed')
        return load_cache_value('weather')
