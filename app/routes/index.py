from app.app import app


@app.route('/')
@app.route('/index')
def index():
    return 'Welcome to the Index'
