from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
import json
app = Flask(__name__)




    

@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not found", 404
    else:
        return render_template('jobpage.html', job=job)

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return json.dumps(jobs, default=str)

@app.route("/api/job/<id>")
def show_job_json(id):
    job = load_job_from_db(id)
    return jsonify(job)

@app.route("/job/<id>/apply", methods = ['POST'])
def apply_to_job(id):
    job = load_job_from_db(id)
    data = request.form
    add_application_to_db(id, data)
    return render_template('application_submitted.html', application = data, job=job)




if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)