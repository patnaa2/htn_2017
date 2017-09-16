import json
import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug import secure_filename
import hashlib

UPLOAD_FOLDER = 'static/images/uploads'
TMP_FOLDER = 'tmp'
ALLOWED_EXTENSIONS = set(['jpg','jpeg', 'png'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TMP_FOLDER'] = TMP_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(TMP_FOLDER):
    os.makedirs(TMP_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['TMP_FOLDER'], filename))
            return json.dumps({"val": "it works"}), 200

    return render_template('index.html', title='Welcome')

app.run()
