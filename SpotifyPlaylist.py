import sys
import spotipy
import spotipy.util as util

# Information needed to receive token to interact w/ Spotify API
# Sterilized for opsec
username = "username"
playlist_id = "playlist-id"
scope = "playlist-modify-private, playlist-modify-public"
client_id = "client_id"
client_secret = "client_secret"
redirect_uri = "https://localhost:8080"

def getSongURIs(artist, song_count=1):
	# Method returns top 3 songs from artist
	songIds = []
	results = sp.search(q='artist:' + artist, type='artist', limit=1)

	if results['artists']['total']:
		# Gives us the artist's tracks and the length of that list
		artist_id = results['artists']['items'][0]['id']
		topTracks = sp.topTracks(artist_id)
		length = len(topTracks['tracks'])
	else:
		#Prints the name of an artist if they are not on Spotify
		print(artist)
		return songIds

	# Adds the song URIs to our array before exiting the method
	for x in range(0, length if song_count > length else song_count):
		songIds.append(artist_top_tracks['tracks'][x]['id'])


	return songIds

def createPlaylist():
	trackIds = []
	artists = [
		'BTS', 
		'BLACKPINK',
		'iKON',
		'NCT 127',
		'DEAN',
		'Woodie Gochild',
		'MINO',
		'EXO',
		'NCT DREAM',
		'PENTAGON',
		'MOMOLAND',
		'JENNIE',
		'NCT U',
		'Jay Park',
		'SEVENTEEN',
		'MONSTA X',
		'SHINee', 
		'TWICE', 
		'RM',
		'Stray Kids',
		'DAY6',
		'The Rose',
		'[STATION]',
		'offonoff',
		'ATEEZ',
		'San E',
		'Jackson Wang',
		'DPR LIVE',
		'GOT7']

	# Loops through the list of artist names
	for i, currentArtist in enumerate(artists):
		addLimit = 100
		songLimit = 3

		# Calls the first method we defined for each artist in our list "artists"
		topSongs = getSongURIs(currentArtist, songLimit)
		trackIds.extend(topSongs) #Changed to extend method, .append() caused problems if songIds was empty when artist was not on Spotify


	# Adding our limit of 100 songs to the playlist using the method from spotipy passing in our list of song URIs
	if len(trackIds) + songLimit > addLimit or (i == len(artists)-1 and len(trackIds)):
		sp.user_playlist_add_tracks(user=username, playlist_id=playlist_id, tracks=trackIds)
		
	# After the playlist is created we clear the array
	trackIds = []

# Prompts spotify for a token to interact with the API based on the following credentials
# Spotify will ask you to provide the URL you are redirected to as a verification measure. This is set in your project page on the Spotify developer's site
token = util.prompt_for_user_token(username, 
								scope, 
								client_id,
								client_secret,
								redirect_uri)

# If token is validated then the main application logic executes with the below method call
if token:
	sp = spotipy.Spotify(auth=token)
	createPlaylist()
else:
	print("Can't get token for", username)