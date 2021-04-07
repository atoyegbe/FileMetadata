import os 
import filetype
from flask import Flask, render_template, request, url_for, abort, json, redirect
from werkzeug.utils import secure_filename 
app = Flask(__name__, template_folder='templates')
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.docx', '.jpg', '.doc', '.pdf', '.png', '.txt']
app.config['UPLOAD_PATH'] = 'uploads'


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def upload_file():
    f = request.files['file']
    f_name = secure_filename(f.filename)
    file_details = {}
    if f_name != '':
        file_ext = os.path.splitext(f_name)[1]
        if file_ext in app.config['UPLOAD_EXTENSIONS']:
            # f.save(f.filename)
            file_details['name'] = os.path.splitext(f.filename)[0]
            file_details['size'] = os.path.getsize(f.filename)
            file_details['type'] = filetype.guess(f.filename).mime 
            print(file_details)
        return json.dumps(file_details)
    return redirect(url_for('home.html'))  

if __name__ == "__main__":
    app.run(debug=True)
