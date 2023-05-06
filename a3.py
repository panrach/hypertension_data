"""CSCA08: Fall 2022 -- Assignment 3: Hypertension and Low Income

Starter code.

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2022 Jacqueline Smith, David Liu, and Anya Tafliovich

"""

from typing import TextIO
import statistics

from constants import (CityData, ID, HT, TOTAL, LOW_INCOME,
                       SEP, HT_ID_COL, LI_ID_COL,
                       HT_NBH_NAME_COL, LI_NBH_NAME_COL,
                       HT_20_44_COL, NBH_20_44_COL,
                       HT_45_64_COL, NBH_45_64_COL,
                       HT_65_UP_COL, NBH_65_UP_COL,
                       POP_COL, LI_POP_COL,
                       HT_20_44_IDX, HT_45_64_IDX, HT_65_UP_IDX,
                       NBH_20_44_IDX, NBH_45_64_IDX, NBH_65_UP_IDX
                       )
SAMPLE_DATA = {
    'West Humber-Clairville': {
        'id': 1,
        'hypertension': [703, 13291, 3741, 9663, 3959, 5176],
        'total': 33230, 'low_income': 5950},
    'Mount Olive-Silverstone-Jamestown': {
        'id': 2,
        'hypertension': [789, 12906, 3578, 8815, 2927, 3902],
        'total': 32940, 'low_income': 9690},
    'Thistletown-Beaumond Heights': {
        'id': 3,
        'hypertension': [220, 3631, 1047, 2829, 1349, 1767],
        'total': 10365, 'low_income': 2005},
    'Rexdale-Kipling': {
        'id': 4,
        'hypertension': [201, 3669, 1134, 3229, 1393, 1854],
        'total': 10540, 'low_income': 2140},
    'Elms-Old Rexdale': {
        'id': 5,
        'hypertension': [176, 3353, 1040, 2842, 948, 1322],
        'total': 9460, 'low_income': 2315}
}

# for testing
SAMPLE_DATA2 = {
    'A': {
        'id': 1,
        'hypertension': [703, 13291, 3741, 9663, 3959, 5176],
        'total': 222222, 'low_income': 5950},
    'B': {
        'id': 2,
        'hypertension': [789, 12906, 3578, 8815, 2927, 3902],
        'total': 32942, 'low_income': 9690},
    'C': {
        'id': 3,
        'hypertension': [220, 3631, 1047, 2829, 1349, 1767],
        'total': 10364, 'low_income': 2005},
    'D': {
        'id': 4,
        'hypertension': [201, 3669, 1134, 3229, 1393, 1854],
        'total': 10545, 'low_income': 2140},
    'E': {
        'id': 5,
        'hypertension': [176, 3353, 1040, 2842, 948, 1322],
        'total': 9466, 'low_income': 2315}
}

# for testing
EMPTY_DICT = {}

EPSILON = 0.005

HT_DATA_NUM_COL = NBH_65_UP_COL + 1
LOW_INCOME_NUM_COL = LI_POP_COL + 1

# Task 1


def extract_ht_data(data_line: list[str]) -> list[int]:
    """
    Return the hypertension data of data_line.

    Precondition: data_line is length 6.

    >>> extract_ht_data(['3', 'a', '2', '3', '1', '2', '1', '1'])
    [2, 3, 1, 2, 1, 1]
    >>> extract_ht_data(['4', 'b', '5', '3', '3', '20', '2', '11'])
    [5, 3, 3, 20, 2, 11]

    """

    new_list = []

    for i in range(HT_20_44_COL, len(data_line)):
        new_list.append(int(data_line[i]))

    return new_list


# input contents: line that contains data about the neighbourhood
# input format: contains: id, nbh name, ht data
# input example: '1,West Humber-Clairville,703,13291,3741,9663,3959,5176'
# output: nbh_data (the dictionary)
# output format:
# key: nbh name, value: {'id': integer, 'hypertension':
# [int1, int2, int3, int4, int5, int6]}
# output example
# 'West Humber-Clairville': {'id': 1, 'hypertension':
# [703, 13291, 3741, 9663, 3959, 5176]}


