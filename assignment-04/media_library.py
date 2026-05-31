# Overview
# Build a small Media Library Hub that:
#
# Uses inheritance (Song, Podcast, Audiobook)
# Uses composition (Playlist, Library)
# Applies four patterns: Factory Method, Observer, Strategy, Facade (CSV export uses a simple Template Method)
# Everything runnable lives in one file — no multi-file imports.

from abc import ABC, abstractmethod

# Dataset
MEDIA_DATA = [
    {"type": "song",      "title": "Bohemian Rhapsody",    "creator": "Queen",           "duration": 354,   "genre": "Rock"},
    {"type": "song",      "title": "Blinding Lights",       "creator": "The Weeknd",      "duration": 200,   "genre": "Pop"},
    {"type": "podcast",   "title": "Lex Fridman #400",      "creator": "Lex Fridman",     "duration": 7200,  "episode_number": 400},
    {"type": "audiobook", "title": "Clean Code",            "creator": "Robert Martin",   "duration": 25200, "chapters": 17},
]

# B1 — OOP hierarchy (25 points)

# MediaItem (ABC)	title, creator, duration; @abstractmethod describe()
# Validation: non-empty title/creator, duration > 0 in MediaItem.__init__.
class MediaItem(ABC):
    def __init__(self, title, creator, duration):
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        if not creator or not creator.strip():
            raise ValueError("Creator cannot be empty")

        if duration <= 0:
            raise ValueError("Duration must be greater than 0")

        self.title = title
        self.creator = creator
        self.duration = duration

    @abstractmethod
    def describe(self):
        pass

# Song	genre; describe() e.g. Song: … by … [Rock] (354s)
class Song(MediaItem):
    def __init__(self, title, creator, duration, genre):
        super().__init__(title, creator, duration)
        self.genre = genre

    def describe(self):
        return (
            f"Song: {self.title} by {self.creator} "
            f"[{self.genre}] ({self.duration}s)"
        )

# Podcast	episode_number; describe() with episode number
class Podcast(MediaItem):
    def __init__(self, title, creator, duration, episode_number):
        super().__init__(title, creator, duration)
        self.episode_number = episode_number

    def describe(self):
        return (
            f"Podcast: {self.title} by {self.creator} "
            f"(Episode {self.episode_number}) "
            f"({self.duration}s)"
        )

# Audiobook	chapters; describe() with chapter count
class Audiobook(MediaItem):
    def __init__(self, title, creator, duration, chapters):
        super().__init__(title, creator, duration)
        self.chapters = chapters

    def describe(self):
        return (
            f"Audiobook: {self.title} by {self.creator} "
            f"({self.chapters} chapters) "
            f"({self.duration}s)"
        )
# Polymorphism: In main, loop over a list of the three types and call describe() only.

# B2 — Composition (15 points)

# Playlist	add_item(item) (MediaItem only), total_duration(), __len__()
# Hook	When Playlist.add_item runs, publish("item_added", {"title": item.title})
# Pass EventBus into Playlist.__init__ (optional arg, default None = no events).

class Playlist:
    def __init__(self, event_bus=None):
        self._items = []
        self._sort_strategy = None
        self.event_bus = event_bus

    def add_item(self, item):
        if not isinstance(item, MediaItem):
            raise TypeError("Only MediaItem objects can be added")

        self._items.append(item)

        if self.event_bus:
            self.event_bus.publish(
                "item_added",
                {"title": item.title}
            )

    def total_duration(self):
        return sum(item.duration for item in self._items)

    def __len__(self):
        return len(self._items)

    # Playlist: set_sort_strategy(s), items_sorted() — does not change _items order.
    def set_sort_strategy(self, strategy):
        self._sort_strategy = strategy

    def items_sorted(self):
        if self._sort_strategy is None:
            return list(self._items)

        return self._sort_strategy.sort(self._items)

