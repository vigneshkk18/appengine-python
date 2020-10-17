from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello This is a sample example of Google App Engine</h1>'
    
if __name__ == '__main__':
    app.run(port=8080,threaded=True)