from flask import Flask, render_template, request, jsonfy
from flask_bootstrap import Bootstrap, template_folder="templates"


  app = Flask(__name__)
  Bootstrap(app)

@app.route("/")
def login
  return render_template (login.html)
  
 
 
 '''@app.route('/crash')
def main():
    raise Exception()'''


if __name__ == '__main__':
app.run(debug=True)
