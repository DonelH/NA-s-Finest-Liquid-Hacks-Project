from flask import Flask, render_template, request
import boto3 
from boto3.dynamodb.conditions import Key, Attr

app = Flask(__name__)


dynamodb = boto3.resource('dynamodb',aws_access_key_id='AKIA5Z3XPAZ2CNF5IF5Q', 
                           aws_secret_access_key='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', 
                           region_name='us-east-1')

@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/signup', methods=['post'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        table = dynamodb.Table('userdata')
        
        table.put_item(
                Item={
        'name': name,
        'email': email,
        'password': password
            }
        )
        msg = "Registration Complete. Please Login to your account !"
    
        return render_template('login.html',msg = msg)
    return render_template('index.html')

@app.route('/check',methods = ['post'])
def check():
    if request.method=='POST':
        
        email = request.form['email']
        password = request.form['password']
        
        table = dynamodb.Table('userdata')
        response = table.query(
                KeyConditionExpression=Key('email').eq(email)
        )
        items = response['Items']
        name = items[0]['name']
        print(items[0]['password'])
        if password == items[0]['password']:
            
            return render_template("splash.html",name = name)
    return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True)
