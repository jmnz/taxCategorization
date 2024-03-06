# taxCategorization

## Description:

This Python script automates expense classification for CSV data, aiming to streamline the process for businesses. It leverages regular expressions for pattern matching and a user-defined dictionary to map expense descriptions to corresponding tax categories.

## Features:

Efficiently processes CSV files containing expense data.
Utilizes regular expressions for flexible pattern matching in expense descriptions.
Employs a user-defined dictionary to categorize expenses based on descriptions.
Handles case-insensitive matching for broader applicability.

## Installation:

This script requires the following Python libraries:

csv (included in the standard library)
re (included in the standard library)

## Usage:

1. Clone the repository:

```
git clone https://github.com/jmnz/python-expense-classification.git
```

2. Replace placeholders:

- Update input_file and output_file variables in process_csv function to match your CSV file paths.
- Modify the categoryDictionary to align with your specific expense categories and tax classifications.

3. Run the script:

```
python process_csv.py
```

This will execute the script and generate a new CSV file (result.csv) with the classified expenses.

## Example Usage:

The script includes an example usage section demonstrating how to set up the input_file, output_file, and categoryDictionary for a sample scenario.

## Additional Notes:

- Consider adding error handling mechanisms to gracefully handle potential issues like file I/O errors or invalid data formats.
- Explore more advanced techniques like fuzzy string matching or machine learning models for improved accuracy with highly variable data.
- Include unit tests to ensure the script's functionality and catch regressions in future modifications.

## License:

:man_shrugging: :ok_man:
