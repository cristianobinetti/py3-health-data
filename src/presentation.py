from src import parser
from src import utility as util
import matplotlib.pyplot as plt

# settings
plt.rcParams.update({'font.size': 4})
title_size = 12
title_size_small = title_size/2


# GRAPHS
def bar_category_distributions():
    bmi_category = parser.select_all_category(util.get_bmi_category_name())
    bmi_x = list()
    bmi_y = list()
    for bmi in bmi_category:
        bmi_x.append(bmi[1] + ' (' + get_percentage(bmi[2]) + ')')
        bmi_y.append(bmi[2])

    gender_category = parser.select_all_category(util.get_gender_category_name())
    gender_x = list()
    gender_y = list()
    for gender in gender_category:
        gender_x.append(gender[1] + ' (' + get_percentage(gender[2]) + ')')
        gender_y.append(gender[2])

    occupation_category = parser.select_all_category(util.get_occupation_category_name())
    occupation_x = list()
    occupation_y = list()
    for occupation in occupation_category:
        occupation_x.append(
            remove_vowels(str(occupation[1]).split()[0].lower()) + ' (' + get_percentage(occupation[2], -1) + ')')
        occupation_y.append(occupation[2])

    sleep_disorder_category = parser.select_all_category(util.get_sleep_disorder_category_name())
    sleep_disorder_x = list()
    sleep_disorder_y = list()
    for sleep_disorder in sleep_disorder_category:
        sleep_disorder_x.append(sleep_disorder[1] + ' (' + get_percentage(sleep_disorder[2]) + ')')
        sleep_disorder_y.append(sleep_disorder[2])

    plt.subplot(2, 2, 1)
    plt.bar(bmi_x, bmi_y, color='orangered')
    plt.title(util.get_bmi_category_name().upper(), size=title_size)

    plt.subplot(2, 2, 2)
    plt.bar(gender_x, gender_y, color='royalblue')
    plt.title(util.get_gender_category_name().upper(), size=title_size)

    plt.subplot(2, 2, 3)
    plt.bar(occupation_x, occupation_y, color='forestgreen')
    plt.title(util.get_occupation_category_name().upper(), size=title_size)

    plt.subplot(2, 2, 4)
    plt.bar(sleep_disorder_x, sleep_disorder_y, color='mediumorchid')
    plt.title(util.get_sleep_disorder_category_name().upper().replace('_', ' '), size=title_size)

    plt.show()


def hist_data_distributions():
    people = parser.select_all_people()

    age = list() #2
    sleep_duration = list() #4
    quality_of_sleep = list() #5
    physical_activity_level = list() #6
    stress_level = list() #7
    blood_pressure = list() #9
    hearth_rate = list () #10
    daily_steps = list() #11

    #prnt = [age, sleep_duration, quality_of_sleep, physical_activity_level, stress_level, blood_pressure, hearth_rate, daily_steps]

    for person in people:
        age.append(person[2])
        sleep_duration.append(float(person[4]))
        quality_of_sleep.append(person[5])
        physical_activity_level.append(person[6])
        stress_level.append(person[7])
        # getting only the systolic pressure
        blood_pressure.append(int(str(person[9]).split('/')[0]))
        hearth_rate.append(person[10])
        daily_steps.append(person[11])

    # age hist
    plt.subplot(4, 2, 1)
    plt.hist(age)
    plt.title(util.get_age_data_name().upper(), size=title_size/2)

    # sleep_duration hist
    plt.subplot(4, 2, 2)
    plt.hist(sleep_duration)
    plt.title(util.get_sleep_duration_data_name().upper(), size=title_size/2)

    # quality_of_sleep hist
    plt.subplot(4, 2, 3)
    plt.hist(quality_of_sleep)
    plt.title(util.get_quality_of_sleep_data_name().upper(), size=title_size/2)

    # physical_activity_level hist
    plt.subplot(4, 2, 4)
    plt.hist(physical_activity_level)
    plt.title(util.get_physical_activity_level_data_name().upper(), size=title_size/2)

    # stress_level hist
    plt.subplot(4, 2, 5)
    plt.hist(stress_level)
    plt.title(util.get_stress_level_data_name().upper(), size=title_size/2)

    # hearth_rate hist
    plt.subplot(4, 2, 6)
    plt.hist(hearth_rate)
    plt.title(util.get_hearth_rate_data_name().upper(), size=title_size/2)

    # blood_pressure hist
    plt.subplot(4, 2, 7)
    plt.hist(blood_pressure)
    plt.title(util.get_blood_pressure_data_name().upper(), size=title_size/2)

    # daily_steps hist
    plt.subplot(4, 2, 8)
    plt.hist(daily_steps)
    plt.title(util.get_daily_steps_data_name().upper(), size=title_size/2)


    plt.show()


# UTILITY
def get_percentage(weigh, decimal=2):
    if decimal >= 0:
        return str(round((weigh * 100) / parser.get_record_count(), decimal)) + '%'
    else:
        return str(int((weigh * 100) / parser.get_record_count())) + '%'


def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ''.join([char for char in string if char not in vowels])
    return result
