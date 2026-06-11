from abc import ABC, abstractmethod

MEDIA_DATA = [
    {"type": "song",      "title": "Bohemian Rhapsody",    "creator": "Queen",           "duration": 354,   "genre": "Rock"},
    {"type": "song",      "title": "Blinding Lights",       "creator": "The Weeknd",      "duration": 200,   "genre": "Pop"},
    {"type": "podcast",   "title": "Lex Fridman #400",      "creator": "Lex Fridman",     "duration": 7200,  "episode_number": 400},
    {"type": "audiobook", "title": "Clean Code",            "creator": "Robert Martin",   "duration": 25200, "chapters": 17},
]


class MediaItem(ABC):
    def __init__(self, title: str, creator: str, duration: int):
        if not title or not creator:
            raise ValueError("Title and creator must be non‑empty strings.")
        if duration <= 0:
            raise ValueError("Duration must be positive.")
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
    def describe(self) -> str:
        pass


class Song(MediaItem):
    def __init__(self, title, creator, duration, genre):
        super().__init__(title, creator, duration)
        self.genre = genre

    def describe(self):
        return f"Song: {self.title} by {self.creator} [{self.genre}] ({self.duration}s)"


class Podcast(MediaItem):
    def __init__(self, title, creator, duration, episode_number):
        super().__init__(title, creator, duration)
        self.episode_number = episode_number

    def describe(self):
        return f"Podcast: {self.title} by {self.creator} (Ep. {self.episode_number}) ({self.duration}s)"


class Audiobook(MediaItem):
    def __init__(self, title, creator, duration, chapters):
        super().__init__(title, creator, duration)
        self.chapters = chapters

    def describe(self):
        return f"Audiobook: {self.title} by {self.creator} ({self.chapters} chapters) ({self.duration}s)"


class EventBus:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event_name, callback):
        self._subscribers.setdefault(event_name, []).append(callback)

    def publish(self, event_name, payload):
        for callback in self._subscribers.get(event_name, []):
            callback(payload)


class Playlist:
    def __init__(self, name, event_bus=None):
        self.name = name
        self._items = []
        self._event_bus = event_bus
        self._sort = None

    def add_item(self, item: MediaItem):
        if not isinstance(item, MediaItem):
            raise TypeError("Only MediaItem instances can be added.")
        self._items.append(item)
        if self._event_bus:
            self._event_bus.publish("item_added", {"title": item.title})

    def total_duration(self):
        return sum(item.duration for item in self._items)

    def __len__(self):
        return len(self._items)

    def set_sort_strategy(self, strategy):
        self._sort = strategy

    def items_sorted(self):
        if self._sort is None:
            return self._items[:]
        return self._sort.sort(self._items)


class Library:
    def __init__(self, name):
        self.name = name
        self._playlists = {}

    def add_playlist(self, playlist: Playlist):
        self._playlists[playlist.name] = playlist

    def statistics(self):
        total_items = sum(len(p) for p in self._playlists.values())
        total_duration = sum(p.total_duration() for p in self._playlists.values())
        return {"total_items": total_items, "total_duration": total_duration}


class SortByTitle:
    @staticmethod
    def sort(items):
        return sorted(items, key=lambda x: x.title.lower())


class SortByDuration:
    @staticmethod
    def sort(items):
        return sorted(items, key=lambda x: x.duration)


class CatalogExporter:
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
        lines = []
        for r in rows:
            lines.append(f"{r['type']},{r['title']},{r['duration']}")
        return "\n".join(lines)


def load_items(data):
    items = []
    for record in data:
        t = record["type"]
        if t == "song":
            items.append(Song(record["title"], record["creator"], record["duration"], record["genre"]))
        elif t == "podcast":
            items.append(Podcast(record["title"], record["creator"], record["duration"], record["episode_number"]))
        elif t == "audiobook":
            items.append(Audiobook(record["title"], record["creator"], record["duration"], record["chapters"]))
        else:
            raise ValueError(f"Unknown media type: {t}")
    return items


def run_media_hub():
    # 1. Load items
    items = load_items(MEDIA_DATA)

    # 2. Polymorphic describe loop
    for item in items:
        print(item.describe())

    # 3. Create library, playlist, event bus and log subscriber
    event_bus = EventBus()
    log = []
    event_bus.subscribe("item_added", lambda p: log.append(f"added:{p['title']}"))

    playlist = Playlist("Favorites", event_bus=event_bus)
    for item in items:
        playlist.add_item(item)

    library = Library("My Library")
    library.add_playlist(playlist)

    # 4. Print statistics
    print(library.statistics())

    # 5. Print event log
    print(log)

    # 6. Strategy demo: sort by title
    playlist.set_sort_strategy(SortByTitle())
    sorted_titles = [item.title for item in playlist.items_sorted()]
    print("Sorted:", " | ".join(sorted_titles))

    # 7. CSV export via facade (Template Method)
    rows = [{"type": type(item).__name__, "title": item.title, "duration": item.duration} for item in items]
    exporter = CsvCatalogExporter()
    csv_output = exporter.export(rows)
    print(csv_output)


if __name__ == "__main__":
    run_media_hub()
