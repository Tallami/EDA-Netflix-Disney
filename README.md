# EDA Project: Analyzing Netflix and Disney Content

- This project involves conducting a comprehensive **Exploratory Data Analysis** on two **Data Sets** stored in an AWS S3 Bucket.
- The analysis is performed using **Python** and **SQL**.
  
## 📝 Description
- This project involves conducting a comprehensive **Exploratory Data Analysis (EDA)** on two datasets containing information about **Netflix** and **Disney+** content, with the data stored in an **AWS S3 Bucket**. The analysis is performed using **Python** and **SQL**.

## 🎯 Objective:
- The objective of this project is to uncover patterns and insights within the content provided by **Netflix** and **Disney+**, and to compare the two platforms based on various factors such as genres, release years, and content types.

## 💻 Tools & Technologies:
- **AWS S3 Bucket** for data storage
- **Boto3** for interacting with the S3 Bucket using Python
- **Python** for data processing and analysis
- **SQL** for querying and filtering data
- **Matplotlib** and **Seaborn** for data visualization

## ⏳ Dataset
- The datasets used in this project are in a **AWS S3 Bucket** but can be accessed through the following links:
  - Netflix Shows: https://www.kaggle.com/datasets/shivamb/netflix-shows?datasetId=434238
  - Disney Movies and TV Shows: https://www.kaggle.com/datasets/shivamb/disney-movies-and-tv-shows

## Project Structure
This project is organized as follows:

- `data`: Contains the raw and processed datasets.
  - `processed`: Contains the cleaned and processed data files.
  - `raw`: Contains the original data files.
- `notebooks`: Contains Jupyter notebooks for various stages of the project.
  - `1.0-Previsualization.ipynb`: Initial data exploration.
  - `1.1-CleaningDisney.ipynb`: Data cleaning for the Disney dataset.
  - `1.1-CleaningNetflix.ipynb`: Data cleaning for the Netflix dataset.
  - `1.2-EDA.ipynb`: Exploratory Data Analysis.
  - `pandasAPI.ipynb`: Pandas API usage.
- `requirements.txt`: Lists the required Python packages for the project.
- `sql`: Contains SQL files for creating tables, loading data, and executing queries.
  - `create_tables.sql`: SQL file for creating tables.
  - `load_data.sql`: SQL file for loading data into tables.
  - `querys.sql`: SQL file containing various queries for analysis.
- `src`: Contains Python scripts for the project.
  - `downloadS3.py`: Python script for downloading data from the AWS S3 Bucket.
