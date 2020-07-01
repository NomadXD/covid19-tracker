import os
from flask import Flask, request, jsonify, render_template
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
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://covid19-sl-fccae.firebaseio.com/'
})

ref = db.reference('/cases')

ref.set({
                '1':{
                    'case_no':1,
                    'detected_date':'2020-03-11',
                    'age':52,
                    'gender':'M',
                    'detected':'Homagama',
                    'detected_prefecture':'Colombo',
                    'origin':'Italy',
                    'location':{'lat':6.841273,'lng':80.003059,'value':'Homagama'},
                    'status':'Recovered'
                },
                '2':{
                    'case_no':2,
                    'detected_date':'2020-03-12',
                    'age':44,
                    'gender':'M',
                    'detected':'Mattegoda',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.813735,'lng':79.971418,'value':'Mattegoda'},
                    'status':'Hospitalized'
                },
                '3':{
                    'case_no':3,
                    'detected_date':'2020-03-13',
                    'age':41,
                    'gender':'M',
                    'detected':'Colombo 8',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.911150,'lng':79.882903,'value':'Colombo'},
                    'status':'Hospitalized'
                },
                '4':{
                    'case_no':4,
                    'detected_date':'2020-03-13',
                    'age':37,
                    'gender':'M',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },
                '5':{
                    'case_no':5,
                    'detected_date':'2020-03-13',
                    'age':43,
                    'gender':'M',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },
                '6':{
                    'case_no':6,
                    'detected_date':'2020-03-14',
                    'age':44,
                    'gender':'M',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },
                '7':{
                    'case_no':7,
                    'detected_date':'2020-03-14',
                    'age':43,
                    'gender':'M',
                    'detected':'Nattandiya',
                    'detected_prefecture':'Kurunegala',
                    'origin':'Italy',
                    'location':{'lat':7.412580, 'lng':79.858482,'value':'Nattandiya'},
                    'status':'Hospitalized'
                },
                '8':{
                    'case_no':8,
                    'detected_date':'2020-03-14',
                    'age':42,
                    'gender':'M',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },
                '9':{
                    'case_no':9,
                    'detected_date':'2020-03-14',
                    'age':56,
                    'gender':'F',
                    'detected':'Dukandawa',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':7.421020,'lng':79.909765,'value':'Dukannawa'},
                    'status':'Hospitalized'
                },
                '10':{
                    'case_no':10,
                    'detected_date':'2020-03-14',
                    'age':17,
                    'gender':'F',
                    'detected':'Mattegoda',
                    'detected_prefecture':'Colombo',
                    'origin':'Italy',
                    'location':{'lat':6.813735,'lng':79.971418,'value':'Mattegoda'},
                    'status':'Hospitalized'
                },
                '11':{
                    'case_no':11,
                    'detected_date':'2020-03-15',
                    'gender':'M',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },
                '12':{
                    'case_no':12,
                    'detected_date':'2020-03-15',
                    'gender':'M',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },
                '13':{
                    'case_no':13,
                    'detected_date':'2020-03-15',
                    'gender':'M',
                    'detected':'Galkanda',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':7.868494, 'lng':81.066752,'value':'Galkanda'},
                    'status':'Hospitalized'
                },
                '14':{
                    'case_no':14,
                    'detected_date':'2020-03-15',
                    'gender':'M',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },
                '15':{
                    'case_no':15,
                    'detected_date':'2020-03-15',
                    'gender':'M',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },
                '16':{
                    'case_no':16,
                    'detected_date':'2020-03-15',
                    'gender':'M',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },
                '17':{
                    'case_no':17,
                    'detected_date':'2020-03-15',
                    'gender':'M',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },
                '18':{
                    'case_no':18,
                    'detected_date':'2020-03-16',
                    'age':13,
                    'gender':'F',
                    'detected':'Mattegoda',
                    'detected_prefecture':'Colombo',
                    'origin':'Italy',
                    'location':{'lat':6.813735,'lng':79.971418,'value':'Mattegoda'},
                    'status':'Hospitalized'
                },
                '19':{
                    'case_no':19,
                    'detected_date':'2020-03-16',
                    'age':73,
                    'gender':'M',
                    'detected':'Galle',
                    'detected_prefecture':'Galle',
                    'origin':'Italy',
                    'location':{'lat':6.053475,'lng':80.221015,'value':'Galle'},
                    'status':'Hospitalized'
                },
                 '20':{
                    'case_no':20,
                    'detected_date':'2020-03-16',
                    'detected':'Akuregoda',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.893832,'lng':79.948567,'value':'Akuregoda'},
                    'status':'Hospitalized'
                },
                 '21':{
                    'case_no':21,
                    'detected_date':'2020-03-16',
                    'detected':'Colombo 8',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.911150,'lng':79.882903,'value':'Colombo'},
                    'status':'Hospitalized'
                },
                '22':{
                    'case_no':22,
                    'detected_date':'2020-03-16',
                    'detected':'Colombo',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.911150,'lng':79.882903,'value':'Colombo'},
                    'status':'Hospitalized'
                },
                  '23':{
                    'case_no':23,
                    'detected_date':'2020-03-16',
                    'detected':'Colombo',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.911150,'lng':79.882903,'value':'Colombo'},
                    'status':'Hospitalized'
                },
                  '24':{
                    'case_no':24,
                    'detected_date':'2020-03-16',
                    'detected':'Colombo',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.911150,'lng':79.882903,'value':'Colombo'},
                    'status':'Hospitalized'
                },
                  '25':{
                    'case_no':25,
                    'detected_date':'2020-03-16',
                    'detected':'Colombo',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.911150,'lng':79.882903,'value':'Colombo'},
                    'status':'Hospitalized'
                },
                  '26':{
                    'case_no':26,
                    'detected_date':'2020-03-16',
                    'detected':'Colombo',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.911150,'lng':79.882903,'value':'Colombo'},
                    'status':'Hospitalized'
                },
                  '27':{
                    'case_no':27,
                    'detected_date':'2020-03-16',
                    'detected':'Colombo',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.911150,'lng':79.882903,'value':'Colombo'},
                    'status':'Hospitalized'
                },
                  '28':{
                    'case_no':28,
                    'detected_date':'2020-03-17',
                    'detected':'Colombo',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.911150,'lng':79.882903,'value':'Colombo'},
                    'status':'Hospitalized'
                },
                  '29':{
                    'case_no':29,
                    'detected_date':'2020-03-17',
                    'detected':'Colombo',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.911150,'lng':79.882903,'value':'Colombo'},
                    'status':'Hospitalized'
                },
                  '30':{
                    'case_no':30,
                    'age':25,
                    'gender':'M',
                    'detected_date':'2020-03-17',
                    'detected':'Udugampola',
                    'detected_prefecture':'Kandy',
                    'location':{'lat':7.147248,'lng':79.975937,'value':'Udugampola'},
                    'status':'Hospitalized'
                },
                '31':{
                    'case_no':31,
                    'detected_date':'2020-03-17',
                    'detected':'Marawila',
                    'detected_prefecture':'Puttalam',
                    'location':{'lat':7.423878,'lng':79.833783,'value':'Marawila'},
                    'status':'Hospitalized'
                },
                '32':{
                    'case_no':32,
                    'detected_date':'2020-03-17',
                    'detected':'Kelaniya',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.971273,'lng':79.922417,'value':'Kelaniya'},
                    'status':'Hospitalized'
                },
                '33':{
                    'case_no':33,
                    'detected_date':'2020-03-17',
                    'gender':'F',
                    'detected':'Mattegoda',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.813735,'lng':79.971418,'value':'Mattegoda'},
                    'status':'Hospitalized'
                },
                    '34':{
                    'case_no':34,
                    'detected_date':'2020-03-17',
                    'detected':'Colombo',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.911150,'lng':79.882903,'value':'Colombo'},
                    'status':'Hospitalized'
                },
                    '35':{
                    'case_no':35,
                    'detected_date':'2020-03-17',
                    'age':61,
                    'gender':'M',
                    'detected':'Batticaloa',
                    'detected_prefecture':'Batticaloa',
                    'location':{'lat':7.732414,'lng':81.677159,'value':'Batticaloa'},
                    'status':'Hospitalized'
                },
                     '36':{
                    'case_no':36,
                    'detected_date':'2020-03-17',
                    'detected':'Colombo',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.911150,'lng':79.882903,'value':'Colombo'},
                    'status':'Hospitalized'
                },
                     '37':{
                    'case_no':37,
                    'detected_date':'2020-03-17',
                    'detected':'Rathnapura',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.705519,'lng':80.382497,'value':'Rathnapura'},
                    'status':'Hospitalized'
                },
                    '38':{
                    'case_no':38,
                    'detected_date':'2020-03-17',
                    'detected':'Vavuniya',
                    'detected_prefecture':'Polonnaruwa',
                    'location':{'lat':8.755686,'lng':80.500628,'value':'Vavuniya'},
                    'status':'Hospitalized'
                },
                '39':{
                    'case_no':39,
                    'detected_date':'2020-03-17',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },
                '40':{
                    'case_no':40,
                    'detected_date':'2020-03-17',
                    'detected':'Nelumdeniya',
                    'detected_prefecture':'Kegalle',
                    'location':{'lat':7.231052,'lng':80.259888,'value':'Nelumdeniya'},
                    'status':'Hospitalized'
                },
                '41':{
                    'case_no':41,
                    'detected_date':'2020-03-17',
                    'detected':'Kalutara',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.586083,'lng':79.964385,'value':'Kalutara'},
                    'status':'Hospitalized'
                },
                '42':{
                    'case_no':42,
                    'detected_date':'2020-03-17',
                    'detected':'Kelaniya',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.971414,'lng':79.922343,'value':'Kelaniya'},
                    'status':'Hospitalized'
                },
                '43':{
                    'case_no':43,
                    'detected_date':'2020-03-18',
                    'detected':'Waikkala',
                    'detected_prefecture':'Negombo',
                    'location':{'lat':7.289340,'lng':79.857438,'value':'Waikkal'},
                    'status':'Hospitalized'
                },
                '44':{
                    'case_no':44,
                    'detected_date':'2020-03-18',
                    'detected':'Waikkala',
                    'detected_prefecture':'Negombo',
                    'location':{'lat':7.289340,'lng':79.857438,'value':'Waikkal'},
                    'status':'Hospitalized'
                },
                '45':{
                    'case_no':45,
                    'detected_date':'2020-03-18',
                    'detected':'Piliyandala',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.802388,'lng':79.922061,'value':'Piliyandala'},
                    'status':'Hospitalized'
                },
                 '46':{
                    'case_no':46,
                    'detected_date':'2020-03-18',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },
                 '47':{
                    'case_no':47,
                    'detected_date':'2020-03-18',
                    'detected':'Bandaragama',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.714960,'lng':79.990692,'value':'Bandaragama'},
                    'status':'Hospitalized'
                },
                '48':{
                    'case_no':48,
                    'detected_date':'2020-03-18',
                    'detected':'Beruwala',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.473002,'lng':79.992778,'value':'Beruwala'},
                    'status':'Hospitalized'
                },
                '49':{
                    'case_no':49,
                    'detected_date':'2020-03-18',
                    'detected':'Malabe',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.906024,'lng':79.964745,'value':'Malabe'},
                    'status':'Hospitalized'
                },
                '50':{
                    'case_no':50,
                    'detected_date':'2020-03-18',
                    'detected':'Mt. Lavinia',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.831131,'lng':79.882035,'value':'Mt.Lavinia'},
                    'status':'Hospitalized'
                },
                '51':{
                    'case_no':51,
                    'detected_date':'2020-03-18',
                    'detected':'Rathmalana',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.819752,'lng':79.881138,'value':'Rathmalana'},
                    'status':'Hospitalized'
                },
                '52':{
                    'case_no':52,
                    'detected_date':'2020-03-18',
                    'detected':'Wattala',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.990957,'lng':79.893991,'value':'Wattala'},
                    'status':'Hospitalized'
                },
                '53':{
                    'case_no':53,
                    'detected_date':'2020-03-19',
                    'detected':'Ja -ela',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':7.066844,'lng':79.904020,'value':'Ja -ela'},
                    'status':'Hospitalized'
                },
                 '54':{
                    'case_no':54,
                    'detected_date':'2020-03-19',
                    'detected':'Rathmalana',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.819752,'lng':79.881138,'value':'Rathmalana'},
                    'status':'Hospitalized'
                },
                 '55':{
                    'case_no':55,
                    'detected_date':'2020-03-19',
                    'detected':'Rathnapura',
                    'gender':'F',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.705519,'lng':80.382497,'value':'Rathnapura'},
                    'status':'Hospitalized'
                },
                '56':{
                    'case_no':56,
                    'detected_date':'2020-03-19',
                    'detected':'Rathnapura',
                    'gender':'F',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.705519,'lng':80.382497,'value':'Rathnapura'},
                    'status':'Hospitalized'
                },
                '57':{
                    'case_no':57,
                    'detected_date':'2020-03-19',
                    'detected':'Waikkala',
                    'detected_prefecture':'Negombo',
                    'location':{'lat':7.289340,'lng':79.857438,'value':'Waikkal'},
                    'status':'Hospitalized'
                },
                  '58':{
                    'case_no':58,
                    'detected_date':'2020-03-19',
                    'detected':'Ja -ela',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':7.066844,'lng':79.904020,'value':'Ja -ela'},
                    'status':'Hospitalized'
                },
                  '59':{
                    'case_no':59,
                    'detected_date':'2020-03-19',
                    'detected':'Ja -ela',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':7.066844,'lng':79.904020,'value':'Ja -ela'},
                    'status':'Hospitalized'
                },
                '60':{
                    'case_no':60,
                    'detected_date':'2020-03-19',
                    'detected':'Bandarawela',
                    'detected_prefecture':'Badulla',
                    'origin':'Italy',
                    'location':{'lat':6.825805,'lng':80.999532,'value':'Bandarawela'},
                    'status':'Hospitalized'
                },
                   '61':{
                    'case_no':61,
                    'detected_date':'2020-03-20',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },
                   '62':{
                    'case_no':62,
                    'detected_date':'2020-03-20',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },
                 '63':{
                    'case_no':63,
                    'detected_date':'2020-03-20',
                    'detected':'Waikkala',
                    'detected_prefecture':'Negombo',
                    'location':{'lat':7.289340,'lng':79.857438,'value':'Waikkal'},
                    'status':'Hospitalized'
                },
                    '64':{
                    'case_no':64,
                    'detected_date':'2020-03-20',
                    'detected':'Ja -ela',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':7.066844,'lng':79.904020,'value':'Ja -ela'},
                    'status':'Hospitalized'
                },
                    '65':{
                    'case_no':65,
                    'detected_date':'2020-03-20',
                    'detected':'Ja -ela',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':7.066844,'lng':79.904020,'value':'Ja -ela'},
                    'status':'Hospitalized'
                },
                 '66':{
                    'case_no':66,
                    'detected_date':'2020-03-20',
                    'detected':'Colombo 8',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.911150,'lng':79.882903,'value':'Colombo'},
                    'status':'Hospitalized'
                },
                   '67':{
                    'case_no':67,
                    'detected_date':'2020-03-20',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },
                   '68':{
                    'case_no':68,
                    'detected_date':'2020-03-20',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },   '69':{
                    'case_no':69,
                    'detected_date':'2020-03-20',
                    'detected':'Kandakadu',
                    'detected_prefecture':'Polonnaruwa',
                    'origin':'Italy',
                    'location':{'lat':8.087345,'lng': 81.177059,'value':'Kandakadu'},
                    'status':'Hospitalized'
                },
                  '70':{
                    'case_no':70,
                    'detected_date':'2020-03-20',
                    'detected':'Niwisapura',
                    'detected_prefecture':'Gampaha',
                    'location':{'lat':7.112116,'lng':79.896765,'value':'Niwisapura'},
                    'status':'Hospitalized'
                },
                  '71':{
                    'case_no':71,
                    'detected_date':'2020-03-20',
                    'detected':'Panadura',
                    'detected_prefecture':'Kalutara',
                    'location':{'lat':6.710452, 'lng':79.906776,'value':'Panadura'},
                    'status':'Hospitalized'
                },
                '72':{
                    'case_no':72,
                    'detected_date':'2020-03-20',
                    'detected':'Colombo 8',
                    'detected_prefecture':'Colombo',
                    'location':{'lat':6.911150,'lng':79.882903,'value':'Colombo'},
                    'status':'Hospitalized'
                },


                











                

            })