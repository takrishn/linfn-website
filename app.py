from flask import Flask, render_template
from flask_scss import Scss
app = Flask(__name__)    
Scss(app, static_dir='static', asset_dir='assets') 

@app.route("/")                   # at the end point /
def hello():       
    return render_template('index.html')
if __name__ == "__main__":        # on running python app.py
    app.run() 