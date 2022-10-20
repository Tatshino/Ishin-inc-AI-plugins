import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from json_handler import *

username = spotifyUsername
playback = ""
scope = ["user-read-currently-playing", "user-modify-playback-state" , "user-read-playback-state"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotifyClientID,
                                                           client_secret=spotifyClientSecret,
                                                           redirect_uri="http://google.com/",
                                                           scope=scope))



"""results = sp.search(q='black rover', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])"""
#playback = sp.current_playback(market=None, additional_types=None)

def getCurrentPlay():
    #scope = "user-read-currently-playing"
    #scopre = "user-read-currently-playing"
    playback = sp.currently_playing(market="ZA")
    #playback = sp.current_user_playing_track('name')
    print(playback)

def nextTrack():
    #scope = "user-modify-playback-state"
    nextT = sp.next_track()

def prevTrack():
    #scope = "user-modify-playback-state"
    prevT = sp.previous_track()

def Pause():
    #scope = "user-modify-playback-state"
    sp.pause_playback()
    #sp.play

def Play():
    #scope = "user-modify-playback-state"
    sp.start_playback()
    #sp.play

def SetVolume(volume_percent):
    #scope = "user-modify-playback-state"
    sp.volume(volume_percent, device_id=None)

def Shuffle(shuffleset):
    sp.shuffle(shuffleset, device_id=None)

def Reapeat(repeatset):
    sp.repeat(repeatset)

#sp.repeat("context")
print(sp.devices)

#nextTrack()
#Pause()
#Play()
#SetVolume()
#getCurrentPlay()
#CurrentPlay()
#print(playback)
