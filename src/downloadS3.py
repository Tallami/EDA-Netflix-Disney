import boto3
import os

def download_s3(bucket_name, file_key, download_path):
    """
    Download files from an Amazon S3 bucket and save them to a specified path.
    1 - bucket_name: Name of the S3 bucket
    2 - file_key: Name of the file in the bucket
    3 - download_path: Path where the downloaded file will be saved
    """
    # S3 Resource
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    # Download Path
    file_name = os.path.basename(file_key)
    download_file_path = os.path.join(download_path, file_name)

    # Download
    bucket.download_file(file_key, download_file_path)

# Download Disney CSV from S3 Bucket
bucket_name = 'tallami-bucket'
file_key = 'disney_plus_titles.csv'
download_path = './data/raw'
download_s3(bucket_name, file_key, download_path)

# Download Netflix CSV from S3 Bucket
bucket_name = 'tallami-bucket'
file_key = 'netflix_titles.csv'
download_path = './data/raw'
download_s3(bucket_name, file_key, download_path)
