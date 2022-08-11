import requests
from datetime import datetime, timedelta
import io
import pandas as pd
import os

def get_match_data():
    now = datetime.now()
    aws_path = "https://oracleselixir-downloadable-match-data.s3-us-west-2.amazonaws.com/"
    year = now.strftime("%Y")
    current_date = now.strftime("%Y%m%d")
    yesterday = (now - timedelta(days=1)).strftime("%Y%m%d")

    directory_name = "csv_files"
    name = "_LoL_esports_match_data_from_OraclesElixir_"
    if os.path.isfile(f'{directory_name}/Match Data {current_date}.csv'):
        match_data = pd.read_csv(f'{directory_name}/Match Data {current_date}.csv', low_memory=False)
        print("Getting data from todays existing file")
        return match_data
    else:
        try:
            url = f"{aws_path}{year}{name}{current_date}.csv"
            response = requests.get(url, allow_redirects=True)
            match_data = response.content.decode("utf-8")
            match_data = pd.read_csv(io.StringIO(match_data), low_memory=False)
            assert len(match_data) > 10
            csv_file_name = f'{directory_name}/Match Data {current_date}.csv'
            print("Downloaded todays data")

        except Exception as e:
            if os.path.isfile(f'{directory_name}/Match Data {yesterday}.csv'):
                match_data = pd.read_csv(f'{directory_name}/Match Data {yesterday}.csv', low_memory=False)
                print("Getting data from yesterdays existing file")
                return match_data
            else:
                # if there is no current date data then grab yesterdays data
                url = f"{aws_path}{year}{name}{yesterday}.csv"
                response = requests.get(url, allow_redirects=True)
                match_data = response.content.decode("utf-8")
                match_data = pd.read_csv(io.StringIO(match_data), low_memory=False)
                assert len(match_data) > 10
                csv_file_name = f'{directory_name}/Match Data {yesterday}.csv'
                print("Downloaded yesterday's data")
        
        match_data.to_csv(csv_file_name, index=False)
        
        return match_data


# from requests_html import HTMLSession
# from bs4 import BeautifulSoup
# session = HTMLSession()
# response = session.get('https://client.finestardiamonds.com/')
# response.html.render() # ye line jaruri h taki javascript load ho jaye
# soup = BeautifulSoup(response.html.raw_html, 'html.parser')
# print(soup.find_all("input", {"label":"USERNAME"}))
