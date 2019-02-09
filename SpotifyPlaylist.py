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

def get_top_songs_for_artist(artist, song_count=1):
	# Method returns top 3 songs from artist
	song_ids = []
	artist_results = sp.search(q='artist:' + artist, type='artist', limit=1)

	if artist_results['artists']['total']:
		# Gives us the artist's tracks and the length of that list
		artist_id = artist_results['artists']['items'][0]['id']
		artist_top_tracks = sp.artist_top_tracks(artist_id)
		artist_top_tracks_length = len(artist_top_tracks['tracks'])
	else:
		#Prints the name of an artist if they are not on Spotify
		print(artist)
		return song_ids

	# Adds the song URIs to our array before exiting the method
	for x in range(0, artist_top_tracks_length if song_count > artist_top_tracks_length else song_count):
		song_ids.append(artist_top_tracks['tracks'][x]['id'])


	return song_ids

def get_youtube_tracks():
	all_track_ids = []
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
	for i, current_artist in enumerate(artists):
		api_track_add_limit = 100
		top_song_limit_per_artist = 3

		# Calls the first method we defined for each artist in our list "artists"
		top_artist_songs = get_top_songs_for_artist(current_artist, top_song_limit_per_artist)
		all_track_ids.extend(top_artist_songs) #Changed to extend method, .append() caused problems if song_ids was empty when artist was not on Spotify


	# Adding our limit of 100 songs to the playlist using the method from spotipy passing in our list of song URIs
	if len(all_track_ids) + top_song_limit_per_artist > api_track_add_limit or (i == len(artists)-1 and len(all_track_ids)):
		sp.user_playlist_add_tracks(user=username, playlist_id=playlist_id, tracks=all_track_ids)
		
	# After the playlist is created we clear the array
	all_track_ids = []

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
	get_youtube_tracks()
else:
	print("Can't get token for", username)