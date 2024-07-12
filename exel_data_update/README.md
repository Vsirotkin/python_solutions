# Product Price Updater

This Python script is designed to update the price of a specified product in an Excel file and mark the product as updated. It also recalculates the total for each product based on the updated price and the quantity sold.

## Features

- Loads product data from an Excel file.
- Updates the price of a specified product.
- Marks the product as updated in the Excel file.
- Recalculates the total for each product based on the updated price and quantity sold.
- Saves the updated data to a new Excel file.

## Requirements

- Python 3.x
- `openpyxl` library

## Installation

1. Clone the repository or download the script.
2. Install the required `openpyxl` library using pip:

    ```sh
    pip install openpyxl
    ```

## Usage

1. Ensure your Excel file is named `produceSales.xlsx` and is located in the same directory as the script.
2. Run the script:

    ```sh
    python price_updating.py
    ```

3. Enter the name of the product you want to update when prompted.
4. Enter the new price for the product when prompted.
5. The script will save the updated data to a new file named `products_revised.xlsx`.

## File Structure

- `produceSales.xlsx`: The input Excel file containing product data.
- `products_revised.xlsx`: The output Excel file with updated product data.

## Functions

### `load_products(file_path: str) -> dict[str, float]`

- Loads product data from the specified Excel file.
- Returns a dictionary where the keys are product names and the values are prices.

### `update_price_and_mark_updated(file_path: str, product_name: str, new_price: float) -> None`

- Updates the price of the specified product in the Excel file.
- Marks the product as updated.
- Recalculates the total for each product based on the updated price and quantity sold.
- Saves the updated data to a new file named `products_revised.xlsx`.

### `main() -> None`

- Prompts the user to enter the name of the product to update.
- Calls the `update_price_and_mark_updated` function to perform the update.
- Handles `ValueError` exceptions if the product is not found in the file.

## Notes

- The script clears the terminal screen after execution.
- Ensure the input Excel file (`produceSales.xlsx`) is formatted correctly with product names in the first column, prices in the second column, and quantities in the third column.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.