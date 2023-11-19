from src import parser
import matplotlib.pyplot as plt

# categories names
category_list = ['bmi', 'gender', 'occupation', 'sleep_disorder']


def get_bmi_category_name():
    return category_list[0]


def get_gender_category_name():
    return category_list[1]


def get_occupation_category_name():
    return category_list[2]


def get_sleep_disorder_category_name():
    return category_list[3].replace('_', ' ')


# data names
data_list = ['age', 'sleep_duration', 'quality_of_sleep', 'physical_activity_level', 'stress_level', 'blood_pressure',
             'hearth_rate', 'daily_steps']


def get_age_data_name():
    return data_list[0]


def get_sleep_duration_data_name():
    return data_list[1].replace('_', ' ')


def get_quality_of_sleep_data_name():
    return data_list[2].replace('_', ' ')


def get_physical_activity_level_data_name():
    return data_list[3].replace('_', ' ')


def get_stress_level_data_name():
    return data_list[4].replace('_', ' ')


def get_blood_pressure_data_name():
    return data_list[5].replace('_', ' ')


def get_hearth_rate_data_name():
    return data_list[6].replace('_', ' ')


def get_daily_steps_data_name():
    return data_list[7].replace('_', ' ')


# graphical settings
graph_settings = {'font-size': 4,
                  'title-size': 12,
                  'title-size-small': 6,
                  'category-matrix': (2, 2),
                  'data-matrix': (2, 4)}


palette = {'blue': '#0072BD',
           'orange': '#D95319',
           'yellow': '#EDB120',
           'purple': '#7E2F8E',
           'green': '#77AC30',
           'cyan': '#4DBEEE',
           'red': '#A2142F'}


def get_color(color='blue'):
    color_result = palette.get(color)

    if color_result is None:
        return '#0072BD'
    else:
        return color_result


def draw_category_bar(x, y, position, title, color='#0072BD'):
    mtrx = graph_settings.get('category-matrix')
    plt.subplot(mtrx[0], mtrx[1], position)
    plt.bar(x, y, color=color)
    plt.title(title.upper(), size=graph_settings.get('title-size'))


def draw_data_hist(data, position, title, color='#0072BD'):
    mtrx = graph_settings.get('data-matrix')
    plt.subplot(mtrx[0], mtrx[1], position)
    plt.hist(data, color=color)
    plt.title(title.upper(), size=graph_settings.get('title-size-small'))


# misc
def get_percentage(weigh, decimal=2):
    if decimal >= 0:
        return str(round((weigh * 100) / parser.record_count, decimal)) + '%'
    else:
        return str(int((weigh * 100) / parser.record_count)) + '%'


def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ''.join([char for char in string if char not in vowels])
    return result

