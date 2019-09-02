import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

client_id = '5572530ac0664df2b34373f3f41db89b'
client_secret = '15734ca0cac44e3c8ee4cc238bc895cf'
uri = 'spotify:user:22okarqslvrgo5yvlkkfvr64a:playlist:2q1iIfQJgOkHumhCQg4Hrg'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# if len(sys.argv) > 1:
#     user = sys.argv[1]



username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

results = sp.user_playlist(username, playlist_id)
results = results['tracks']['items']
# print(results[0].keys())
playlist_art = {}
playlist_uri = {}
uri_list = list()
for track in results:
    art = list()
    for artist in track['track']['artists']:
        art.append(artist['name'])
    playlist_art.update({track['track']['name'] : art})
    playlist_uri.update({track['track']['name'] : track['track']['uri']})
    uri_list.append(track['track']['uri'])

# Audio analysis Doc
# https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-analysis/#rhythm
analyze = sp.audio_analysis(playlist_uri['Loyal']) # dict_keys(['meta', 'track', 'bars', 'beats', 'tatums', 'sections', 'segments'])
analyze = analyze['bars']
# print(analyze)
# print(analyze.keys())


# Audio Features
# https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/
analy = sp.audio_features(uri_list[0])
print(analy)
