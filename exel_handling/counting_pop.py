import openpyxl
import json

# Open the Excel file
workbook = openpyxl.load_workbook("censuspopdata.xlsx")

# Select the worksheet
worksheet = workbook["Population by Census Tract"]

# Read the data from the worksheet and calculate the sum of Population for each State and County
data = {}
for row in worksheet.iter_rows(min_row=2, values_only=True):  # Skip header row
    state = row[1]
    county = row[2]
    population = row[3]

    if not isinstance(population, (int, float)):
        continue

    if state not in data:
        data[state] = {"total_population": 0, "counties": {}}

    if county not in data[state]["counties"]:
        data[state]["counties"][county] = 0

    data[state]["counties"][county] += int(population)
    data[state]["total_population"] += int(population)

# Save the calculated data to a JSON file
with open("states_populations.json", "w") as file:
    json.dump(data, file, indent=4)

# Close the workbook
workbook.close()

print('Done.')
