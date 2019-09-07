from flask import Flask
from flask_uploads import UploadSet, configure_uploads, IMAGES, DOCUMENTS
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# flask upload initialization
photos = UploadSet('photos', IMAGES)
docs = UploadSet('docs', DOCUMENTS)
myAppAttachments = UploadSet('myAppAttachments', DOCUMENTS)  # example showing you can name these for a specific app
configure_uploads(app, (photos, docs, myAppAttachments))

from app.routes import index, file_upload
