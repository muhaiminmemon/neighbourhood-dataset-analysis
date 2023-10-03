# Neighbourhood Health Data Analysis

This Python script contains functions for analyzing health data for different neighborhoods. The data includes information about hypertension rates and low-income populations. Here's an overview of the script:

## Sample Data
- `SAMPLE_DATA` and `OTHER_DATA` are dictionaries containing sample health data for different neighborhoods. These dictionaries are used for testing the functions.

## Functions
1. `get_age_standardized_ht_rate(city_data: CityData, nbh_name: str) -> float`: Calculates and returns the age-standardized hypertension rate for a given neighborhood.

2. `get_hypertension_data(dictionary: CityData, file: TextIO) -> None`: Modifies a dictionary to add hypertension data from a TextIO file.

3. `get_low_income_data(data, file: TextIO) -> None`: Modifies a dictionary to add low-income data from a TextIO file.

4. `get_bigger_neighbourhood(data: CityData, neighbourhood1: str, neighbourhood2: str) -> str`: Compares two neighborhoods and returns the one with a larger population.

5. `get_high_hypertension_rate(data: CityData, threshold: float) -> list[tuple[str, float]]`: Returns a list of neighborhoods with hypertension rates above a specified threshold.

6. `get_ht_to_low_income_ratios(data: CityData) -> dict[str, float]`: Calculates the ratio of hypertension rates to low-income rates for each neighborhood.

7. `calculate_ht_rates_by_age_group(data: CityData, nbh: str) -> tuple[float, float, float]`: Calculates hypertension rates for different age groups in a neighborhood.

8. `get_correlation(data: CityData) -> float`: Calculates the correlation between low-income rates and age-standardized hypertension rates for all neighborhoods.

9. `order_by_ht_rate(data: CityData) -> list[str]`: Orders neighborhood names from lowest to highest age-standardized hypertension rate.

## Usage
- The script includes a conditional block `if __name__ == '__main__':` to execute doctests when the script is run as the main program.

## Testing
- The script includes doctests that demonstrate the usage and expected output of each function.

Make sure to provide the required data files and test the functions with your own datasets or use the provided sample data for testing.

# Repository Description

This repository contains Python scripts for analyzing neighborhood health data, including hypertension rates and low-income populations.
