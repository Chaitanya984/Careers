from flask import Flask,render_template,jsonify
from flask.json import load
from database import load_jobs_from_db

app = Flask(__name__)

# JOBS = [
# {
#     'id': 1,
#     'title': 'Data Analyst',
#     'location': 'Bengaluru, India',
#     'salary': 'Rs. 10,00,000'
# },
# {    
#     'id': 2,
#    'title': 'Data Engineer',
#    'location': 'Hyderabad, India',
#    'salary': 'Rs. 15,00,000'
# },
# {    
#     'id': 3,
#    'title': 'Software Engineer',
#    'location': 'Remote, India',
#    'salary': 'Rs. 15,00,000'
# },
# {    
#     'id': 4,
#    'title': 'Frontend Engineer',
#    'location': 'San Franscisco,USA',
#    'salary': '$15,00,000'
# }
# ]

@app.route("/")
def hello_world():
    JOBS = load_jobs_from_db()   
    return render_template('home.html',jobs = JOBS,company_name= 'Jovian Careers')


@app.route("/api/jobs")
def list_jobs(): 
    JOBS = load_jobs_from_db()   
    return jsonify(JOBS)


    
if(__name__) == '__main__':
  app.run(host='0.0.0.0', debug = True)