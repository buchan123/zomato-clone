from flask import render_template,Flask, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/restaurant')
def restaurant():
    return render_template('restaurant.html')
                        
if __name__ == '__main__':
    app.run()