def get_hypertension_data(nbh_data: dict, ht_file: TextIO) -> None:
    """
    Modify nbh_data so that it contains the hypertension data in ht_file.

    Precondition: number of columns in ht_file is HT_DATA_NUM_COL.

    """

    line = ht_file.readline()  # skip header

    while line != '':
        line = ht_file.readline()
        columns = line.rstrip().split(SEP)
        if len(columns) != HT_DATA_NUM_COL:
            continue

        nbh_name = columns[HT_NBH_NAME_COL]
        nbh_id = int(columns[HT_ID_COL])
        ht_data = extract_ht_data(columns)

        if nbh_name not in nbh_data:
            nbh_data[nbh_name] = {}

        nbh_data[nbh_name][ID] = nbh_id
        nbh_data[nbh_name][HT] = ht_data


# input contents: lines containing data about the neighbourhood
# input format: contains id, nbh name, total, low_income
# input example: '1,West Humber-Clairville,33230,5950'
# output: nbh_data (the dictionary)
# output format
# key: nbh name, value: {'id': integer, 'total': int, 'low income': int}
# output example:
# 'West Humber-Clairville': {'id': 1, 'total': 33230, 'low_income': 5950}


def get_low_income_data(nbh_data: dict, income_file: TextIO) -> None:
    """
    Modify nbh_data so that it contains the low income data in income_file.

    Precondition: the number of columns in income_file is LOW_INCOME_NUM_COL

    """

    line = income_file.readline()  # skip header

    while line != '':
        line = income_file.readline()
        columns = line.rstrip().split(SEP)

        if len(columns) != LOW_INCOME_NUM_COL:
            continue

        nbh_name = columns[LI_NBH_NAME_COL]
        nbh_id = int(columns[LI_ID_COL])
        total = int(columns[POP_COL])
        low_income = int(columns[LI_POP_COL])
        if nbh_name not in nbh_data:
            nbh_data[nbh_name] = {}

        nbh_data[nbh_name][ID] = nbh_id
        nbh_data[nbh_name][TOTAL] = total
        nbh_data[nbh_name][LOW_INCOME] = low_income


# Task 2

def get_population(city_data: CityData, nbh: str) -> int:
    """
    Return the population of nbh in city_data. If nbh is not in city_data,
    return 0.

    >>> get_population(SAMPLE_DATA, 'Hello')
    0
    >>> get_population(SAMPLE_DATA, 'West Humber-Clairville')
    33230

    """

    if nbh in city_data:
        nbh_data = city_data[nbh]
        return nbh_data[TOTAL]

    return 0


def get_bigger_neighbourhood(city_data: CityData, nbh1: str, nbh2: str) -> str:
    """
    Return the name of the neighbourhood with the higher population in
    city_data. That is, return nbh1 if it has the highest population or return
    nbh2 if it has the highest population. If both have the same population,
    return nbh1.

    Preconditions:
    - if nbh1 or nbh2 is not in city_data, the population of the
    neighborhood is 0.
    - nbh1 and nbh2 are different
    - each neighbourhood has a population of at least 0

    """

    population1 = get_population(city_data, nbh1)
    population2 = get_population(city_data, nbh2)

    if population1 >= population2:
        return nbh1

    return nbh2


def get_ht_rate(city_data: CityData, nbh: str) -> float:
    """
    Return the hypertension rate of nbh in city_data given population.

    Precondition: nbh is a valid neighborhood in city_data.

    >>> get_ht_rate(SAMPLE_DATA, 'West Humber-Clairville')
    0.2987202275151084
    >>> get_ht_rate(SAMPLE_DATA, 'Mount Olive-Silverstone-Jamestown')
    0.28466612028255867

    """

    nbh_data = city_data[nbh]
    ht_list = nbh_data[HT]
    population = (ht_list[NBH_20_44_IDX] + ht_list[NBH_45_64_IDX] +
                  ht_list[NBH_65_UP_IDX])
    num_hypertension = (ht_list[HT_20_44_IDX] + ht_list[HT_45_64_IDX] +
                        ht_list[HT_65_UP_IDX])

    return num_hypertension / population


