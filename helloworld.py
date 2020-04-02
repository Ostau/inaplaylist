from tekore import util, Spotify
from tekore.scope import scopes
from tekore.convert import to_uri
import time

client_id = 'bed5c285af6a46feb76b5c0a5467f991'
client_secret = '3453aeac8bd141c19856bade4c06ce21'
redirect_uri = 'http://localhost/'
scope = scopes.user_library_read + scopes.user_modify_playback_state

token = util.prompt_for_user_token(
    client_id,
    client_secret,
    redirect_uri,
    scope=scope
)

spotify = Spotify(token)

playlist = spotify.followed_playlists(limit=2).items[1]
print(playlist.primary_color)

playlist_uri = playlist.uri

for i in range(10):
    
    spotify.playback_start_context(playlist_uri, offset=i)
    time.sleep(5)
