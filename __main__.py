#python test server
from flask import Flask, jsonify,request,render_template

app = Flask(__name__)

@app.route('/test/put/<string(length=2):code>', methods=['PUT'])
def test_put(code):
    #args: A MultiDict with the parsed contents of the query string. (The part in the URL after the question mark).
    #e.g: http://127.0.0.1:5000/test/put/st?number=23
    number = request.args.get('number', '3,1415')
    #in the request header (not on body)
    test = request.headers.get('test')
    #in the request for the body
    name = request.form.get('name',None)
    print('put')
    print(number)
    print(test)
    print(code)
    return jsonify({"put": 'successful'})

@app.route('/test/post', methods=['POST'])
def test_post():
    name = request.form.get('name',None)
    print(name)
    #default value 'Quappi'
    lastName = request.form.get('lastName',"Quappi")
    print(lastName)
    toReturn = {"success": True, "Hi": lastName}
    return jsonify(toReturn);

@app.route('/test/delete', methods=['DELETE'])
def test_delete():
    print('delete')
    return jsonify({"deletion": 'successful'})

@app.route('/test/get', methods=['GET'])
def test_get():
    print('get')
    return jsonify({"get": 'successful', "hi": 'mampf'})

@app.route('/test/post/template', methods=['POST'])
def test_post_template():
    name = request.form.get('name','Frederik')
    print(name)
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')