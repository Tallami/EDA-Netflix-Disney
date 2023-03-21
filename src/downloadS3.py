import boto3
import os


def download_s3(bucket_name, file_key, download_path):
    """
    Descarga archivos de un bucket de Amazon S3 y los guarda en una ruta

    1 - bucket_name = Nombre del bucket de S3
    2 - file_key = Nombre del archivo en el bucket
    3 - download_path = Ruta de guardado del archivo descargado

    """
    # Recurso de S3
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    # Ruta de descarga
    file_name = os.path.basename(file_key)
    download_file_path = os.path.join(download_path, file_name)

    # Descarga
    bucket.download_file(file_key, download_file_path)


# Disney CSV
bucket_name = 'tallami-bucket'
file_key = 'disney_plus_titles.csv'
download_path = './data/raw'
download_s3(bucket_name, file_key, download_path)

# Netflix CSV
bucket_name = 'tallami-bucket'
file_key = 'netflix_titles.csv'
download_path = './data/raw'
download_s3(bucket_name, file_key, download_path)
