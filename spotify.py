
import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def read_json(file_name):
    """Reads the spotify.json file and returns a dictionary."""
    with open(file_name, 'r') as f:
        return json.load(f)

def get_codes(arr, service):
    """Returns a list of the spotify codes."""
    arr = arr['{}'.format(service)]
    return arr['client_id'], arr['client_secret']

def set_environ(env_var, env_val):  
    """Sets the environment variable to the value provided."""
    os.environ[env_var] = env_val

def initiate():
    """Initiates the spotify environment."""
    client_id, client_secret = get_codes(read_json('codes.json'), 'Spotify')
    set_environ('SPOTIPY_CLIENT_ID', client_id)
    set_environ('SPOTIPY_CLIENT_SECRET', client_secret)
    set_environ('SPOTIPY_REDIRECT_URI', "'http://localhost/'")


def get_playlists():
    # Shows a user's playlists (need to be authenticated via oauth)

    import sys
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth

    
    username = '9xwmfey49bdh2v0l46nm7w0l0'
    

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

    playlists = sp.user_playlists(username)

    for playlist in playlists['items']:
        print(playlist['name'])

def current_playing():
    """Returns the current playing song."""
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    user = sp.user('9xwmfey49bdh2v0l46nm7w0l0')
    print(dir(user))
    current = user.currently_playing()
    if current:
        return current
    else:
        return None

if __name__ == '__main__':
    initiate()
        
    print(get_playlists())