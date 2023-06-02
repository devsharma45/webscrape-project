# webscrape-project

1. It imports necessary libraries such as `requests`, `re`, `csv`, and `json` for making HTTP requests, working with regular expressions, and handling CSV and JSON files.

2. The `send_request` function is defined to send a GET request to the ScrapingBee API. It takes a parameter `start` which specifies the starting index for pagination in Google search results.

3. Within the `send_request` function, an HTTP GET request is made to the ScrapingBee API. The API key and URL for the Google search are provided as parameters. The `custom_google` parameter is set to `'True'` to scrape Google search results.

4. The response from the ScrapingBee API is retrieved, and the HTTP status code and response body are printed.

5. Regular expressions (`re.findall`) are used to extract YouTube channel links from the response text. The extracted links are stored in the `youtube_channel_links` list and printed.

6. The `youtube_channel_links` list is returned from the `send_request` function.

7. The code then enters a loop to fetch YouTube channel links until a total of 10,000 links are obtained or there are no more links to fetch. The `send_request` function is called within the loop, with the `start` parameter incremented by 10 for each iteration.

8. The retrieved YouTube channel links are appended to the `all_links` list.

9. If no links are found in the response, the loop breaks.

10. Once the loop is complete, the code saves the YouTube channel links to a CSV file named `youtube_channels.csv`. It opens the file in write mode, writes the header row, and then writes each YouTube channel link as a separate row.

11. The code also saves the YouTube channel links to a JSON file named `youtube_channels.json`. It creates a dictionary `data` with the key `'YouTube Channel Links'` and the `all_links` list as its value. The dictionary is then dumped into the JSON file using `json.dump`.

