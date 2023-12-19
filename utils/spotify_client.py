import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from pytube import YouTube


# Replace with your credentials from the Spotify Developer Dashboard
client_id = "9646598c63ff43eb8e2ffd5fb5795bad"
client_secret = "ec640fe832f54858994183a25f0d69b3"
redirect_uri = "http://localhost:5444"  # Set this in the Developer Dashboard as well


def get_tracks():
    # Replace with your credentials from the Spotify Developer Dashboard
    client_id = "9646598c63ff43eb8e2ffd5fb5795bad"
    client_secret = "ec640fe832f54858994183a25f0d69b3"
    redirect_uri = (
        "http://localhost:5444"  # Set this in the Developer Dashboard as well
    )

    # Create a SpotifyOAuth instance to get the access token
    sp_oauth = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="playlist-read",
    )

    # Get the access token
    access_token = sp_oauth.get_access_token(as_dict=False)
    # Create a Spotipy instance using the access token
    sp = spotipy.Spotify(auth=access_token)
    playlists = sp.current_user_playlists(limit=1)

    list_of_songs = []
    songs = {}
    print("lazar")
    # go through all the playlists and get the tracks and add them to a list of dictionaries
    for playlist in playlists["items"]:
        for track in sp.playlist_tracks(playlist["id"])["items"]:
            songs["author"] = track["track"]["album"]["artists"][0]["name"]
            songs["title"] = track["track"]["album"]["name"]
            list_of_songs.append(songs.copy())

    return list_of_songs


def stream_to_buffer(buffer, youtube_url):
    youtube = YouTube(youtube_url)
    audio_stream = youtube.streams.filter(only_audio=True).first()

    if audio_stream:
        audio_stream.stream_to_buffer(buffer)


def audio_from_buffer(buffer):
    buffer.seek(0)
    data = buffer.read(1024)
    while data:
        yield data
        data = buffer.read(1024)