def get_high_hypertension_rate(city_data: CityData,
                               threshold: float) -> list[tuple[str, float]]:
    """
    Return a list of tuples of all neighbourhoods that have a hypertension rate
    greater than or equal to threshold in city_data with its corresponding
    hypertension rate.

    Preconditions:
    - no neighborhood has a population of 0
    - assume 0.0 <= threshold <= 1.0

    >>> result = get_high_hypertension_rate(SAMPLE_DATA, 0.3)
    >>> expected = ([('Thistletown-Beaumond Heights', 0.31797739151574084),
    ...            ('Rexdale-Kipling', 0.3117001828153565)])
    >>> result == expected
    True
    >>> get_high_hypertension_rate(SAMPLE_DATA, 1.0)
    []

    """

    nbh_list = []

    for nbh in city_data:
        hypertension_rate = get_ht_rate(city_data, nbh)

        if hypertension_rate >= threshold:
            nbh_list.append((nbh, hypertension_rate))

    return nbh_list


def get_low_income_rate(city_data: CityData, nbh: str) -> float:
    """
    Return the low income rate of nbh based on city_data.

    >>> get_low_income_rate(SAMPLE_DATA, 'West Humber-Clairville')
    0.1790550707192296
    >>> get_low_income_rate(SAMPLE_DATA, 'Mount Olive-Silverstone-Jamestown')
    0.2941712204007286

    Precondition: the population of nbh is never 0.

    """

    population = get_population(city_data, nbh)
    nbh_data = city_data[nbh]
    low_income = nbh_data[LOW_INCOME]

    return low_income / population


def get_ht_to_low_income_ratios(city_data: CityData) -> dict[str, float]:
    """
    Return a dictionary with each key being the same as city_data. Values are
    the ratio of the hypertension rate to the low income rate for the
    corresponding neighbourhood

    >>> result = get_ht_to_low_income_ratios(SAMPLE_DATA)
    >>> expected = ({'West Humber-Clairville': 1.6683148168616895,
    ...              'Mount Olive-Silverstone-Jamestown': 0.9676885451091314,
    ...              'Thistletown-Beaumond Heights': 1.6438083107534431,
    ...              'Rexdale-Kipling': 1.5351962275111484,
    ...              'Elms-Old Rexdale': 1.1763941257986577})
    >>> result == expected
    True
    >>> result = get_ht_to_low_income_ratios(SAMPLE_DATA2)
    >>> expected = ({'A': 11.156673344346625,
    ...              'B': 0.9677472997263207,
    ...              'C': 1.6436497185382235,
    ...              'D': 1.5359244989663243,
    ...              'E': 1.1771402531511728})
    >>> result == expected
    True

    """

    ht_to_low_income_ratios = {}

    for nbh in city_data:
        hypertension_rate = get_ht_rate(city_data, nbh)
        low_income_rate = get_low_income_rate(city_data, nbh)

        ht_to_low_income_ratios[nbh] = hypertension_rate / low_income_rate

    return ht_to_low_income_ratios


def calculate_ht_rates_by_age_group(city_data: CityData, nbh: str) -> tuple:
    """
    Return a tuple that contains the hypertension rates of each age group
    in nbh based on city_data.

    Precondition:
    - nbh is a neighbourhood in city_data
    - nbh does not have a population of 0

    >>> calculate_ht_rates_by_age_group(SAMPLE_DATA, 'Elms-Old Rexdale')
    (5.24903071875932, 36.593947923997185, 71.70953101361573)
    >>> calculate_ht_rates_by_age_group(SAMPLE_DATA2, 'B')
    (6.113435611343561, 40.589903573454336, 75.01281394156842)

    """

    nbh_data = city_data[nbh]
    ht_data = nbh_data[HT]

    age_20_44 = ht_data[HT_20_44_IDX] / ht_data[NBH_20_44_IDX] * 100
    age_45_64 = ht_data[HT_45_64_IDX] / ht_data[NBH_45_64_IDX] * 100
    age_65_up = ht_data[HT_65_UP_IDX] / ht_data[NBH_65_UP_IDX] * 100

    return (age_20_44, age_45_64, age_65_up)


