from flask import Flask, request, jsonify, render_template
import os


# Initialize Flask App
app = Flask(__name__,static_url_path='/static')

@app.route('/',methods=['GET'])
def render_map():
    return render_template('index.html')

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)    