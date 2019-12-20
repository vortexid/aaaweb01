#-*- coding: utf-8 -*-
import psycopg2
import datetime
import time
from  flask import Flask, render_template, url_for
app = Flask(__name__)

conn = psycopg2.connect(host="localhost",database="student1",user="student1",password="student1")
sql_prihod = """INSERT INTO prihodi (konto, komitent, naziv, iznos) VALUES (%s, %s, %s, %s);"""
title="Autorizacija i autentifikacija";
price=5.0

@app.route('/kupi/<name>')
def pay(name):    
    cur = conn.cursor()
    cur.execute(sql_prihod, ("7020",name,"Prihodi od web stranice", price,));
    conn.commit()
    ts = time.time()
    print datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S') + " "+name+" je uplatio "+str(price)+" Kn" 
    return render_template("index.html", naziv=title, cijena=price, name=name, mod=0 ) 

@app.route("/")
def home():
    return render_template("index.html", naziv=title, cijena=price, mod=1 ) 

@app.route("/cijena/<cijena>")
def set_price(cijena):
    global price
    price=cijena
    return "<p>Promijenili ste cijenu u "+cijena+" Kn.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')
