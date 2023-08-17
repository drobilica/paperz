import os,time
from app import app, rss_model, rservice
from flask import render_template, flash, redirect, url_for, request, jsonify
import random # get this out of this



app.url_map.strict_slashes = False

@app.route('/')
@app.route('/index')
def index():
    entries = rss_model.load_live_news()
    return render_template(
        'live.html.j2',
        entries = entries
        )
@app.route('/404')
def not_found():
    return render_template(
        '404.html.j2',
        )

@app.route('/explore/')
@app.route('/explore/<source>')
def explore(source=None):
    # airiq = rservice.load_airiq()
    # weather= rservice.load_weather()
    yaml_keys = rss_model.get_news()
    
    if source == None:
        random_news = yaml_keys[random.randint(0,len(yaml_keys)-1)]
        rss_model.check_file_cache(random_news)
        return redirect(f"/explore/{random_news}", code=302)        
    elif source in yaml_keys:
        rss_model.check_file_cache(source)
        entries = rss_model.load_news_cache(source)
    else:
        return redirect(f"/404", code=302)        
    airiq = rservice.load_airiq()
    weather = rservice.load_weather()
    return render_template(
        'csv_list.html.j2',
        entries = entries,
        airiq = airiq,
        weather = weather,
        get_news_list = rss_model.get_news()
        )

@app.route('/live')
def live():
    entries = rss_model.load_live_news()
    return render_template(
        'live.html.j2',
        entries = entries
        )

### API starts here ###

@app.route('/api/cache')
@app.route('/api/cache/<source>')
def cache(source=None):
    if source == None:
        cache_resp = rss_model.get_news()
    else: #add an elsif if key not found in     yaml_keys = list(out['news'].keys())
        cache = rss_model.make_cache(source)
        cache_resp = f'cache made for {source}'
    return jsonify(cache_resp)

@app.route('/api/generate_cache')
def generate_cache():
    msg = rss_model.populate_news()
    return jsonify(msg)


@app.route('/api/get_cache_info')
def get_cache_info():
    directory = 'data/'
    file_list = []
    for i in os.listdir(directory):
        a = os.stat(os.path.join(directory,i))
        file_list.append([i,time.ctime(a.st_atime)]) #[file,most_recent_access,created]
    return jsonify(file_list)
