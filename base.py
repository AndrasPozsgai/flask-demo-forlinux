from flask import Flask
from flask_bootstrap import Bootstrap


  app = Flask(__name__)
  Bootstrap(app)

@app.route("/")
def login
  return (login.html)
  
 
 
 '''@app.route('/crash')
def main():
    raise Exception()'''
 
app.run(debug=True)
