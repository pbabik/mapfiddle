#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import sqlite3

from werkzeug.utils import secure_filename

from flask import Flask, request, session, g, redirect, url_for, \
abort, render_template, make_response, send_from_directory, jsonify

from modules import mapcss_converter, json_getter, uniquefile
from vtile import cache

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'icons')
ALLOWED_EXTENSIONS = set(['gif','jpg','jpeg','svg','png'])
OSM_DATABASE = "host=localhost dbname=osm user=osm password=osm" #adjust to your configuration
#OSM_DATABASE = "__none__" or use __none__ to use the cached tiles only

def allowed_file(filename):
    """ Helper method to filter out unwanted files """
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config.from_object(__name__) 

@app.route('/')
def editor():
    """ Main HTML page """
    return render_template('index.html')

@app.route('/compile',methods=['POST'])
def compile_mapcss():
    """ Compile the MapCSS provided in POST request to JavaScript, and send it in response """
    stylecontent = request.form['css']
    stylename = request.form['name']
    compiled_style = mapcss_converter.render_js(stylename,stylecontent)
    
    if compiled_style:
        return compiled_style
    else:
        return 'alert("Malformed MapCSS")' #response gets eval()d on client side

@app.route('/download',methods=['POST'])
def send_style():
    """ Send the style - compiled or not - as an attachment """
    if request.form['format'] == 'css': #don't compile, just send file with proper headers
        response_body = request.form['css']
        response_type = 'text/css'
        response_extension = 'mapcss'
    else: #compile style to JS
        try:
            request_body = request.form['css']
            response_body = mapcss_converter.render_js(request.form['name'],request_body)
            response_type = 'text/javascript'
            response_extension = 'js'
        except:
            abort(400)
    response = make_response(response_body)
    response.headers['Content-Disposition'] = 'attachment; filename=%s.%s' % (request.form['name'], response_extension) #force the browser to download result
    return response

@app.route('/icons',methods=['GET','POST'])
def icons():
    """ Get a list of available icons or add new icon to library """
    if request.method == 'GET': #get icon list and return JSON object with the it
        return jsonify({'icons': os.listdir(app.config['UPLOAD_FOLDER'])})
    else: #POST request - handle uploaded file
        the_file = request.files.get('filedata', None)
        if the_file and allowed_file(the_file.filename):
            filename = secure_filename(the_file.filename) #clean up the file name
            fullpath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            finalname = uniquefile.add_unique_postfix(fullpath) #add unique postfix if needed
            the_file.save(finalname)
            (finalpath,finalfile) = os.path.split(finalname)          
            return jsonify({'uploaded':finalfile})
        elif not the_file:
	        return make_response(jsonify({'error': 'no file'}),400) #in case of empty request
        else:
            return make_response(jsonify({'error': 'filetype not allowed'}),403) #not an image file

@app.route('/icons/<filename>')
def icon(filename):
    """ Send a single icon """
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.route('/vtile/<z>/<x>/<y>')
def fetch_json_and_print(z,x,y):
    """ Vector tiles backend """
    tiledb = cache.VTileCache()
    the_tile = tiledb.get_tile(x,y,z) #try to fetch tile from cache
    if the_tile is not None:
        return the_tile[0] #tile already cached, return it
    elif app.config['OSM_DATABASE'] == '__none__': #if no osm2pgsql database is configured, return an empty tile
        empty_tile = 'onKothicDataResponse({"features":[],"bbox":[19.934692382812504,50.05008477836654,19.940185546875,50.05361190678807],"granularity":10000},%s,%s,%s)' % (z,x,y)
        return empty_tile
    else:
        result = json_getter.render_tile(int(z),int(x),int(y),app.config['OSM_DATABASE']) #tile not present in cache and osm2pgsql database is available - render it
        if result:
            tiledb.set_tile(x,y,z,result)
        else:
            abort(500) 
        return result
        
if __name__ == '__main__':
	app.run()
