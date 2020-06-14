from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import pr
import json
from ALPRwithSuperResolution_master import projectcode

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index.html')
def index1():
    return render_template("index.html")


@app.route('/members.html')
def member():
    return render_template("members.html")


@app.route('/members_company.html')
def member_company():
    return render_template("members_company.html")


@app.route('/members_professor.html')
def member_professor():
    return render_template("members_professor.html")


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/about_Detec.html')
def about_d():
    return render_template("about_Detec.html")


@app.route('/about_OCR.html')
def about_ocr():
    return render_template("about_OCR.html")


@app.route('/about_SR.html')
def about_Sr():
    return render_template("about_SR.html")


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('/Users/leejeongjin/Desktop/test/ALPRwithSuperResolution_master/data/dataset' + secure_filename(f.filename))
    return render_template('index.html', result=pr.text())


@app.route('/process/image', methods=['POST'])
def image_processing():
    if request.method == 'POST':
        f = request.files['file']
        f.save('/Users/leejeongjin/Desktop/test/ALPRwithSuperResolution_master/data/dataset' + secure_filename(f.filename))
        result = projectcode.text()
        return json.dumps(result)


if __name__ == '__main__':
    app.run(debug=True)
