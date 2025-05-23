﻿# xlsx_to_sql

  

These Python scripts automate processing Excel files with student data, storing them in PostgreSQL, and generating a `results.xlsx` file with `student_id`, `full_name`, `score`, and `total`.

  

## Features

- Reads `fake_data0.xlsx` (`student_id`, `full_name`) and `fakedata[1-3].xlsx` (`student_id`, `full_name`, `score`) using `openpyxl`.

- Stores and processes data in PostgreSQL via `psycopg2`.

- Outputs `results.xlsx` with aggregated scores and totals.

  

## Technologies

- Python 3.8+

- openpyxl

- psycopg2

- PostgreSQL

  

## Setup

1. **Clone the Repository**:

```sh
git clone https://github.com/artahaam/xlsx_to_sql.git
cd xlsx_to_sql
```

  

2. **Install Dependencies**:

```sh
pip install -r requirements.txt
```

  

3. **Set Up PostgreSQL**:

   - Create a database (e.g., `course`).

   - Update connection details in `convert.py` (host, database, user, password).

  

4. **Prepare Excel Files**:

   - Place `fake_data0.xlsx`, `fakedata1.xlsx`, `fakedata2.xlsx`, `fakedata3.xlsx` in the project directory or generate them using:

```sh
python fake_data.py
```

  

## Usage

1. **Import Data**:

```sh
python convert.py
```

   Reads Excel files and stores data in PostgreSQL.

  

2. **Export Results**:

```sh
python export.py
```

   Generates `results.xlsx` with `student_id`, `full_name`, `score`, and `total`.

  

## File Structure

```sh
xlsx_to_sql/

├── convert.py        # Imports Excel data to PostgreSQL

├── export.py         # Generates results.xlsx

├── fake_data.py      # Generates sample Excel files

├── fake_data0.xlsx   # Student IDs and names

├── fakedata1.xlsx    # Scores

├── fakedata2.xlsx    # Scores

├── fakedata3.xlsx    # Scores

├── results.xlsx      # Output file

├── results.sql       # Can be an option in later updates

├── requirements.txt  # Dependencies

└── README.md         # This file
```

  
