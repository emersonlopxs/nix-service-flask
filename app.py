from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_capsules():
  response = requests.get('https://api.spacexdata.com/v4/capsules')
  return response.content


if __name__ == '__main__':
  app.run(debug=True)