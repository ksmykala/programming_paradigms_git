This program is designed to manage a media library: it imports music tracks, podcasts, and audiobooks based on stored data, saves them to a playlist, and calculates library statistics. It illustrates many concepts of object-oriented programming and design patterns by allowing elements to describe themselves polymorphically, sorting the playlist using interchangeable strategies, logging the addition of elements via an event bus, and exporting the catalog to a CSV file using a template method.
Translated with DeepL.com (free version)

For CMD:
python media_library.py

OOP Inheritance
Song, Podcast, and Audiobook all inherit MediaItem class. This enables polymorphism correct describe() method is called automatically based on object type.

Example Strategy
The SortByTitle and SortByDuration classes implement the Strategy pattern. Playlist.set_sort_strategy() swaps the sorting algorithm, and Playlist.items_sorted() uses the current strategy without changing the original order.

Song: Bohemian Rhapsody by Queen [Rock] (354s)
Song: Blinding Lights by The Weeknd [Pop] (203s)
Podcast: The Daily by NYT (Ep 42) [1800s]
Audiobook: 1984 by George Orwell (12 chapters) [30697s]
{'total_items': 4, 'total_duration': 33054}
['added:Bohemian Rhapsody', 'added:Blinding Lights', 'added:The Daily', 'added:1984']
Sorted: 1984 | Blinding Lights | Bohemian Rhapsody | The Daily
type,title,duration
Song,Bohemian Rhapsody,354
Song,Blinding Lights,203
Podcast,The Daily,1800
Audiobook,1984,30697

=== Code Execution Successful ===