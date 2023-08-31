from flask import Flask, render_template, request

app = Flask(__name__)

users_database = {
    "ekow" : "ekow1",
    "sackey" : "sackey1",
    "edem" : "edem1",
    "user" : "user1"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authorize', methods=['GET', 'POST'])
def authorize():
    
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username in users_database.keys():
        if users_database[username] == password:
            return render_template('landingPage.html')
        else:
            return render_template('errorPage.html')
        

@app.route('/logout')
def logout():
    return render_template('index.html')
    

@app.route('/whereami')
def whereami():
    return 'Ghana!'

def deco(func):
    def wrap():
        bold = func()
        return f"<b>{bold}</b>"
    return wrap

@app.route('/greeting')
@deco
def helloworld():
    return "<p>Hello world. Hello!</p>"

@app.route('/greeting/<name>/<age>')
def print_name():
    return "i am here."
def helloperson(name: str, age: int):
    return f"Hello {age} year old, {name}. How are you doing today?"
    

print(__name__)

if __name__ == '__main__':
    app.run(debug= True, host= '0.0.0.0')