import requests
import re
import csv
import json

def send_request(start):
    response = requests.get(
        url='https://app.scrapingbee.com/api/v1/',
        params={
            'api_key': 'TOIANLB7XTG3OIHLBQW6MKKY9ODG2PMG1X02QXMTYVA2K8EQSLTJ7VUATT9J2238Y5UFI8ES4NB36XRN',
            'url': f'https://www.google.com/search?q=site%3Ayoutube.com+openinapp.co&oq=site%3Ayoutube.com+openinapp.co&aqs=chrome.0.69i59j69i58.1898j0j1&sourceid=chrome&ie=UTF-8&start={start}',
            'custom_google': 'True'
        },
    )
    print('Response HTTP Status Code:', response.status_code)
    #print('Response HTTP Response Body:', response.content.decode('utf-8'))

    # Extract YouTube channel links using regular expressions
    youtube_channel_links = re.findall(r'(?:https?://)?(?:www\.)?youtube\.com/channel/[\w-]+', response.text)
    print('YouTube Channel Links:')
    for link in youtube_channel_links:
        print(link)

    return youtube_channel_links

all_links = []
start = 0
while len(all_links) < 10000:
    youtube_links = send_request(start)
    all_links.extend(youtube_links)
    start += 10
    if len(youtube_links) == 0:
        break

# Save YouTube channel links to CSV file
with open('youtube_channels.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['YouTube Channel Links'])
    writer.writerows([[link] for link in all_links])
print('YouTube channel links saved to youtube_channels.csv')

# Save YouTube channel links to JSON file
data = {'YouTube Channel Links': all_links}
with open('youtube_channels.json', 'w') as json_file:
    json.dump(data, json_file)
print('YouTube channel links saved to youtube_channels.json')
