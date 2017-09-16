from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug import secure_filename
import hashlib
import json
import os
import subprocess
import sys

# set python path to current folder to local folder to add ruby lib
sys.path.insert(0, os.getcwd())
from exec_ruby import *

UPLOAD_FOLDER = 'static/images/uploads'
TMP_FOLDER = 'tmp'
ALLOWED_EXTENSIONS = set(['jpg','jpeg', 'png'])

def main():
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
                return redirect(url_for('results', filename=filename))

        # if request is a get
        return render_template('index.html', title='Welcome')

    @app.route("/results/<filename>")
    def results(filename):
        out, err = ruby(filename)
        print out
        print err
        return json.dumps({"out": out, "err": err}), 200

    app.run()

if __name__ == '__main__':
    main()
