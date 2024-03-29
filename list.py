import requests
from bs4 import BeautifulSoup

def get_channel_list():
    url = "https://www.airtel.in/plans/dth/all-channel-list"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    channel_list = []
    channel_table = soup.find("table", {"class": "channel-list-table"})
    rows = channel_table.find_all("tr")
    
    for row in rows[1:]:
        columns = row.find_all("td")
        channel_name = columns[0].text.strip()
        channel_number = columns[1].text.strip()
        channel_list.append((channel_name, channel_number))
    
    return channel_list

channel_list = get_channel_list()
for channel in channel_list:
    print(f"Channel Name: {channel[0]}, Channel Number: {channel[1]}")