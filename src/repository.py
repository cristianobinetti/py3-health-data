import psycopg2
import time
import hidden

# load the secrets
secrets = hidden.secrets()


# log function
def log(log_str):
    print('\n' + secrets['database'] + '=#', log_str)
    time.sleep(0.5)


# db connection
conn = psycopg2.connect(host=secrets['host'],
                        port=secrets['port'],
                        database=secrets['database'],
                        user=secrets['user'],
                        password=secrets['pass'],
                        connect_timeout=3)
cur = conn.cursor()

#"""
# <!> DROP TABLE TO TEST <!>
log('DROP TABLE')

sql = 'DROP TABLE IF EXISTS gender CASCADE;'
print(sql)
cur.execute(sql)

sql = 'DROP TABLE IF EXISTS occupation CASCADE;'
print(sql)
cur.execute(sql)

sql = 'DROP TABLE IF EXISTS bmi_category CASCADE;'
print(sql)
cur.execute(sql)

sql = 'DROP TABLE IF EXISTS sleep_disorder CASCADE;'
print(sql)
cur.execute(sql)

sql = 'DROP TABLE IF EXISTS person CASCADE;'
print(sql)
cur.execute(sql)
# <!> DROP TABLE TO TEST <!>
#"""

# CREATE TABLE
log('CREATE TABLE')

# create gender table
sql = '''
CREATE TABLE IF NOT EXISTS gender
(id SERIAL PRIMARY KEY, gender VARCHAR(8) UNIQUE NOT NULL, count INTEGER NOT NULL);'''
print(sql)
cur.execute(sql)

# create occupation table
sql = '''
CREATE TABLE IF NOT EXISTS occupation
(id SERIAL PRIMARY KEY, occupation VARCHAR(32) UNIQUE NOT NULL, count INTEGER NOT NULL);'''
print(sql)
cur.execute(sql)

# create bmi_category table
sql = '''
CREATE TABLE IF NOT EXISTS bmi_category
(id SERIAL PRIMARY KEY, bmi_category VARCHAR(32) UNIQUE NOT NULL, count INTEGER NOT NULL);'''
print(sql)
cur.execute(sql)

# create sleep_disorder
sql = '''
CREATE TABLE IF NOT EXISTS sleep_disorder
(id SERIAL PRIMARY KEY, sleep_disorder VARCHAR(32) UNIQUE NOT NULL, count INTEGER NOT NULL);'''
print(sql)
cur.execute(sql)

# create person table
sql = '''
CREATE TABLE IF NOT EXISTS person
(id SERIAL PRIMARY KEY,
gender_id INTEGER NOT NULL,
age INTEGER NOT NULL CHECK (age > 0),
occupation_id INTEGER NOT NULL,
sleep_duration DECIMAL NOT NULL CHECK (sleep_duration > 0),
quality_of_sleep INTEGER NOT NULL CHECK (quality_of_sleep > 0),
physical_activity_level INTEGER NULL CHECK (physical_activity_level > 0),
stress_level INTEGER NULL CHECK (stress_level > 0),
bmi_category_id INTEGER NOT NULL,
blood_pressure VARCHAR(8),
hearth_rate INTEGER NULL CHECK (hearth_rate > 0),
daily_steps INTEGER NULL CHECK (daily_steps > 0),
sleep_disorder_id INTEGER NOT NULL,

FOREIGN KEY(gender_id) REFERENCES gender(id),
FOREIGN KEY(occupation_id) REFERENCES occupation(id),
FOREIGN KEY(bmi_category_id) REFERENCES bmi_category(id),
FOREIGN KEY(sleep_disorder_id) REFERENCES sleep_disorder(id));'''
print(sql)
cur.execute(sql)

# commit create table
conn.commit()


# SELECT QUERY
def select_fk_category(query, *args):
    cur.execute(query, args)
    conn.commit()

    result = cur.fetchone()[0]
    #print('SELECT category:', args[0], 'FK:', result)
    return result


# INSERT QUERY
def insert_category(query, *args):
    print('INSERT category:', args[0])
    cur.execute(query, args)
    conn.commit()


def insert_person(args):
    params = tuple(args)
    query = '''
        INSERT INTO person
        (gender_id, age, occupation_id,
        sleep_duration, quality_of_sleep, physical_activity_level,
        stress_level, bmi_category_id, blood_pressure,
        hearth_rate, daily_steps, sleep_disorder_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;'''
    cur.execute(query, params)
    conn.commit()

    person_id = cur.fetchone()[0]
    print('INSERT person', person_id, (params[0], params[2], params[7], params[11]))


# UPDATE QUERY
def update_category(query, *args):
    print('UPDATE category:', args[1], 'count:', args[0])
    cur.execute(query, args)
    conn.commit()


# UTILITY
def get_connection():
    return cur, conn

def check_query(limit):
    time.sleep(1)
    print('\nCHECK JOIN QUERY:')
    sql = '''SELECT p.id, g.gender, o.occupation, b.bmi_category, s.sleep_disorder
    FROM person as p JOIN gender as g ON p.gender_id = g.id
    JOIN occupation as o ON p.occupation_id = o.id
    JOIN bmi_category as b ON p.bmi_category_id = b.id
    JOIN sleep_disorder as s ON p.sleep_disorder_id = s.id
    ORDER BY p.id LIMIT %s;'''
    print(sql % limit)
    cur.execute(sql, (limit,))

    print('RESULT:')
    result = cur.fetchall()
    for row in result:
        print(row)
