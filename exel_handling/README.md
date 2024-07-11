# Population Data Analysis

This Python script reads population data from an Excel file (`censuspopdata.xlsx`), processes it to calculate the total population for each state and the population for each county within those states, and then saves the results to a JSON file (`states_populations.json`).

## Requirements

- Python 3.x
- `openpyxl` library
- `json` library (usually included with Python standard library)

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Install the `openpyxl` library using pip:

    ```bash
    pip install openpyxl
    ```

## Usage

1. Place the `censuspopdata.xlsx` file in the same directory as the `counting_pop.py` script or update the file path in the script to point to the correct location.

2. Run the script:

    ```bash
    python counting_pop.py
    ```

3. The script will generate a `states_populations.json` file in the same directory, containing the calculated population data.

## File Structure

- `censuspopdata.xlsx`: The input Excel file containing population data. The worksheet named "Population by Census Tract" is used for data extraction.
- `states_populations.json`: The output JSON file containing the calculated population data for each state and county.

## Script Details

- The script opens the Excel file and selects the "Population by Census Tract" worksheet.
- It iterates through each row (skipping the header row) to extract state, county, and population data.
- It calculates the total population for each state and the population for each county within those states.
- The results are saved in a JSON file with the following structure:

    ```json
    {
        "State1": {
            "total_population": 123456,
            "counties": {
                "County1": 12345,
                "County2": 23456
            }
        },
        "State2": {
            "total_population": 78901,
            "counties": {
                "County3": 7890,
                "County4": 1234
            }
        }
    }
    ```

- The script closes the workbook and prints "Done." to indicate completion.

## Notes

- Ensure that the Excel file is properly formatted and contains the expected data in the "Population by Census Tract" worksheet.
- The script assumes that the population data is numeric. Non-numeric values are skipped during processing.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.