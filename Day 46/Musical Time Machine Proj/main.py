from requests import get
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# working as of 2022-03-02

base_URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? YYYY-MM-DD: ")

with get(url=base_URL + date) as response:
    soup = BeautifulSoup(response.text, 'html.parser')

raw_data = [song.getText().strip() for song in soup.find_all(name="h3", id="title-of-a-story")]
redundant_items = ["Songwriter(s):", "Producer(s):", "Imprint/Promotion Label:", "Gains in Weekly Performance",
                   "Additional Awards", "Songwriter(s): ", " Imprint/Promotion Label:", " Songwriter(s):"]
top_songs = []

for title in raw_data:
    if title in redundant_items:
        pass
    else:
        top_songs.append(title)

top_songs = top_songs[:100]  # get top 100 only

# date = "2002-08-12"
# top_songs = ['Dilemma', 'Hot In Herre', 'Complicated', 'I Need A Girl (Part Two)', 'Just A Friend 2002', 'Down 4 U', 'Hero', 'Just Like A Pill', 'Heaven', "Nothin'", "Gangsta Lovin'", 'Happy', 'No Such Thing', 'The Middle', "I'm Gonna Be Alright", 'Without Me', 'A Thousand Miles', 'Still Fly', 'Oh Boy', 'Move B***h', 'Foolish', "Cleanin' Out My Closet", 'One Last Breath', 'Soak Up The Sun', 'Addictive', 'The Good Stuff', "Why Don't We Fall In Love", 'halfcrazy', 'Courtesy Of The Red, White And Blue (The Angry American)', 'Long Time Gone', 'Love At First Sight', "Grindin'", 'Gotta Get Thru This', 'Two Wrongs', 'Wherever You Will Go', 'Unbroken', 'The One', 'By The Way', 'Blurry', 'I Miss My Friend', 'Feel It Boy', 'All You Wanted', "What's Luv?", 'Hella Good', 'Good Times', 'Wasting My Time', 'I Need A Girl (Part One)', 'I Keep Looking', 'The Impossible', 'Call Me', 'Ten Rounds With Jose Cuervo', 'If I Could Go!', 'My Neck, My Back', 'Days Go By', 'Tonight I Wanna Be Your Man', 'A Little Less Conversation', 'The Rising', 'Running Away', 'Where Are You Going', 'Baby', 'Stingy', 'Living And Living Well', 'Someone To Love You', 'Walking Away', "Burnin' Up", 'Beautiful Mess', 'Aerials', 'Out Of My Heart (Into Your Head)', 'All Eyez On Me', 'Trade It All', 'Way Of Life', 'She Was', 'Somebody Like You', 'Flake', "I Don't Have To Be Me ('til Monday)", "I'm Gonna Miss Her (The Fishin' Song)", 'Not A Day Goes By', 'Drift & Die', 'She Loves Me Not', 'In Da Wind', 'Sweetness', 'For All Time', 'Full Moon', 'I Do (Wanna Get Close To You)', 'You Know That I Love You', 'Gots Ta Be', 'Tainted', "Po' Folks", 'Hate To Say I Told You So', "Don't Mess With My Man", 'When You Lie Next To Me', 'My Heart Is Lost To You', 'What If A Woman', 'Down A** Chick', "I've Got You", 'Where Do We Go From Here', 'Quitame Ese Hombre', "Don't Say Goodbye", 'Blue Jeans', 'Gimme The Light', "Sally Kellerman, Hot Lips Houlihan in 'M*A*S*H,' Dies at 84", 'Chelsea Handler Hitting the Ski Slopes in Nothing But Her Underwear Is One Inspiring Way to Ring in 47', 'T.I. Responds To Atlanta Debate Sparked By Omeretta The Great', 'Larry David Picks Up Quaint French Normandy Cottage in Montecito', 'AMC Theatres’ Quarterly Loss Shrinks, But Still Totals $134M', 'House Passes Emmett Till Antilynching Act To Make Lynching A Federal Hate\xa0Crime', 'Nordstrom Posts Strong 4th Quarter as Strategies Kick\xa0In', 'Bob Baffert Sues Churchill Downs in Federal Court Over\xa0Suspension', 'Naya Rivera’s Family Reaches Wrongful Death Settlement to Go to Son: ‘He’s a Great Kid’', 'Follow Us', 'Have a Tip?', 'The Daily', 'Have a Tip?']
# # in order to not have to search everytime, data is fixed onto 2002-08-12, uncomment above if you want to change the date

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='c74f5b8b1f2a4be7b8a666c21a6ecf2e',
                                               client_secret='13a0655e4a2746db86a6b9b154cdb70b',
                                               redirect_uri='http://example.com',
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]

