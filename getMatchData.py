import requests
from datetime import datetime
import io
import pandas as pd

class MatchData:
    def __init__(self):
        self.now = datetime.now()

    def get_path(self):
        # original csv file path
        # "https://oracleselixir-downloadable-match-data.s3-us-west-2.amazonaws.com/2022_LoL_esports_match_data_from_OraclesElixir_20220721.csv"
        # generating an automated request url
        aws_path = "https://oracleselixir-downloadable-match-data.s3-us-west-2.amazonaws.com/"

        # dealing with date patterns
        year = self.now.strftime("%Y")
        current_date = self.now.strftime("%Y%m%d")

        name = "_LoL_esports_match_data_from_OraclesElixir_"

        generated_path = f"{aws_path}{year}{name}{current_date}.csv"
        return generated_path

    def get_data(self, url):
        try:
            response = requests.get(url, allow_redirects=True)
            return response.content.decode("utf-8")

        except Exception as err:
            print(f"There was error while getting the match data. The error message is {err}")



data_instance = MatchData()
url = data_instance.get_path()
match_data = data_instance.get_data(url)

csv_data = pd.read_csv(io.StringIO(match_data), low_memory=False)
directory_name = "csv_files/"
csv_file_name = f'{directory_name}Match Data {datetime.now().strftime("%d_%m_%Y")}.csv'
# Dumping the dataframe into csv file
csv_data.to_csv(csv_file_name, index=False)

