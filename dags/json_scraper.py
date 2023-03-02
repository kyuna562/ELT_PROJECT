import json
import requests
import boto3
import datetime

date = str(datetime.date.today())


def json_scraper(url, file_name, bucket):
    response = requests.request("GET", url)
    json_data = response.json()

    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)

    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket, f"predict_files/date_{date}.json")
