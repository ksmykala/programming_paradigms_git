"""
media_library.py
A simple media library demonstrating OOP, composition, factory, observer, strategy,
template method, and facade patterns.
"""

from abc import ABC, abstractmethod

# ========== B1 – OOP Hierarchy ==========

class Media(ABC):
    """Abstract base class for all media items."""
    def __init__(self, title: str, creator: str, duration: int):
        # validation
        if not title:
            raise ValueError("Title cannot be empty")
        if not creator:
            raise ValueError("Creator cannot be empty")
        if duration <= 0:
            raise ValueError("Duration must be positive")
        self.title = title
        self.creator = creator
        self.duration = duration

    @abstractmethod
    def describe(self) -> str:
        """Return a formatted description."""
        pass

class Song(Media):
    def __init__(self, title: str, creator: str, duration: int, genre: str):
        super().__init__(title, creator, duration)
        self.genre = genre

    def describe(self) -> str:
        return f"Song: {self.title}, by {self.creator}, {self.genre}, ({self.duration}s)"

class Podcast(Media):
    def __init__(self, title: str, creator: str, duration: int, episode_number: int):
        super().__init__(title, creator, duration)
        self.episode_number = episode_number

    def describe(self) -> str:
        return f"Podcast: {self.title}, by {self.creator}, Episode {self.episode_number} ({self.duration}s)"

class Audiobook(Media):
    def __init__(self, title: str, creator: str, duration: int, chapters: int):
        super().__init__(title, creator, duration)
        self.chapters = chapters

    def describe(self) -> str:
        return f"Audiobook: {self.title}, by {self.creator}, Chapters: {self.chapters} ({self.duration}s)"

# ========== B2 – Composition ==========

class Playlist:
    """A playlist that holds Media items. Optionally uses an EventBus for notifications."""
    def __init__(self, name: str, event_bus=None):
        self.name = name
        self._items = []
        self._event_bus = event_bus      # for Observer pattern
        self._sort_strategy = None       # for Strategy pattern

    def add_item(self, item):
        if not isinstance(item, Media):
            raise TypeError("Item must be a Media subclass")
        self._items.append(item)
        if self._event_bus:
            self._event_bus.publish("item_added", {"title": item.title})

    def total_duration(self) -> int:
        return sum(item.duration for item in self._items)

    def __len__(self) -> int:
        return len(self._items)

    def set_sort_strategy(self, strategy):
        """Set the sorting strategy (e.g., SortByTitle, SortByDuration)."""
        self._sort_strategy = strategy

    def items_sorted(self):
        """Return a new sorted list without changing the original order."""
        if self._sort_strategy is None:
            return self._items.copy()
        return self._sort_strategy.sort(self._items)

class Library:
    """A collection of playlists."""
    def __init__(self):
        self._playlists = []

    def add_playlist(self, playlist):
        if not isinstance(playlist, Playlist):
            raise TypeError("Playlist must be a Playlist instance")
        self._playlists.append(playlist)

    def statistics(self) -> dict:
        total_items = 0
        total_duration = 0
        for pl in self._playlists:
            total_items += len(pl)
            total_duration += pl.total_duration()
        return {"total_items": total_items, "total_duration": total_duration}

# ========== B3 – Factory Method ==========

def load_items(data):
    """Create Media objects from a list of dictionaries."""
    items = []
    for record in data:
        media_type = record.get("type")   # avoid using 'type' as variable name
        if media_type == "song":
            obj = Song(
                title=record["title"],
                creator=record["creator"],
                duration=record["duration"],
                genre=record["genre"]
            )
        elif media_type == "podcast":
            obj = Podcast(
                title=record["title"],
                creator=record["creator"],
                duration=record["duration"],
                episode_number=record["episode_number"]
            )
        elif media_type == "audiobook":
            obj = Audiobook(
                title=record["title"],
                creator=record["creator"],
                duration=record["duration"],
                chapters=record["chapters"]
            )
        else:
            raise ValueError(f"Unknown media type: {media_type}")
        items.append(obj)
    return items

# ========== B4 – Observer ==========

class EventBus:
    """Simple event bus for publish‑subscribe (Observer pattern)."""
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event: str, callback):
        if event not in self._subscribers:
            self._subscribers[event] = []
        self._subscribers[event].append(callback)

    def publish(self, event: str, payload):
        for callback in self._subscribers.get(event, []):
            callback(payload)

# ========== B5 – Strategy ==========

class SortByTitle:
    @staticmethod
    def sort(items):
        return sorted(items, key=lambda item: item.title.lower())

class SortByDuration:
    @staticmethod
    def sort(items):
        return sorted(items, key=lambda item: item.duration)

# ========== B6 – Template Method + Facade ==========

class CatalogExporter(ABC):
    """Template Method: export rows (list of dicts) in a specific format."""
    def export(self, rows):
        result = self.format_header()
        result += self.format_rows(rows)
        return result

    @abstractmethod
    def format_header(self) -> str:
        pass

    @abstractmethod
    def format_rows(self, rows) -> str:
        """Format each row as a string (concatenated)."""
        pass

class CsvCatalogExporter(CatalogExporter):
    """Concrete exporter: CSV format."""
    def format_header(self) -> str:
        return "type,title,duration\n"

    def format_rows(self, rows) -> str:
        lines = []
        for row in rows:
            lines.append(f"{row['type']},{row['title']},{row['duration']}")
        return "\n".join(lines) + "\n"   # add final newline

# ========== Facade ==========

def run_media_hub():
    """Orchestrate the whole media library flow (Facade pattern)."""
    # 1. Load media items
    all_items = load_items(MEDIA_DATA)

    # 2. Create Library and a Playlist, add all items
    lib = Library()
    playlist = Playlist("All Media")
    for item in all_items:
        playlist.add_item(item)
    lib.add_playlist(playlist)

    # 3. EventBus and log subscriber (Observer demo)
    event_bus = EventBus()
    log = []
    event_bus.subscribe("item_added", lambda payload: log.append(f"added:{payload['title']}"))

    # Create a playlist that publishes events to fill the log
    log_playlist = Playlist("Logged Playlist", event_bus=event_bus)
    for item in all_items:
        log_playlist.add_item(item)   # each add triggers a log entry

    # 4. Output statistics, log, sorting demo, and CSV export
    stats = lib.statistics()
    print(f"Statistics: {stats}")

    print("\nLog (Observer):")
    for entry in log:
        print(entry)

    print("\nSort demo (by title):")
    playlist.set_sort_strategy(SortByTitle())
    sorted_items = playlist.items_sorted()
    titles = [item.title for item in sorted_items]
    print(" | ".join(titles))

    # Prepare rows for CSV export
    rows = []
    for item in all_items:
        rows.append({
            "type": type(item).__name__,
            "title": item.title,
            "duration": item.duration
        })
    exporter = CsvCatalogExporter()
    csv_output = exporter.export(rows)
    print("\nCSV Export:")
    print(csv_output, end="")

# ========== Data ==========

MEDIA_DATA = [
    {"type": "song",      "title": "Bohemian Rhapsody",    "creator": "Queen",           "duration": 354,   "genre": "Rock"},
    {"type": "song",      "title": "Blinding Lights",       "creator": "The Weeknd",      "duration": 200,   "genre": "Pop"},
    {"type": "podcast",   "title": "Lex Fridman #400",      "creator": "Lex Fridman",     "duration": 7200,  "episode_number": 400},
    {"type": "audiobook", "title": "Clean Code",            "creator": "Robert Martin",   "duration": 25200, "chapters": 17},
]

# ========== Run the facade ==========
if __name__ == "__main__":
    run_media_hub()