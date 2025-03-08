from flask import Flask 
app = Flask(__name__)
@app.route('/')
def personal_details():
    return 'Hello,World!'

@app.route('/name')
def get_name():
    return 'Rahul'
@app.route('/regno')
def get_regno():
    return '22IT035'
@app.route('/department')
def get_dept():
    return 'Information Technology'
if __name__ == '_main_':
    app.run(debug=True)
