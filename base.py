from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap


  app = Flask(__name__)
  Bootstrap(app)

@app.route("/")
def login
  return (login.html)
  
 
 
 '''@app.route('/crash')
def main():
    raise Exception()'''


if __name__ == '__main__':
app.run(debug=True)
