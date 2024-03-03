# Project: Anime Database Migration

This project aims to migrate data from CSV files to a PostgreSQL database named "anime". The provided Python script facilitates the extraction of data from CSV files, the creation of the database schema, and the insertion of data into the corresponding tables within the database.

## Requirements
- Python 3.x
- PostgreSQL

## Setup

1. **Install Dependencies:**
   Ensure you have the required Python dependencies installed. You can install them using pip:

   ```
   pip install psycopg2 pandas numpy
   ```

2. **Database Configuration:**
   Ensure PostgreSQL is installed and running on your system. You need to set up a PostgreSQL database named "anime" with the appropriate user credentials.

   ```
   host=127.0.0.1
   dbname=postgres
   user=postgres
   password=********
   ```

3. **CSV Files:**
   Prepare your CSV files containing the data to be migrated. The script expects two CSV files: `anime.csv` and `rating.csv`. You can download the dataset from https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database

## Usage

1. **Clone the Repository:**
   Clone or download the repository to your local machine.

2. **Run the Script:**
   Execute the Python script `data_migration.py`. This script performs the following actions:

   - Connects to the PostgreSQL database.
   - Creates necessary tables (`anime` and `rating`) if they do not exist.
   - Reads data from CSV files (`anime.csv` and `rating.csv`).
   - Inserts data into the respective tables in the database.

   ```
   python data_migration.py
   ```

3. **Verify Data:**
   Once the script execution completes successfully, verify that the data has been migrated correctly by querying the PostgreSQL database using your preferred database management tool.

## CSV File Format

Ensure that your CSV files (`anime.csv` and `rating.csv`) follow the appropriate format for the migration script to work correctly. The script assumes the following structure:

- `anime.csv`:
  - Columns: id, name, genre, type, episodes, rating, members

- `rating.csv`:
  - Columns: user_id, anime_id, rating

Note: The script handles 'Unknown' values in the 'episodes' column of the `anime.csv` file by replacing them with 0 during the migration process.

## Future work

Implement incremental data migration capabilities to support updates and additions to the existing dataset without re-importing the entire dataset. This can be done by scraping myanimelist (the source of the original dataset) for new added animes and user ratings for these animes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
