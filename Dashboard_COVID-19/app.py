# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
import json
import py2neo
from py2neo import Graph
# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('login.html')  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template	
	
# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/covid_kg')
def covid_kg():
    return render_template('covid_kg.html')  # render a template	

@app.route('/regionwise_Knowledge')
def regionwise_Knowledge():
	graph = Graph("bolt://localhost:7687", auth=("neo4j", "123"))
	query = """
	MATCH (n:Location) WHERE n.Region= "China" RETURN n
	"""
	region_info = graph.run(query).to_data_frame() 
	return render_template('regionwise_Knowledge.html', tables=[region_info.to_html(classes='Location')]) 

@app.route('/recovery_status')
def recovery_status():
	graph = Graph("bolt://localhost:7687", auth=("neo4j", "123"))
	query = """
	MATCH (n:Location) WHERE n.Region= "China" RETURN n.Recovered
	"""
	region_info = graph.run(query).to_data_frame() 
	return render_template('recovery_status.html', tables=[region_info.to_html(classes='Location')]) 

@app.route('/provinceandregion_status')
def provinceandregion_status():
	graph = Graph("bolt://localhost:7687", auth=("neo4j", "123"))
	query = """
	MATCH (n:Location) WHERE n.Region= "China" AND n.Province= "Hubei" RETURN n
	"""
	region_info = graph.run(query).to_data_frame() 
	return render_template('provinceandregion_status.html', tables=[region_info.to_html(classes='Location')]) 

@app.route('/provinceandregion_status_date')
def provinceandregion_status_date():
	graph = Graph("bolt://localhost:7687", auth=("neo4j", "123"))
	query = """
	MATCH (n:Location) WHERE n.Region= "China" AND n.Province= "Hubei" AND n.Last_Update= "2020-03-11T10:53:02"  RETURN n
	"""
	region_info = graph.run(query).to_data_frame() 
	return render_template('provinceandregion_status_date.html', tables=[region_info.to_html(classes='Location')]) 

@app.route('/test_Status_region')
def test_Status_region():
	graph = Graph("bolt://localhost:7687", auth=("neo4j", "123"))
	query = """
	MATCH (n:Location) WHERE n.Region= "Pakistan" AND n.Province= "Sindh" RETURN n.Total_tests_performed
	"""
	region_info = graph.run(query).to_data_frame() 
	return render_template('test_Status_region.html', tables=[region_info.to_html(classes='Location')]) 
@app.route('/patient_admit_status')
def patient_admit_status():
	graph = Graph("bolt://localhost:7687", auth=("neo4j", "123"))
	query = """
	MATCH (n:Location) WHERE n.Region= "Pakistan" AND n.Province= "Sindh" AND n.date = "20-Mar-20" RETURN n.Still_admit
	"""
	region_info = graph.run(query).to_data_frame() 
	return render_template('patient_admit_status.html', tables=[region_info.to_html(classes='Location')]) 
# start the server with the 'run()' method
if __name__ == '__main__':
	app.run(debug=True)