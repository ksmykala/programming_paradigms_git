from abc import ABC, abstractmethod

MEDIA_DATA = [
    {"type": "song", "title": "Bohemian Rhapsody", "creator": "Queen", "duration": 354, "genre": "Rock"},
    {"type": "song", "title": "Blinding Lights", "creator": "The Weeknd", "duration": 203, "genre": "Pop"},
    {"type": "podcast", "title": "The Daily", "creator": "NYT", "duration": 1800, "episode_number": 42},
    {"type": "audiobook", "title": "1984", "creator": "George Orwell", "duration": 30697, "chapters": 12},
]

class MediaItem(ABC):
    def __init__(self, title, creator, duration):
        assert title and creator and duration > 0, "Invalid media data"
        self.title, self.creator, self.duration = title, creator, duration

    @abstractmethod
    def describe(self): pass

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
        return f"Podcast: {self.title} by {self.creator} (Ep {self.episode_number}) [{self.duration}s]"

class Audiobook(MediaItem):
    def __init__(self, title, creator, duration, chapters):
        super().__init__(title, creator, duration)
        self.chapters = chapters
    def describe(self):
        return f"Audiobook: {self.title} by {self.creator} ({self.chapters} chapters) [{self.duration}s]"

class EventBus:
    def __init__(self):
        self._subs = {}
    def subscribe(self, event, cb):
        self._subs.setdefault(event, []).append(cb)
    def publish(self, event, payload):
        for cb in self._subs.get(event, []):
            cb(payload)

class SortByTitle:
    def sort(self, items): return sorted(items, key=lambda i: i.title.lower())

class SortByDuration:
    def sort(self, items): return sorted(items, key=lambda i: i.duration)

class Playlist:
    def __init__(self, name, event_bus=None):
        self.name, self._items, self._strategy, self._bus = name, [], SortByTitle(), event_bus
    def add_item(self, item):
        self._items.append(item)
        if self._bus:
            self._bus.publish("item_added", {"title": item.title})
    def total_duration(self): return sum(i.duration for i in self._items)
    def __len__(self): return len(self._items)
    def set_sort_strategy(self, s): self._strategy = s
    def items_sorted(self): return self._strategy.sort(self._items)

class Library:
    def __init__(self): self._playlists = {}
    def add_playlist(self, p): self._playlists[p.name] = p
    def statistics(self):
        return {"total_items": sum(len(p) for p in self._playlists.values()),
                "total_duration": sum(p.total_duration() for p in self._playlists.values())}

def load_items(data):
    items = []
    for r in data:
        t = r["type"]
        if t == "song":
            items.append(Song(r["title"], r["creator"], r["duration"], r["genre"]))
        elif t == "podcast":
            items.append(Podcast(r["title"], r["creator"], r["duration"], r["episode_number"]))
        elif t == "audiobook":
            items.append(Audiobook(r["title"], r["creator"], r["duration"], r["chapters"]))
        else:
            raise ValueError(f"Unknown type: {t}")
    return items

class CatalogExporter:
    def export(self, rows): return self.format_header() + self.format_rows(rows)
    def format_header(self): raise NotImplementedError
    def format_rows(self, rows): raise NotImplementedError

class CsvCatalogExporter(CatalogExporter):
    def format_header(self): return "type,title,duration\n"
    def format_rows(self, rows): return "\n".join(f"{r['type']},{r['title']},{r['duration']}" for r in rows) + "\n"

def run_media_hub():
    items = load_items(MEDIA_DATA)

    for item in items:
        print(item.describe())

    bus, log = EventBus(), []
    bus.subscribe("item_added", lambda p: log.append(f"added:{p['title']}"))
    pl = Playlist("main", bus)
    for item in items:
        pl.add_item(item)
    lib = Library()
    lib.add_playlist(pl)

    print(lib.statistics())
    print(log)

    pl.set_sort_strategy(SortByTitle())
    sorted_titles = [i.title for i in pl.items_sorted()]
    print("Sorted:", " | ".join(sorted_titles))

    rows = [{"type": type(i).__name__, "title": i.title, "duration": i.duration} for i in items]
    exporter = CsvCatalogExporter()
    print(exporter.export(rows), end="")

if __name__ == "__main__":
    run_media_hub()
