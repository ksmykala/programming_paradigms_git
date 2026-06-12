##Media Library Hub

This program manages a simple collection, containing songs, podcasts and audiobooks.
It load data from a given list of dictionaries, creates media objects based on those dictionaries and stores tem
in playlists. Users can view every item's information (Name, genre, length, author, episodes, chapters), calculate the total
duration of a playlist, its length and sor them by title or duration. An event bus, logs all addition to playlists, while a SCV exporter
generates a catalog of all media. The program shows inheritence, composition and design paterns like factory, obserser and strategies. All of 
it is wrapped in a single easily executable script.

##How to run?

If you have Pyton installed, then execute: "python media_library.py" in bash

OOP example: Library class has a list of Playlist objects, when the statistics function is called it checks all playlists's duration and number of items.
This keeps the code reusable after slight adjustments.

Design pattern example: The strategy pattern implemented in the playlist together with the two SortBy options. 

##Sample output returned on my personal PC

Statistics: {'total_items': 4, 'total_duration': 32954}

Log (Observer):
added:Bohemian Rhapsody
added:Blinding Lights
added:Lex Fridman #400
added:Clean Code

Sort demo (by title):
Blinding Lights | Bohemian Rhapsody | Clean Code | Lex Fridman #400

CSV Export:
type,title,duration
Song,Bohemian Rhapsody,354
Song,Blinding Lights,200
Podcast,Lex Fridman #400,7200
Audiobook,Clean Code,25200

Process finished with exit code 0