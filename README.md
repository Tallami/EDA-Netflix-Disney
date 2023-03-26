# Comparative Exploratory Data Analysis of Netflix and Disney+ Content

In this project, I analyzed two datasets from Disney and Netflix to gain insights into trends in content production in the entertainment industry. I found that Netflix produces significantly more original content than Disney, and that both Netflix and Disney are responding to the growing demand for family-friendly content by producing more content for children and families.

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

## 📊 Project Structure
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
  
## 🚀 Getting Started

1. Clone the repository to your local machine.
2. Install the required Python packages listed in `requirements.txt`.
3. Download the datasets from the provided links and place them in the `data/raw` directory.
4. Run the Jupyter notebooks in the `notebooks` directory to perform data cleaning, processing, and analysis.
5. Execute the SQL files in the `sql` directory to create tables, load data, and run queries.
