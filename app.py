from flask import Flask, render_template, redirect
import os

app = Flask(__name__)

# Load configuration from environment variable or use default value
config_page = os.environ.get('CONFIG_PAGE', '/default')

@app.route('/')
def index():
    return render_template('index.html', config_page=config_page)

@app.route('/redirect')
def redirect_page():
    return redirect(config_page)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)