from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    num=request.json
    result=num['first']+num['second']
    return jsonify({'result':result})
    

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    num=request.json
    result=num['first']-num['second']
    return jsonify({'result':result})

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
