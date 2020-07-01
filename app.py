from flask import Flask, request, jsonify, render_template
import os
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app,db


import numpy as np
import pandas as pd
import folium
import webbrowser
import os
import math

from h3 import h3
from folium import Map



# Initialize Flask App
app = Flask(__name__,static_url_path='/static')

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://covid19-sl-fccae.firebaseio.com/'
})



@app.route('/',methods=['GET'])
def render_map():
    data = read_data()
    time = data['time']
    total = data['total']
    cases = data['cases']
    provinces = data['provinces']
    last_update = data['meta']['last_update']
    total.pop(0)
    time.pop(0)
    cases.pop(0)
    provinces.pop(0)
    summary = data['summary']
    return render_template('index.html',time=time,summary=summary,total=total,cases=cases,last_update=last_update,provinces=provinces)

def read():
    ref = db.reference('cases')
    arr = jsonify(ref.get())
    return ref.get()

def read_data():
    ref = db.reference('/')
    arr = jsonify(ref.get())
    return ref.get()



def lat_lng_to_h3(lat,lng,level):
    return h3.geo_to_h3(lat,lng,level)


@app.route('/generate5',methods=['GET'])
def generate_map_5():
    map = folium.Map(
    tiles='https://api.mapbox.com/v4/mapbox.streets/{z}/{x}/{y}.png?access_token=pk.eyJ1Ijoibm9tYWR4ZCIsImEiOiJjazd4bzA5dXcwMWdiM2ZtcWJ5ZXN0cHRvIn0.dwYVqMpGEfsmrqZ8JThQ5A',max_bounds=True,min_lat=4.811839,max_lat=10.012130,max_lon=82.596596,min_lon=79.169890,min_zoom=7,zoom_start=7,
    attr= '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors © <a href="http://cartodb.com/attributions#basemaps">CartoDB</a>')
    # map = Map(tiles="cartodbpositron", 
    #       attr= '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors © <a href="http://cartodb.com/attributions#basemaps">CartoDB</a>')
    max_lat = 9.725300
    min_lat = 5.993070
    max_lon = 81.897583
    min_lon = 79.861244
    map.fit_bounds([[min_lat, min_lon], [max_lat, max_lon]])
    latlng = read()
    latlng = list(latlng)
    latlng.pop(0)
    print(latlng)
    
    h3Arr = []
    for co_ordinate in latlng:
        co_ordinate['h3'] =  lat_lng_to_h3(co_ordinate['location']['lat'],co_ordinate['location']['lng'],6)
        h3Arr.append(co_ordinate)

    clusters = dict()

    for row in h3Arr:
        key = row['h3']
        if key in clusters:
            clusters[key]['count'] += 1
        else:
            clusters[key] = {"count": 1,
                         "geom": h3.h3_to_geo_boundary(h3_address=key),"name":row['location']['value']}

    for cluster in clusters.values():
        points = cluster['geom']
        # points = [p[::-1] for p in points]
        tooltip = "{0} cases | {1}".format(cluster['count'],cluster['name'])
        if(cluster['count']>10):
             polygon = folium.vector_layers.Polygon(locations=points, tooltip=tooltip,
                                               fill=True, 
                                               color='#ff0000', 
                                               fill_color='#ff0000', 
                                               fill_opacity=0.8, weight=3, opacity=0.8)
        elif (cluster['count']>5):
             polygon = folium.vector_layers.Polygon(locations=points, tooltip=tooltip,
                                               fill=True, 
                                               color='#ff0000', 
                                               fill_color='#ff0000', 
                                               fill_opacity=0.5, weight=3, opacity=0.5)
        else:
            polygon = folium.vector_layers.Polygon(locations=points, tooltip=tooltip,
                                               fill=True, 
                                               color='#ff0000', 
                                               fill_color='#ff0000', 
                                               fill_opacity=0.3, weight=3, opacity=0.3)

        
        
        polygon.add_to(map)
    map.save("./static/html/map.html")


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port, debug=True)    