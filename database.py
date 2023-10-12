from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
load_dotenv()

db_connection = os.getenv('DB_CONNECTION')

engine = create_engine(db_connection, connect_args={
    "ssl":{
        "ssl_ca": "/etc/ssl/cert.pem"
  }
})

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        result_all = result.all()
        jobs = []
        for row in result_all:
            jobs.append(row._mapping)
        return jobs
def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text(f"SELECT * FROM jobs WHERE id = {id}")
        )
        rows = result.all()
        if len(rows) ==0:
            return None
        else:
            return dict(rows[0]._mapping)

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
        conn.execute(query, {"job_id":job_id, "full_name":data['full_name'], "email":data['email'], "linkedin_url":data['linkedin_url'], "education":data['education'], "work_experience":data['work_experience'], "resume_url":data['resume_url'] })
        
                     

# if __name__=="__main__":
#     print(add_application_to_db(1))