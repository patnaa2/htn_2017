from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug import secure_filename
import hashlib
import json
import os
import subprocess
import sys

prod = False

# set python path to current folder to local folder to add ruby lib
sys.path.insert(0, os.getcwd())
from exec_ruby import *

if prod:
    from google_vision_api import GoogleVisionClient

UPLOAD_FOLDER = 'static/images/uploads'
TMP_FOLDER = 'tmp'
RUBY_FILE = 'ruby_tmp.rb'
ALLOWED_EXTENSIONS = set(['jpg','jpeg', 'png'])

def main():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['TMP_FOLDER'] = TMP_FOLDER

    # global variable for google client
    if prod:
        gvc = GoogleVisionClient()
    else:
        gvc = None

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
                filename = secure_filename('current')
                f.save(os.path.join(app.config['TMP_FOLDER'], filename))
                return redirect(url_for('results', filename=filename))

        # if request is a get
        return render_template('index.html', title='Welcome')

    @app.route("/results/<filename>")
    def results(filename):
        # process text first
        filename = os.path.join(app.config['TMP_FOLDER'], filename)
        text = gvc.get_text(filename)
        ruby_f = os.path.join(app.config['TMP_FOLDER'], RUBY_FILE)

        with open(ruby_f, 'w') as f:
            f.write(text)

        out, err = ruby(ruby_f)
        print out
        print err
        return json.dumps({"out": out, "err": err}), 200

    app.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    main()
