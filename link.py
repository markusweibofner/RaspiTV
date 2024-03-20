#!/usr/bin/python3
# coding: utf-8

import sys
import requests

channel_links = {
    "CNN": "https://www.newslive.com/featured/cnn-live-free.html",
    "FoxNews": "https://www.newslive.com/featured/fox-news.html",
    "FoxBusiness": "https://www.newslive.com/business/fox-business-network-fbn.html",
    "CBCNews": "https://www.newslive.com/canadian-news/cbc-news.html",
    "AlJazeeraAmerica": "https://www.newslive.com/american/al-jazeera-america.html",
    "CNBC": "https://www.newslive.com/business/cnbc-live-free.html"
}

def get_channel_link(channel_name):
    if channel_name in channel_links:
        headers = {
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer RzBFAiAz_oms2E55XZ65aQfpK1vXrfMIysj2e7cu3D2YBbPWHAIhAOctdvucbpNoQV9VG9X0sd_DlRuQZxLbhsfdH2hrnE9keyJ1IjoxLCJlIjoiMjAyNC0wMS0yNVQyMzowMDowMC4wMDArMDA6MDAifQ'
        }
        response = requests.request("GET", channel_links[channel_name], headers=headers)
        data = response.text
        start = data.find("file: ")
        end = data.find(",autostart:")
        link = str(data[start + 7:end - 1])
        return link
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 link.py <channel>")
        sys.exit(1)

    channel = sys.argv[1]
    link = get_channel_link(channel)
    if link:
        print(link)
    else:
        print("Invalid channel name. Available channels: CNN, FoxNews, FoxBusiness, CBCNews, AlJazeeraAmerica, CNBC")
