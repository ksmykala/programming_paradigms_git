from abc import ABC, abstractmethod
Media_data[
     {"type": "song",      "title": "Bohemian Rhapsody",    "creator": "Queen",           "duration": 354,   "genre": "Rock"},
    {"type": "song",      "title": "Blinding Lights",       "creator": "The Weeknd",      "duration": 200,   "genre": "Pop"},
    {"type": "podcast",   "title": "Lex Fridman #400",      "creator": "Lex Fridman",     "duration": 7200,  "episode_number": 400},
    {"type": "audiobook", "title": "Clean Code",            "creator": "Robert Martin",   "duration": 25200, "chapters": 17},
]

"""Class	Requirements
MediaItem (ABC)	title, creator, duration; @abstractmethod describe()
Song	genre; describe() e.g. Song: … by … [Rock] (354s)
Podcast	episode_number; describe() with episode number
Audiobook	chapters; describe() with chapter count

Validation: non-empty title/creator, duration > 0 in MediaItem.__init__.

Polymorphism: In main, loop over a list of the three types and call describe() only."""
"""Media Library Hub — assignment 04.

One file, no external imports. Covers:
- inheritance (MediaItem -> Song / Podcast / Audiobook)
- composition (Playlist holds items, Library holds playlists)
- Factory Method (load_items), Observer (EventBus),
  Strategy (sorters), Template Method + Facade (export / run_media_hub)
"""

from abc import ABC, abstractmethod

MEDIA_DATA = [
    {"type": "song",      "title": "Bohemian Rhapsody", "creator": "Queen",         "duration": 354,   "genre": "Rock"},
    {"type": "song",      "title": "Blinding Lights",   "creator": "The Weeknd",    "duration": 200,   "genre": "Pop"},
    {"type": "podcast",   "title": "Lex Fridman #400",  "creator": "Lex Fridman",   "duration": 7200,  "episode_number": 400},
    {"type": "audiobook", "title": "Clean Code",        "creator": "Robert Martin", "duration": 25200, "chapters": 17},
]



class MediaItem(ABC):
    """Base class for everything playable. Validates the common fields."""

    def __init__(self, title, creator, duration):
        if not title or not str(title).strip():
            raise ValueError("title must be a non-empty string")
        if not creator or not str(creator).strip():
            raise ValueError("creator must be a non-empty string")
        if not isinstance(duration, (int, float)) or duration <= 0:
            raise ValueError("duration must be a positive number")
        self._title = title
        self._creator = creator
        self._duration = duration

    @property
    def title(self):
        return self._title

    @property
    def creator(self):
        return self._creator

    @property
    def duration(self):
        return self._duration

    @abstractmethod
    def describe(self):
        """Return a one-line human readable description."""


class Song(MediaItem):
    def __init__(self, title, creator, duration, genre):
        super().__init__(title, creator, duration)
        self._genre = genre

    @property
    def genre(self):
        return self._genre

    def describe(self):
        return f"Song: {self.title} by {self.creator} [{self.genre}] ({self.duration}s)"


class Podcast(MediaItem):
    def __init__(self, title, creator, duration, episode_number):
        super().__init__(title, creator, duration)
        self._episode_number = episode_number

    @property
    def episode_number(self):
        return self._episode_number

    def describe(self):
        return (f"Podcast: {self.title} by {self.creator} "
                f"(episode {self.episode_number}, {self.duration}s)")


class Audiobook(MediaItem):
    def __init__(self, title, creator, duration, chapters):
        super().__init__(title, creator, duration)
        self._chapters = chapters

    @property
    def chapters(self):
        return self._chapters

    def describe(self):
        return (f"Audiobook: {self.title} by {self.creator} "
                f"({self.chapters} chapters, {self.duration}s)")



class EventBus:
    """Tiny pub/sub. Subscribers register callbacks per event name."""

    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event, callback):
        self._subscribers.setdefault(event, []).append(callback)

    def publish(self, event, payload):
        for callback in self._subscribers.get(event, []):
            callback(payload)



class SortByTitle:
    def sort(self, items):
        return sorted(items, key=lambda i: i.title.lower())


class SortByDuration:
    def sort(self, items):
        return sorted(items, key=lambda i: i.duration)



class Playlist:
    def __init__(self, name, event_bus=None):
        self._name = name
        self._items = []
        self._event_bus = event_bus
        self._sort = SortByTitle()  # sensible default

    @property
    def name(self):
        return self._name

    @property
    def items(self):
        return list(self._items)  # copy, so nobody mutates our internals

    def add_item(self, item):
        if not isinstance(item, MediaItem):
            raise TypeError("playlist only accepts MediaItem instances")
        self._items.append(item)
        if self._event_bus is not None:
            self._event_bus.publish("item_added", {"title": item.title})

    def total_duration(self):
        return sum(item.duration for item in self._items)

    def __len__(self):
        return len(self._items)

    # strategy hooks
    def set_sort_strategy(self, strategy):
        self._sort = strategy

    def items_sorted(self):
        # returns a new sorted list, _items keeps insertion order
        return self._sort.sort(self._items)


class Library:
    def __init__(self, name):
        self._name = name
        self._playlists = {}

    def add_playlist(self, playlist):
        self._playlists[playlist.name] = playlist

    def statistics(self):
        total_items = sum(len(p) for p in self._playlists.values())
        total_duration = sum(p.total_duration() for p in self._playlists.values())
        return {"total_items": total_items, "total_duration": total_duration}



def load_items(data):
    """Factory method: turn raw dicts into the right MediaItem subclass."""
    items = []
    for record in data:
        kind = record["type"]
        if kind == "song":
            items.append(Song(record["title"], record["creator"],
                              record["duration"], record["genre"]))
        elif kind == "podcast":
            items.append(Podcast(record["title"], record["creator"],
                                 record["duration"], record["episode_number"]))
        elif kind == "audiobook":
            items.append(Audiobook(record["title"], record["creator"],
                                   record["duration"], record["chapters"]))
        else:
            raise ValueError(f"unknown media type: {kind!r}")
    return items



class CatalogExporter:
    """Template method: export() fixes the skeleton, subclasses fill the steps."""

    def export(self, rows):
        return self.format_header() + self.format_rows(rows)

    def format_header(self):
        raise NotImplementedError

    def format_rows(self, rows):
        raise NotImplementedError


class CsvCatalogExporter(CatalogExporter):
    def format_header(self):
        return "type,title,duration\n"

    def format_rows(self, rows):
        return "\n".join(
            f"{r['type']},{r['title']},{r['duration']}" for r in rows
        )



def run_media_hub():
    """One call that wires everything together and runs the demo."""
    # 1. factory
    items = load_items(MEDIA_DATA)

    # polymorphic loop — same call, different output per subclass
    for item in items:
        print(item.describe())

    # 2-3. composition + observer
    bus = EventBus()
    log = []
    bus.subscribe("item_added", lambda p: log.append(f"added:{p['title']}"))

    playlist = Playlist("All Media", event_bus=bus)
    for item in items:
        playlist.add_item(item)

    library = Library("My Library")
    library.add_playlist(playlist)

    # 4. output
    print(library.statistics())
    print(log)

    playlist.set_sort_strategy(SortByTitle())
    print("Sorted:", " | ".join(i.title for i in playlist.items_sorted()))

    rows = [{"type": type(i).__name__, "title": i.title, "duration": i.duration}
            for i in items]
    print(CsvCatalogExporter().export(rows))


if __name__ == "__main__":
    run_media_hub()
