from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/get", methods=['GET'])
def get():
    for arg in request.args:
        print('Key: ' + arg)
        print('Value: ' + request.args.get(arg))
    return "GET"

@app.route("/post", methods=['POST'])
def post():
    for body in request.form:
        print('Key: ' + body)
        print('Value: ' + request.form.get(body))
    for file_name in request.files:
        print('Key: ' + file_name)
        file = request.files.get(file_name)
        f = open('../images/' + file_name + '.jpg', 'wb+')
        f.write(file.read())
        f.close()
    return "POST"

@app.route('/param/<name>', methods=['GET'])
def param(name):
    print(name)
    return "PARAM"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")