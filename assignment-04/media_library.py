# Overview
# Build a small Media Library Hub that:
#
# Uses inheritance (Song, Podcast, Audiobook)
# Uses composition (Playlist, Library)
# Applies four patterns: Factory Method, Observer, Strategy, Facade (CSV export uses a simple Template Method)
# Everything runnable lives in one file — no multi-file imports.
#
#
# Dataset
# MEDIA_DATA = [
#     {"type": "song",      "title": "Bohemian Rhapsody",    "creator": "Queen",           "duration": 354,   "genre": "Rock"},
#     {"type": "song",      "title": "Blinding Lights",       "creator": "The Weeknd",      "duration": 200,   "genre": "Pop"},
#     {"type": "podcast",   "title": "Lex Fridman #400",      "creator": "Lex Fridman",     "duration": 7200,  "episode_number": 400},
#     {"type": "audiobook", "title": "Clean Code",            "creator": "Robert Martin",   "duration": 25200, "chapters": 17},
# ]
# Only 4 records — enough to test all types without long debugging.
#
#
# Part B — Media Library Hub (75 points)
# File: media_library.py
# Time: ~90 minutes
#
# Implement all sections in one file. A if __name__ == "__main__": block at the end must run without errors.
#
# B1 — OOP hierarchy (25 points)
# Class	Requirements
# MediaItem (ABC)	title, creator, duration; @abstractmethod describe()
# Song	genre; describe() e.g. Song: … by … [Rock] (354s)
# Podcast	episode_number; describe() with episode number
# Audiobook	chapters; describe() with chapter count
# Validation: non-empty title/creator, duration > 0 in MediaItem.__init__.
#
# Polymorphism: In main, loop over a list of the three types and call describe() only.
#
# B2 — Composition (15 points)
# Class	Methods
# Playlist	add_item(item) (MediaItem only), total_duration(), __len__()
# Library	add_playlist(playlist), statistics() → {"total_items": int, "total_duration": int}
# B3 — Factory Method: load_items (10 points)
# def load_items(data):
#     # branch on record["type"]: song / podcast / audiobook
#     # unknown type → ValueError
# B4 — Observer (10 points)
# Class	Role
# EventBus	subscribe(event, callback), publish(event, payload)
# Hook	When Playlist.add_item runs, publish("item_added", {"title": item.title})
# Pass EventBus into Playlist.__init__ (optional arg, default None = no events).
#
# In main, subscribe a list log with:
# lambda p: log.append(f"added:{p['title']}")
#
# B5 — Strategy (10 points)
# Class	sort(items)
# SortByTitle	sorted by title (case-insensitive)
# SortByDuration	sorted by duration
# Playlist: set_sort_strategy(s), items_sorted() — does not change _items order.
#
# In main, print titles from items_sorted() after set_sort_strategy(SortByTitle()).
#
# B6 — Template Method + Facade (15 points)
# Template Method — export catalog as CSV:
#
# Class	Role
# CatalogExporter	export(rows) calls format_header() + format_rows(rows)
# CsvCatalogExporter	header type,title,duration\n; body: CSV lines
# Facade — one function:
#
# def run_media_hub():
#     """
#     1. load_items(MEDIA_DATA)
#     2. one Library, one Playlist, add all items
#     3. EventBus + log subscriber
#     4. print statistics(), log, sort demo, CSV export
#     """
# Row dict for export: {"type": type(item).__name__, "title": item.title, "duration": item.duration}.
#
# Expected main output shape (values may vary slightly in formatting):
#
# Song: Bohemian Rhapsody by Queen [Rock] (354s)
# ...
# {'total_items': 4, 'total_duration': 33054}
# ['added:Bohemian Rhapsody', 'added:Blinding Lights', ...]
# Sorted: Blinding Lights | Bohemian Rhapsody | ...
# type,title,duration
# Song,Bohemian Rhapsody,354
# ...
# Starter skeleton:
#
# from abc import ABC, abstractmethod
#
# MEDIA_DATA = [...]
#
#
# class MediaItem(ABC):
#     ...
#
#
# class Song(MediaItem):
#     ...
#
#
# class Podcast(MediaItem):
#     ...
#
#
# class Audiobook(MediaItem):
#     ...
#
#
# class Playlist:
#     ...
#
#
# class Library:
#     ...
#
#
# class EventBus:
#     ...
#
#
# class SortByTitle:
#     ...
#
#
# class SortByDuration:
#     ...
#
#
# class CatalogExporter:
#     ...
#
#
# class CsvCatalogExporter(CatalogExporter):
#     ...
#
#
# def load_items(data):
#     pass
#
#
# def run_media_hub():
#     pass
#
#
# if __name__ == "__main__":
#     run_media_hub()