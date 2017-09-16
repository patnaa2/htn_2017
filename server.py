import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug import secure_filename
import hashlib
import io
from google.cloud import vision

UPLOAD_FOLDER = 'static/images/uploads'
TMP_FOLDER = 'tmp'
ALLOWED_EXTENSIONS = set(['jpg','jpeg', 'png'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TMP_FOLDER'] = TMP_FOLDER
# app.config['SQLALCHEMY_DATABASE_URI'] = db_connection_string
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(TMP_FOLDER):
    os.makedirs(TMP_FOLDER)
# db = SQLAlchemy(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['TMP_FOLDER'], filename))
            vision_client = vision.Client()
            with io.open(os.path.join(app.config['TMP_FOLDER'], filename), 'rb') as image_file:
                content = image_file.read()
            image = vision_client.image(content=content)

            texts = image.detect_text()

            output = texts[0].description
            # if images_table.query.filter(images_table.hash_id == hash_object).count() == 0:
            #     # Save Image
            #     copyfile(os.path.join(app.config['TMP_FOLDER'], filename), os.path.join("/home/htn/symmetrical-snuffle", app.config['UPLOAD_FOLDER'], hash_name))
            #     #Save in DB
            # os.remove(os.path.join(app.config['TMP_FOLDER'], filename))
            return redirect(url_for('results', pic_name=image_file, text=output))
    return render_template('index.html', title='Welcome')

@app.route('/results/<pic_name>/<text>')
def results(pic_name, text):
    # pic_url = url_for('static',filename='images/uploads/{}'.format(pic_name))
    # image_query = images_table.query.filter(images_table.hash_id == pic_name).first()
    # # image = Image.open("static/images/uploads/{}".format(pic_name))
    # # pixel_array = np.array(image)
    # # results = indicoio.fer(pixel_array, detect=False) 
    
    # pic_url = url_for('static',filename='images/uploads/{}'.format(image_query.url))
    # results = {'emotion_angry': image_query.emotion_angry,
    #     'emotion_sad': image_query.emotion_sad,
    #     'emotion_happy': image_query.emotion_happy,
    #     'emotion_fear': image_query.emotion_fear,
    #     'emotion_surprise': image_query.emotion_surprise,
    #     'emotion_neutral': image_query.emotion_neutral}
    # emotion_results = max(results.iteritems(), key=operator.itemgetter(1))[0]
    # emotion_results = (emotion_results, results[emotion_results])
    # more_details_link = url_for('details', pic_name = pic_name)
    return render_template("picture.html", title= "Results", image_src = pic_url, code_text=text)
