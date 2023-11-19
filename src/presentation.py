from src import parser
from src import utility as util
import matplotlib.pyplot as plt

# setting matplotlib graph
plt.rcParams.update({'font.size': util.graph_settings.get('font-size')})

# GRAPHS
def bar_category_distributions():

    bmi_category = parser.select_all_category(util.get_bmi_category_name())
    bmi_x = list()
    bmi_y = list()
    for bmi in bmi_category:
        bmi_x.append(bmi[1] + ' (' + util.get_percentage(bmi[2]) + ')')
        bmi_y.append(bmi[2])

    gender_category = parser.select_all_category(util.get_gender_category_name())
    gender_x = list()
    gender_y = list()
    for gender in gender_category:
        gender_x.append(gender[1] + ' (' + util.get_percentage(gender[2]) + ')')
        gender_y.append(gender[2])

    occupation_category = parser.select_all_category(util.get_occupation_category_name())
    occupation_x = list()
    occupation_y = list()
    for occupation in occupation_category:
        occupation_x.append(
            util.remove_vowels(str(occupation[1]).split()[0].lower()) + ' (' + util.get_percentage(occupation[2], -1) + ')')
        occupation_y.append(occupation[2])

    sleep_disorder_category = parser.select_all_category(util.get_sleep_disorder_category_name().replace(' ', '_'))
    sleep_disorder_x = list()
    sleep_disorder_y = list()
    for sleep_disorder in sleep_disorder_category:
        sleep_disorder_x.append(sleep_disorder[1] + ' (' + util.get_percentage(sleep_disorder[2]) + ')')
        sleep_disorder_y.append(sleep_disorder[2])

    util.draw_category_bar(bmi_x, bmi_y, 1, util.get_bmi_category_name(), util.get_color('orange'))
    util.draw_category_bar(gender_x, gender_y, 2, util.get_gender_category_name(), util.get_color('cyan'))
    util.draw_category_bar(occupation_x, occupation_y, 3, util.get_occupation_category_name(), util.get_color('green'))
    util.draw_category_bar(sleep_disorder_x, sleep_disorder_y, 4, util.get_sleep_disorder_category_name(), util.get_color('purple'))

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

    util.draw_data_hist(age, 1, util.get_age_data_name())
    util.draw_data_hist(sleep_duration, 2, util.get_sleep_duration_data_name())
    util.draw_data_hist(quality_of_sleep, 3, util.get_quality_of_sleep_data_name())
    util.draw_data_hist(physical_activity_level, 4, util.get_physical_activity_level_data_name())
    util.draw_data_hist(stress_level, 5, util.get_stress_level_data_name())
    util.draw_data_hist(hearth_rate, 6, util.get_hearth_rate_data_name())
    util.draw_data_hist(blood_pressure, 7, util.get_blood_pressure_data_name())
    util.draw_data_hist(daily_steps, 8, util.get_daily_steps_data_name())

    plt.show()