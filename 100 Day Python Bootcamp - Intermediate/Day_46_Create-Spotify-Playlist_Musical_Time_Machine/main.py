from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


spotify_client_id = "" # Your ID
spotify_client_secret = "" # Your Secret
spotify_url =  'https://accounts.spotify.com/authorize'
redirect_uri = "http://example.com"

time_travel = input("What your would you like to travel to? YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{time_travel}/")
website = response.text
soup = BeautifulSoup(website, "html.parser")
all_titles = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
all_artists = soup.find_all(class_="a-truncate-ellipsis-2line")

# Get song titles and artist names
song_titles = [str(title.getText("'[]'").split()) for title in all_titles]
song_artists = [str(artist.getText("'[]'").split()) for artist in all_artists]

songs = []

for i in range(len(song_artists)):
    # get the names from list1 and list2
    name1 = song_titles[i].strip("[]'\"").replace("'", "").replace(",", "")
    name2 = song_artists[i].strip("[]'\"").replace("'", "").replace(",", "")
    
    # concatenate the names with a hyphen separator
    all_songs = songs.append(f"{name1} {' - '} {name2}")


    
# Integrating with Spotify

scope = "playlist-modify-private"

oauth_object = spotipy.SpotifyOAuth(client_id = spotify_client_id,
                                   client_secret = spotify_client_secret,
                                   redirect_uri = redirect_uri,
                                   scope = scope)


token_dict = oauth_object.get_access_token()
token = token_dict['access_token']

# Spotify Object
spotify_object = spotipy.Spotify(auth = token)

current = spotify_object.current_user()["id"]

playlists = spotify_object.current_user_playlists()

song_uris_list = []

new_playlist = spotify_object.user_playlist_create(user=current, name=f"{time_travel}", public=False, collaborative=True, description="First Playlist" )

for uris in range(len(song_artists)):
    song = spotify_object.search(q=songs[uris], limit=1, type="track", market="US")
    song_uri = song['tracks']['items'][0]['uri']
    song_uris_list.append(song_uri)
    try:
        spotify_object.playlist_add_items(playlist_id=new_playlist["id"], items=[song_uri], position=None)
    except NameError:
        print(f"Song not found. ID: {song}")