# Library	add_playlist(playlist), statistics() → {"total_items": int, "total_duration": int}
class Library:
    def __init__(self):
        self.playlists = []

    def add_playlist(self, playlist):
        if not isinstance(playlist, Playlist):
            raise TypeError("Expected Playlist")

        self.playlists.append(playlist)

    def statistics(self):
        total_items = sum(len(pl) for pl in self.playlists)
        total_duration = sum(
            pl.total_duration()
            for pl in self.playlists
        )

        return {
            "total_items": total_items,
            "total_duration": total_duration,
        }

# B4 — Observer (10 points)

# EventBus	subscribe(event, callback), publish(event, payload)
class EventBus:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event, callback):
        self._subscribers.setdefault(event, []).append(callback)

    def publish(self, event, payload):
        for callback in self._subscribers.get(event, []):
            callback(payload)

# B5 — Strategy (10 points)

# SortByTitle	sorted by title (case-insensitive)
class SortByTitle:
    def sort(self, items):
        return sorted(items, key=lambda item: item.title.lower())

# SortByDuration	sorted by duration
class SortByDuration:
    def sort(self, items):
        return sorted(items, key=lambda item: item.duration)



# B3 — Factory Method: load_items (10 points)

# def load_items(data):
def load_items(data):
    items = []

    # branch on record["type"]: song / podcast / audiobook
    for record in data:
        media_type = record["type"]

        if media_type == "song":
            item = Song(
                record["title"],
                record["creator"],
                record["duration"],
                record["genre"],
            )

        elif media_type == "podcast":
            item = Podcast(
                record["title"],
                record["creator"],
                record["duration"],
                record["episode_number"],
            )

        elif media_type == "audiobook":
            item = Audiobook(
                record["title"],
                record["creator"],
                record["duration"],
                record["chapters"],
            )

        # unknown type → ValueError
        else:
            raise ValueError(
                f"Unknown media type: {media_type}"
            )

        items.append(item)

    return items


# B6 — Template Method + Facade (15 points)
# Template Method — export catalog as CSV:

# CatalogExporter	export(rows) calls format_header() + format_rows(rows)
class CatalogExporter:
    def export(self, rows):
        return self.format_header() + self.format_rows(rows)

    def format_header(self):
        raise NotImplementedError

    def format_rows(self, rows):
        raise NotImplementedError

# Row dict for export: {"type": type(item).__name__, "title": item.title, "duration": item.duration}.
class CsvCatalogExporter(CatalogExporter):
    def format_header(self):
        return "type,title,duration\n"

    def format_rows(self, rows):
        output = ""

        for row in rows:
            output += (
                f"{row['type']},"
                f"{row['title']},"
                f"{row['duration']}\n"
            )

        return output

def run_media_hub():

# 1. load_items(MEDIA_DATA)
    items = load_items(MEDIA_DATA)

    # Polymorphism demo
    for item in items:
        print(item.describe())

# 2. one Library, one Playlist, add all items
    library = Library()


# 3. EventBus + log subscriber
    bus = EventBus()
    log = []

# lambda p: log.append(f"added:{p['title']}")
# In main, subscribe a list log with:
    bus.subscribe(
        "item_added",
        lambda p: log.append(f"added:{p['title']}")
    )

    playlist = Playlist(event_bus=bus)


    for item in items:
        playlist.add_item(item)

    library.add_playlist(playlist)

#  4. print statistics(), log, sort demo, CSV export
    # Statistics
    print(library.statistics())

    # Observer log
    print(log)

    # Strategy demo
# In main, print titles from items_sorted() after set_sort_strategy(SortByTitle()).
    playlist.set_sort_strategy(SortByTitle())

    sorted_titles = [
        item.title
        for item in playlist.items_sorted()
    ]

    print("Sorted:", " | ".join(sorted_titles))

    # CSV Export
    rows = [
        {
            "type": type(item).__name__,
            "title": item.title,
            "duration": item.duration,
        }
        for item in items
    ]
    # CsvCatalogExporter	header type,title,duration\n; body: CSV lines
    exporter = CsvCatalogExporter()

    print(exporter.export(rows))


if __name__ == "__main__":
    run_media_hub()
