from flask import Flask, render_template, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxy', methods=['POST'])
def proxy():
    try:
        url = request.json.get('url')
        headers = request.json.get('headers')
        body = request.json.get('body')
        response = requests.post(url, headers=headers, json=body)
        return Response(response.text, status=response.status_code, content_type=response.headers['Content-Type'])
    except Exception as e:
        return Response(str(e), status=500)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)