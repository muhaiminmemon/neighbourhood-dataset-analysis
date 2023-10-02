from typing import TextIO
import statistics

# Constants from constants.py
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

OTHER_DATA = {
    'Mount': {
        'id': 0,
        'hypertension': [500, 13906, 4578, 5314, 2527, 3020],
        'total': 1940, 'low_income': 2784},
    'RK': {
        'id': 1,
        'hypertension': [111, 3596, 2336, 2522, 7294, 3844],
        'total': 15667, 'low_income': 4352}
}

EPSILON = 0.005


# This function is provided for use in Task 3. You do not need to
# change it.  Note the use of EPSILON constant (similar to what we had
# in asisgnment 2) for testing.
def get_age_standardized_ht_rate(city_data: CityData, nbh_name: str) -> float:
    """Return the age standardized hypertension rate from the
    neighbourhood in city_data with neighbourhood name nbh_name.
    """

    rates = calculate_ht_rates_by_age_group(city_data, nbh_name)

    canada_20_44 = 11_199_830 / 19_735_665  
    canada_45_64 = 5_365_865 / 19_735_665   
    canada_65_plus = 3_169_970 / 19_735_665 

    return (rates[0] * canada_20_44 + rates[1] * canada_45_64 +
            rates[2] * canada_65_plus)


def get_hypertension_data(dictionary: CityData, file: TextIO) -> None:

    """Modify dictionary to add hypertension data from TextIO to dictionary.
    """
    for line in file:
        # Split the line into columns
        columns = line.strip().split(",")

        # Get the neighbourhood name and ID
        name = columns[0]
        id = columns[1]

        # Get the hypertension dictionary
        hypertension = columns[2:]

        # Update the dictionary with the hypertension dictionary
        if name in dictionary:
            dictionary[name][ID] = id
            dictionary[name][HT] = hypertension
        else:
            dictionary[name] = {ID: id, HT: hypertension}

def get_low_income_data(data, file: TextIO) -> None:

    """Modify dictionary to add low income data from TextIO to dictionary.
    """
    for line in file:
        # Split the line into columns
        columns = line.strip().split(",")

        # Get the neighbourhood name and ID
        name = columns[0]
        id = columns[1]

        # Get the total population and low income data
        total = columns[2]
        low_income = columns[3]

        # Update the dictionary with the low income data
        if name in data:
            data[name][ID] = id
            data[name][TOTAL] = total
            data[name][LOW_INCOME] = low_income
        else:
            data[name] = {
                ID: id,
                TOTAL: total,
                LOW_INCOME: low_income
            }

def get_bigger_neighbourhood(data: CityData, neighbourhood1: str, neighbourhood2: str) -> str:
    """Returns the neighbourhood with the larger population

    >>> result = get_bigger_neighbourhood(SAMPLE_DATA, 'Rexdale-Kipling', 'Mount Elms-Old Rexdale')
    >>> result == 'Rexdale-Kipling'
    True
    >>> result = get_bigger_neighbourhood(SAMPLE_DATA, 'Aroura', 'West Humber-Clairville')
    >>> result == 'West Humber-Clairville'
    True
    """
    population1 = 0
    population2 = 0

    if neighbourhood1 in data:
        population1 = data[neighbourhood1][TOTAL]

    if neighbourhood2 in data:
        population2 = data[neighbourhood2][TOTAL]

    if population1 >= population2:
        return neighbourhood1

    return neighbourhood2


def get_high_hypertension_rate(data: CityData,
                               threshold: float) -> list[tuple[str, float]]:

    """Returns hypertension rate of the neighbourhood

    Precondition: nbh is in data

    >>> get_high_hypertension_rate(SAMPLE_DATA, 0.4)
    []
    >>> get_high_hypertension_rate(SAMPLE_DATA, 0.31797739151574084)
    [('Thistletown-Beaumond Heights', 0.31797739151574084)]
    """
    neighbourhoods = []

    for index in data:

        ht_cases = (data[index][HT][HT_65_UP_IDX] + data[index][
            HT][HT_20_44_IDX] + data[index][HT][HT_45_64_IDX])

        total_population = (data[index][HT][NBH_65_UP_IDX] + data[
            index][HT][NBH_20_44_IDX] + data[index][HT][NBH_45_64_IDX])

        ht_rate = ht_cases / total_population

        if ht_rate >= threshold:
            neighbourhoods.append((index, ht_rate))

    return neighbourhoods


