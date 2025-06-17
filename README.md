# youtube-playlist-crud-demo

Description:

Tooling that performs CRUD operations on Youtube resources --
Currently implemented:

- insert list of YTvideos to a YT playlist


## yt_add_songs_to_playlist.py

### Directions

1. install poetry &rarr; `sudo apt install python3-poetry`
2. poetry shell
3. python3 yt_add_songs_to_playlist.py
4. go to auth URL to login and get code to enter into terminal prom

#### Set Points

1. CLIENT_SECRET_FILEPATH environment variable
2. List of Youtube VideoIds in Videos_to_add()
3. videoId in videoIds FOR loop:
   1. key
   2. body.PlaylistId
   3. body.position -- position in YT playlist to insert video
4. toggle on/off time.sleep(2)

## REFs
(Demo repo of youtube_playlist_gen)