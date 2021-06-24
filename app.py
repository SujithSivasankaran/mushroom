from flask import Flask,render_template,request
import requests,json,urllib
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/', methods=['POST','GET'])
def predict():
    features_names = [x for x in request.form.keys()]
    features = [x for x in request.form.values()]
    n = {}
    for i in range(0, len(features_names)):
        n[features_names[i]] = features[i]
    l = [n]
    data = {'data' : l}
    body = str.encode(json.dumps(data))
    headers = {'Content-Type': 'application/json'}
    service = 'http://e9eb91f9-f735-4d50-a452-9261e1dc6b51.centralus.azurecontainer.io/score'
    resp = requests.post(service, body, headers=headers)
    print(resp.text[17])
    if (resp.text[17] == 'e'):
        out = ' not poisonous'
    elif (resp.text[17] == 'p'):
        out = ' poisonous'
    return render_template('index.html', output= out)

    # return render_template('index.html',prediction_text=' {}'.format(out))

if __name__ == "__main__":
    app.run()