# Task 3
# This function is provided for use in Task 3. You do not need to
# change it.  Note the use of EPSILON constant (similar to what we had
# in asisgnment 2) for testing.
def get_age_standardized_ht_rate(city_data: CityData, nbh_name: str) -> float:
    """Return the age standardized hypertension rate from the
    neighbourhood in city_data with neighbourhood name nbh_name.

    Precondition: nbh_name is in city_data

    >>> abs(get_age_standardized_ht_rate(SAMPLE_DATA, 'Elms-Old Rexdale') -
    ...     24.44627) < EPSILON
    True
    >>> abs(get_age_standardized_ht_rate(SAMPLE_DATA, 'Rexdale-Kipling') -
    ...     24.72562) < EPSILON
    True

    """

    rates = calculate_ht_rates_by_age_group(city_data, nbh_name)

    # These rates are normalized for only 20+ ages, using the census data
    # that our datasets are based on.
    canada_20_44 = 11_199_830 / 19_735_665   # Number of 20-44 / Number of 20+
    canada_45_64 = 5_365_865 / 19_735_665    # Number of 45-64 / Number of 20+
    canada_65_plus = 3_169_970 / 19_735_665  # Number of 65+ / Number of 20+

    return (rates[0] * canada_20_44 + rates[1] * canada_45_64 +
            rates[2] * canada_65_plus)


def get_correlation(city_data: CityData) -> float:
    """
    Return the correlation between age standardised hypertension rates and
    low income rates across every neighborhood in city_data.

    >>> get_correlation(SAMPLE_DATA)
    0.28509539188554994
    >>> get_correlation(SAMPLE_DATA2)
    -0.021526155999741513

    """
    low_income = []
    age_std_ht = []

    for nbh in city_data:
        age_std_ht.append(get_age_standardized_ht_rate(city_data, nbh))
        low_income.append(get_low_income_rate(city_data, nbh))

    return statistics.correlation(age_std_ht, low_income)


# Task 4


def order_by_ht_rate(city_data: CityData) -> list[str]:
    """
    Return the names of every neighbourhood in city_data ordered by lowest
    to highest age-standarised hypertension rate

    Precondition: Each neighbourhood in city_data has a different hypertension
    rate

    >>> value = order_by_ht_rate(SAMPLE_DATA)
    >>> expected = (['Elms-Old Rexdale', 'Rexdale-Kipling',
    ...              'Thistletown-Beaumond Heights', 'West Humber-Clairville',
    ...              'Mount Olive-Silverstone-Jamestown'])
    >>> value == expected
    True
    >>> order_by_ht_rate(SAMPLE_DATA2)
    ['E', 'D', 'C', 'A', 'B']

    """

    nbh_data_list = []
    return_list = []

    for nbh in city_data:
        data = get_age_standardized_ht_rate(city_data, nbh)
        nbh_data_list.append((data, nbh))

    nbh_data_list.sort()

    for pair in nbh_data_list:
        return_list.append(pair[1])

    return return_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    """
    # Uncomment when ready to test:
    # Using the small data files:
    small_data = {}
    # add hypertension data
    with open('hypertension_data_small.csv') as ht_small_f:
        get_hypertension_data(small_data, ht_small_f)
    # add low income data
    with open('low_income_small.csv') as li_small_f:
        get_low_income_data(small_data, li_small_f)

    print('Did we build the dict correctly?', small_data == SAMPLE_DATA)
    print('Correlation in small data file:', get_correlation(small_data))

    # Using the example data files:
    example_neighbourhood_data = {}
    # add hypertension data
    with open('hypertension_data_2016.csv') as ht_example_f:
        get_hypertension_data(example_neighbourhood_data, ht_example_f)
    # add low income data
    with open('low_income_2016.csv') as li_example_f:
        get_low_income_data(example_neighbourhood_data, li_example_f)
    print('Correlation in example data file:',
          get_correlation(example_neighbourhood_data))
    """
