from flask import Flask ,redirect,request, render_template
import json,requests


app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/results", methods=["POST", "GET"])
def results():
	city_name = request.form['City']
	call_function = calculate(city_name)
	if len(call_function) ==2:
		city_ = call_function[1]
		current_temperature = str(call_function[0]) + ' \u00b0'+ "C"
		return render_template('index.html', city_ = city_, current_temperature = current_temperature)
	else:
		return render_template("index.html", city_ = call_function)

def calculate(city_name):
	api_key = "ENTER YOUR OWN KEY HERE"
	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name
	response = requests.get(complete_url)
	result = response.json()
	if result['cod'] != "404":
		values = result["main"] 
		x= values["temp"] -273.15
		current_temperature = round(x,2)
		city = result["name"]
		return current_temperature,city
	else:
		return "City not found, Please enter again"

if __name__ == "__main__":
	app.run()

