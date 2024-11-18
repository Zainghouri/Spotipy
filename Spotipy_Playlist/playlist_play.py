from spotipy.oauth2 import SpotifyOAuth
import spotipy


# Set your Spotify API credentials
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
SPOTIPY_REDIRECT_URI = 'redirected uri' 

# Change the uri of playlist accoridng to your playlist uri
playlist_uri = 'spotify:playlist:1bZlEMfqTdxAjQC0fbRd9l'

# Set the scope for the Spotify API
scope = 'user-library-read playlist-read-private user-read-playback-state user-modify-playback-state'

# Authenticate with the Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

# Retrieve devices
devices = sp.devices()
if devices['devices']:
    device_id = devices['devices'][0]['id']
    print(f"Using device: {devices['devices'][0]['name']}")
else:
    print("No available devices found. Please ensure a device is active on your Spotify account.")
    GPIO.cleanup()
    exit()

try:
    while True:
            sp.start_playback(device_id=device_id, context_uri=playlist_uri)
            

except KeyboardInterrupt:
    print("Program interrupted")
finally:
    GPIO.cleanup()
    print("GPIO cleanup complete.")
