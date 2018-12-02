#-*- coding: utf-8 -*-
import psycopg2
from  flask import Flask, render_template, url_for
app = Flask(__name__)

conn = psycopg2.connect(host="localhost",database="student1",user="student1",password="student1")
sql_prihod = """INSERT INTO prihodi (konto, komitent, naziv, iznos) VALUES (%s, %s, %s, %s);"""
title="Autorizacija i autentifikacija";
price=5.0

@app.route('/<name>')
def pay(name):
    cur = conn.cursor()
    cur.execute(sql_prihod, ("7020",name,"Prihodi od web stranice", price,));
    conn.commit()
    return "Test"

@app.route("/")
def home():
    return render_template("index.html", naziv=title, cijena=price, ) 

@app.route("/cijena/<cijena>")
def set_price(cijena):
    global price
    price=cijena
    return "<p>Promijenili ste cijenu u "+cijena+" Kn.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')
