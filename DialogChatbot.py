from flask import Flask,request,jsonify
import json
import requests
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


app=Flask(__name__)

@app.route('/api',methods=['POST'])
def Get_Data():
    if request.method=='POST':
        data=json.loads(request.data)
        url = "https://motivational-quotes1.p.rapidapi.com/motivation"
        headers = {
            'content-type': "application/json",
            'x-rapidapi-host': "motivational-quotes1.p.rapidapi.com",
            'x-rapidapi-key': "a18e3fac81mshebe52b1274e2648p176074jsn2cdb75cd9456"}
        response = requests.request("POST", url, data=data, headers=headers,verify=False)
        return jsonify({"fulfillment":response.text})

if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
