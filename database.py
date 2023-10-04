from sqlalchemy import create_engine, text

db_connection = "mysql+pymysql://l7zu6ywom0jetnv24pg1:pscale_pw_3wevcL4CeQ683PV5JbxVVWa4zdLg2qFOUIZMf9UavP5@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"

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