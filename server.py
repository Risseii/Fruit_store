#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)  

app.secret_key = "llave super secreta" #Establecemos una clave secreta

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    
    session['cantidad'] = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    session['datos_completos'] = request.form['first_name'] +" "+ request.form['last_name']
    session['strawberry'] = int(request.form['strawberry'])
    session['raspberry'] = int(request.form['raspberry'])
    session['apple'] = int(request.form['apple'])
    # cantidad = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    # first_name = request.form['first_name']

    return render_template("checkout.html")  #cantidad = cantidad,first_name = first_name
    

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    