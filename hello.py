# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return "Hey there!"
# if __name__ == '__main__':
#     app.run(debug=True)

import LicenseNumberDetect as lnd
import os.path
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
  #return 'Server Works!'
  return jsonify({'name': 'alice', 'email': 'alice@outlook.com'})
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'

@app.route('/detect', methods=['GET'])
def detect_plate():
    file_src = request.args.get('src')
    print(file_src)

    print(os.path.isfile(file_src))
    print(os.path.exists(file_src))

    licenseNumber = lnd.detect_license_number(file_src)
    print(licenseNumber)



    return jsonify({'success': 'true', 'licenseNumber': licenseNumber})

    # with open('/tmp/data.txt', 'r') as f:
    #     data = f.read()
    #     records = json.loads(data)
    #     for record in records:
    #         if record['name'] == name:
    #             return jsonify(record)
        # return jsonify({'error': 'data not found'})

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/', methods=['POST'])
# @app.route('/', methods=['DELETE'])
# @app.route('/', methods=['PUT'])