def get_ht_to_low_income_ratios(data: CityData) -> dict[str, float]:
    """Returns the ratio of hypertension rate to low income rate of neighbourhood

    >>> result = get_ht_to_low_income_ratios(SAMPLE_DATA)
    >>> result == {'West Humber-Clairville': 1.6683148168616895,
    ...            'Mount Olive-Silverstone-Jamestown': 0.9676885451091314,
    ...            'Thistletown-Beaumond Heights': 1.6438083107534431,
    ...            'Rexdale-Kipling': 1.5351962275111484,
    ...            'Elms-Old Rexdale': 1.1763941257986577}
    True
    >>> result = get_ht_to_low_income_ratios(OTHER_DATA)
    >>> result == {'Mount': 0.23828512620937733, 'RK': 3.520091582388075}
    True
    """

    result = {}

    for index in data:

        ht_cases = (data[index][HT][HT_65_UP_IDX] + data[
            index][HT][HT_20_44_IDX] + data[index][HT][HT_45_64_IDX])

        total_population = (data[index][HT][NBH_65_UP_IDX] + data[
            index][HT][NBH_20_44_IDX] + data[index][HT][NBH_45_64_IDX])

        ht_rate = ht_cases / total_population
        low_income_rate = data[index][LOW_INCOME] / data[index][TOTAL]
        result[index] = ht_rate / low_income_rate

    return result


def calculate_ht_rates_by_age_group(data: CityData, nbh: str) -> tuple[float, float, float]:
    """Returns hypertension for the age groups in nbh as a percentage

    Precondition: nbh is a key in data

    >>> calculate_ht_rates_by_age_group(SAMPLE_DATA, 'Thistletown-Beaumond Heights')
    (6.058936931974663, 37.009544008483566, 76.34408602150538)

    >>> calculate_ht_rates_by_age_group(OTHER_DATA, 'RK')
    (3.0867630700778643, 92.62490087232355, 189.75026014568158)

    """
    senior = data[nbh][HT][HT_65_UP_IDX] / data[nbh][HT][NBH_65_UP_IDX] * 100
    middle = data[nbh][HT][HT_45_64_IDX] / data[nbh][HT][NBH_45_64_IDX] * 100
    young = data[nbh][HT][HT_20_44_IDX] / data[nbh][HT][NBH_20_44_IDX] * 100

    return (young, middle, senior)

def get_correlation(data: CityData) -> float:

    """Returns correlation between low income rates and age standardized
    hypertension rates in the dictionary

    >>> get_correlation(SAMPLE_DATA)
    0.28509539188554994
    >>> get_correlation(OTHER_DATA)
    -1.0

    """
    age_stand_hypertension = []
    low_income_rates = []

    for index in data:

        age_stand_hypertension.append(get_age_standardized_ht_rate(
            data, index))

        low_income_rates.append(data[index][LOW_INCOME] / data[
            index][TOTAL])

    return statistics.correlation(low_income_rates, age_stand_hypertension)


def order_by_ht_rate(data: CityData) -> list[str]:

    """Return the names of the neighbourhoods in data, ordered from lowest to
    highest age-standardized hypertension rate.

    order_by_ht_rate(OTHER_DATA)
    ['Mount', 'RK']
    >>> result = order_by_ht_rate(SAMPLE_DATA)
    >>> result == ['Elms-Old Rexdale', 'Rexdale-Kipling',
    ... 'Thistletown-Beaumond Heights', 'West Humber-Clairville',
    ... 'Mount Olive-Silverstone-Jamestown']
    True
    """
    names_and_rates = []
    for name in data:
        rate = get_age_standardized_ht_rate(data, name)
        names_and_rates.append((name, rate))

    names_and_rates.sort(key=lambda x: x[1])

    return [name for (name, rate) in names_and_rates]


if __name__ == '__main__':
    import doctest
    doctest.testmod()