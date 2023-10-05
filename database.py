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