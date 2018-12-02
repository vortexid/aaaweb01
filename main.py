import psycopg2
from  flask import Flask
app = Flask(__name__)

conn = psycopg2.connect(host="localhost",database="student1",user="student1",password="student1")
sql_prihod = """INSERT INTO prihodi (konto, komitent, naziv, iznos) VALUES (%s, %s, %s, %s);"""
title="Student1";

@app.route('/<name>')
def pay(name):
    cur = conn.cursor()
    cur.execute(sql_prihod, ("7020",name,"Web prihodi", 10.0,));
    conn.commit()
    return "<h1>"+title+"</h1></br>Hvala "+name+" !"

@app.route("/")
def home():
    return "<h1>"+title+"</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')
