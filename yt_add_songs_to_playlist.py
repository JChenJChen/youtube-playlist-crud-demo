# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import time
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]  
scopes = ["https://www.googleapis.com/auth/youtube"]

def main(videoIds):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = os.environ['CLIENT_SECRET_FILEPATH']

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    for videoId in videoIds:
        request = youtube.playlistItems().insert(
            part="snippet",
            key='KEY',
            body={
              'snippet': {
                  'playlistId': 'PLAYLIST-ID',
                  'resourceId': {
                      'kind': 'youtube#video',
                      'videoId': videoId
                  },
                  'position': 0
              }
            }
        )
        response = request.execute()

        print(response)


def videoIds_to_add():
    return [
        "videoID_1",
        "videoID_2",
    ]

if __name__ == "__main__":
    videoIds = videoIds_to_add()
    main(videoIds)
    # time.sleep(2)