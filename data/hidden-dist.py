#Copy this file in a new file called hidden.py and insert in the returned dict values your psql secrets.

def secrets():
    return {"host": "localhost",
            "port": 5432,
            "database": "db_name",
            "user": "postgres",
            "pass": "postgres"}