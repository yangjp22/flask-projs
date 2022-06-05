from flask import Flask, make_response, request, render_template
import settings

app = Flask(__name__)
# app.config['ENV'] = 'development'
# app.config['DEBUG'] = True
print(app.config)
app.config.from_object(settings)
print(app.config)

@app.route('/')
def index():
    return 'hello world yang'

def hello():
    return 'hello world'
app.add_url_rule('/hello', view_func=hello)

data = {'a': 'Beijing', 'b': 'Shenzhen', 'c': 'Nanjing'}
@app.route('/getcity/<string:city>')
def find(city):
    return data.get(city, 'None')

@app.route('/path/<p>/link')
def path(p):
    return p

@app.route('/response')
def res():

    response = make_response('hello world')
    response.headers['myheader'] = '123'
    return response


@app.route('/request')
def req():
    print(request.url)
    print(request.full_path)
    print(request.headers)
    return 'hello request'


@app.route('/register2')
def register2():
    print(request.args)
    return 'hello register2'

def ownFilter(value):
    if type(value) == str:        
        return value
    elif type(value) == int:
        return value + 3
    else:
        return 'hello'

app.add_template_filter(ownFilter, 'ownfilter')

@app.route('/register')
def register():
    name = 'fredyang'
    names = ['汤姆', '杰克', '西蒙斯', '肯德基', '琳达', 3, 4, 5]
    return render_template('register.html', name=name, names=names)

if __name__ == '__main__':
    app.run()