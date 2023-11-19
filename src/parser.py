from src import repository as repo
from src import utility as util

record_count = 0

gender_dict = dict()
occupation_dict = dict()
bmi_dict = dict()
sleep_disorder_dict = dict()

# reading .csv file
with open('../data/sleep_health.csv') as file:
    lines = file.readlines()
    # skip the first line --> header
    lines.pop(0)

    for line in lines:
        line = line.split(',')
        '''
        line[0] = id
        line[1] = gender
        line[2] = age
        line[3] = occupation
        line[4] = sleep duration
        line[5] = quality of sleep
        line[6] = physical activity level
        line[7] = stress level
        line[8] = bmi category
        line[9] = blood pressure
        line[10] = hearth rate
        line[11] = daily steps
        line[12] = sleep disorder
        '''

        # stripping elements in line
        for i in range(len(line)):
            line[i] = line[i].strip()

        # cleaning data
        if line[8] == 'Normal':
            line[8] += ' Weight'

        # counting category occurrences
        gender_dict[line[1]] = gender_dict.get(line[1], 0) + 1
        if gender_dict.get(line[1], 0) == 1:
            repo.insert_category('INSERT INTO gender (gender, count) VALUES (%s, %s)', line[1], 1)

        occupation_dict[line[3]] = occupation_dict.get(line[3], 0) + 1
        if occupation_dict.get(line[3], 0) == 1:
            repo.insert_category('INSERT INTO occupation (occupation, count) VALUES (%s, %s)', line[3], 1)

        bmi_dict[line[8]] = bmi_dict.get(line[8], 0) + 1
        if bmi_dict.get(line[8], 0) == 1:
            repo.insert_category('INSERT INTO bmi (bmi, count) VALUES (%s, %s)', line[8], 1)

        sleep_disorder_dict[line[12]] = sleep_disorder_dict.get(line[12], 0) + 1
        if sleep_disorder_dict.get(line[12], 0) == 1:
            repo.insert_category('INSERT INTO sleep_disorder (sleep_disorder, count) VALUES (%s, %s)', line[12], 1)

        # fetching category id
        line[1] = repo.select_fk_category('SELECT id FROM gender WHERE gender = %s', line[1])
        line[3] = repo.select_fk_category('SELECT id FROM occupation WHERE occupation = %s', line[3])
        line[8] = repo.select_fk_category('SELECT id FROM bmi WHERE bmi = %s', line[8])
        line[12] = repo.select_fk_category('SELECT id FROM sleep_disorder WHERE sleep_disorder = %s', line[12])

        # insert person record
        line.pop(0)
        repo.insert_person(line)
        record_count += 1

# update category count
for cat, count in gender_dict.items():
    repo.update_category('UPDATE gender SET count = %s WHERE gender = %s', count, cat)

for cat, count in occupation_dict.items():
    repo.update_category('UPDATE occupation SET count = %s WHERE occupation = %s', count, cat)

for cat, count in bmi_dict.items():
    repo.update_category('UPDATE bmi SET count = %s WHERE bmi = %s', count, cat)

for cat, count in sleep_disorder_dict.items():
    repo.update_category('UPDATE sleep_disorder SET count = %s WHERE sleep_disorder = %s', count, cat)

# check query for debug
#repo.check_query(20)


# UTILITY
def select_all_category(category, limit=0):

    if category in util.category_list:

        if limit > 0:
            sql = 'SELECT * FROM {} LIMIT {};'.format(category, limit)
        else:
            sql = 'SELECT * FROM {};'.format(category)

        return repo.exec(sql)

    else:
        print('<!> category:', category, 'not found')

def select_all_people(limit=0):

    if limit > 0:
        sql = 'SELECT * FROM person LIMIT {};'.format(limit)
    else:
        sql = 'SELECT * FROM person;'

    return repo.exec(sql)

