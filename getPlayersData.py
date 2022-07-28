from datetime import datetime, timedelta
import os

def players_data_to_csv(data):
    now = datetime.now()
    current_date = now.strftime("%Y%m%d")
    yesterday = (now - timedelta(days=1)).strftime("%Y%m%d")
    if os.path.isfile(f'csv_files/Match Data {current_date}.csv'):
        player_filename = f"csv_files/Player Data {current_date}.csv"
    else:
        player_filename = f"csv_files/Player Data {yesterday}.csv"

    data.to_csv(player_filename, index=False)
