

from flask import Flask,request,jsonify,render_template
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def loadPage():
	return render_template('index.html', query="")

@app.route("/api/submit", methods = ['POST'])
def submit():
    item_identifier = request.form["item_identifier"]
    item_weight = request.form["item_weight"]
    item_fat_content = request.form["item_fat_content"]
    item_visibility = request.form["item_visibility"]
    item_type = request.form["item_type"]
    item_mrp = request.form["item_mrp"]
    outlet_identifier = request.form["outlet_identifier"]
    outlet_establishment_year = request.form["outlet_establishment_year"]
    outlet_size = request.form["outlet_size"]
    outlet_location_type = request.form["outlet_location_type"]
    outlet_type = request.form["outlet_type"]
   
   data = np.
    
    print("Received data:", data)
    response = {
        "status": "success",
        "received_data": data,
        "message": "Data processed successfully!"
    }
    return jsonify(response)

    

    
# output = 'recevied'
# return render_template('index.html', output1 = output)

if __name__ == '__main__':
    app.run(port= 3000,debug=True)