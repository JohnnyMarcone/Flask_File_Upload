from app.app import app
from app import photos, docs
from flask import request, render_template


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        print(request.files)
        filename = photos.save(request.files['photo'])  # ['photo'] refers to the name attribute in the template input
        return filename
    if request.method == 'POST' and 'doc' in request.files:
        print(request.files)
        filename = docs.save(request.files['doc'])  # ['doc'] refers to the name attribute in the template input
        return filename
    return render_template('upload.html')


@app.route('/serve', methods=['GET'])
def serve():
    return 'here is your file'
