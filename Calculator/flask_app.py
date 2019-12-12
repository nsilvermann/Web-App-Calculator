
#Created by Nathan Silverman for Sezzle
#On 12/11/2019
from flask import Flask, request, render_template, url_for, jsonify

#Intiates Global list to track the ten most recent calculations
oldCalculations= [0] * 10
app = Flask(__name__,
            static_url_path='/static', 
            static_folder='static')
app.config["DEBUG"] = True

#Redirects you the proper page
@app.route('/')
def hello_world():
    return 'Hello please add /api/calc to the end of your URL'

#Loads calculator.html 
@app.route("/api/calc", methods=["POST","GET"])
def calc():
    return render_template('calculator.html')

# Updates the log in real time
@app.route("/api/log", methods=["POST","GET"])
def storeList():
    global oldCalculations
    #recieveing the sent calculation
    update= request.get_json()
    print("update: ",update)
    #makes new calculation the first element in list 
    oldCalculations[:0]= [update]
    #removes oldest element
    oldCalculations.pop()
    print("oldCalculations: ",oldCalculations)
    #returns the updated list 
    return jsonify(oldCalculations)

# Populates the log with the 10 most recent calculations when a page first loads up
@app.route("/api/clog", methods=["POST","GET"])
def returnList():
    global oldCalculations
    print("oldCalculations: ",oldCalculations)
    return jsonify(oldCalculations)

if __name__ == '__main__':
    app.run(host="localhost", port=5500, debug=True)