song_uris = []

for song in top_songs:
    results = sp.search(q=f"track:{song} year:{date[:4]} ", type="track")
    try:
        song_uris.append(results["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"Song {song} not available on Spotify. Skipping.")

print(song_uris)

# song_uris = ['spotify:track:14MgTooapmJdLlEMAr2zAM', 'spotify:track:2fGCHSaaAsKoWjq5jHVISe', 'spotify:track:5xEM5hIgJ1jjgcEBfpkt2F', 'spotify:track:2cxbxpHrND6i4uvUGVvC9J', 'spotify:track:1D7V22q80JaaCBS7acQc49', 'spotify:track:5Ci3b8pfpLA9Zk17qGXBCF', 'spotify:track:5li4lnRD6Hy02h2m3nlSdE', 'spotify:track:72SpPFrMYCXLB3Fbw9tEgf', 'spotify:track:18xQYPx62DwnjtOzS6zs1Z', 'spotify:track:0WgLpgUdThEpA5L5K0SKq7', 'spotify:track:6CbcdeTQKj0qTaZTt0xkdk', 'spotify:track:7k5BU3htshjw8MR5uDPHhs', 'spotify:track:3ciWav3L7wFcoFtloCCgRn', 'spotify:track:7lQ8MOhq6IN2w8EYcFNSUk', 'spotify:track:4w1lzcaoZ1IC2K5TwjalRP', 'spotify:track:563vSy3HB5NHxel1VGQCW6', 'spotify:track:5aW7s0G2rREOaIjivB53pF', 'spotify:track:0zO5wv6HN6UZ4yvXvLJJDr', 'spotify:track:6zMUIb4uce1CzpbjR3vMdN', 'spotify:track:7BMO7O7ImjV8HNTH74Tshv', 'spotify:track:1v2ECI79z8S4PQv9xYwIfU', 'spotify:track:36jSIOSE72neBbKntCthqw', 'spotify:track:1sR3kJi14jA8Gau3a0yXAo', 'spotify:track:4bnjq8zqtCnxTGxll5ezOO', 'spotify:track:3oXNIpoUMdk8qGkwCeXqGv', 'spotify:track:0M7mWKqwTIaVjYyxfZmtTa', 'spotify:track:0JiX8NsRdCHm8GliFuf97V', 'spotify:track:4urQbjpKd5HnYTSBRd7z6G', 'spotify:track:3XrvEifl0hIzgBGUa5jBLS', 'spotify:track:2HStGirSZokbjdi1xU1QCW', 'spotify:track:11PQ9qtLuvJmIriOR5SpS5', 'spotify:track:01d3sVIcCir71osKtkVvcI', 'spotify:track:0M0vszFSzqdSQTIy15XDu0', 'spotify:track:4bJygwUKrRgq1stlNXcgMg', 'spotify:track:1f2V8U1BiWaC9aJWmpOARe', 'spotify:track:0qnoS5hMZMphvKWi0D2LQh', 'spotify:track:6KUI3A3jmZ0cGLDzOT41lX', 'spotify:track:2hQ2geUnewmEA6KAnL7yjN', 'spotify:track:2eSJflipjhSKLExuSwuFrO', 'spotify:track:0bDcYZ5ZSnDcHPNvkQJ8ef', 'spotify:track:7cFpB4ozcSwXuhqjvNbrbP', 'spotify:track:6DfVCAGDC0SexF578ivy23', 'spotify:track:78xp7chb8f5zt596uB1K1e', 'spotify:track:2aBEchhqPDgnvjPhCgzHSx', 'spotify:track:1zdWyTCr75tUmAaUJ0S7wY', 'spotify:track:3H6JUtLbiZh07T7GLiuTON', 'spotify:track:2RLpFEf6d0708O7Bqhjyxg', 'spotify:track:3RwlpiM8WPPQsNrdQsQb7Y', 'spotify:track:4rr0gWiMrF4sOIefs3IEvZ', 'spotify:track:2czBvzOv3TvnyoW7Ozo7fP', 'spotify:track:1XIvKsXJ1BQq3cJz9N0kGW', 'spotify:track:15MhLnkZLJe4Z2tLISwe5k', 'spotify:track:1uVfUdVv0h9MWia3tdZo5G', 'spotify:track:77S5wtMOUOsWN5Fu7stlPS', 'spotify:track:4UYreO1MW2LCUzWhsRQCGO', 'spotify:track:2LrvK045zLQyt4s9n1QSBA', 'spotify:track:2Kld9kvWGQn4kr5KiiCsNH', 'spotify:track:5AI1TN1wwfFuHHbbVr91HR', 'spotify:track:19QT1L9qUNKHYNbYqawaX8', 'spotify:track:4Rp0ocZktktrId9nNAuOml', 'spotify:track:7kO0M0CPH66v0L2eLoVUaF', 'spotify:track:0rHehT9M8peRzeV1O1FeOk', 'spotify:track:7Ab9BFVAgS4waaYB5tFQzy', 'spotify:track:4UlIJjRM33esbMS6RiA4yX', 'spotify:track:4tZdPxjFCZepceY2iuoeKp', 'spotify:track:0b9djfiuDIMw1zKH6gV74g', 'spotify:track:58MQ1mQRr7upijfSrVvtSr', 'spotify:track:5v1bA7NmQcQHvH9IDkeeF4', 'spotify:track:5AVf3DkEFQvqZBfwljej8O', 'spotify:track:0RKvPOuH9vEsDrLrg9ejZ9', 'spotify:track:1eRgyfyizDWISeS99kwLNC', 'spotify:track:4TJ56OkWrnf2fv2a6T69DL', 'spotify:track:0oDXKcNWPPF4343JXsX0Zj', 'spotify:track:0TDzOOO5nRZu8nxOw0EEF4', 'spotify:track:6QxuZMdsElzjC1NnXUfl8c', 'spotify:track:1gf5KKoAbd1vUWwRKzeXF3', 'spotify:track:5QiTs0egWAq0k2O8HWKoEP', 'spotify:track:63MKNIWCCxtqnehwFhmYqp', 'spotify:track:6tc2nHTmQjXQXo2ybeVZB7', 'spotify:track:22F01qwlQDpxjPN8UQFz8n', 'spotify:track:6azyEn0aqmnDZHLm750I9J', 'spotify:track:4xrbZOEUfcn0P8mUa3X8kP', 'spotify:track:2qYj4wRMxF1p6eHvl6EmRv', 'spotify:track:0iU9Qfn7hoJHbBleOaMOAt', 'spotify:track:2SQzE9AvTi4LyPGbbSkoCn', 'spotify:track:43KalLJBA0ucHM81xfImY1', 'spotify:track:3SCVtAJq8li6HlKfM4M08u', 'spotify:track:6QGKwSp0UNrmgN3HfVPuzY', 'spotify:track:2iyStvIv0hhf8FBLrcOlq9', 'spotify:track:5y5h5PnCZCTXwClLl05xve', 'spotify:track:2iyStvIv0hhf8FBLrcOlq9']
# # Once again, very slow to rerun the above code everytime, comment out if you change the date

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard Top 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
