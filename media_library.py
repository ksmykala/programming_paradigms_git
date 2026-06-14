from abc import ABC, abstractmethod


MEDIA_DATA = [
    {
        "type": "song",
        "title": "Bohemian Rhapsody",
        "creator": "Queen",
        "duration": 354,
        "genre": "Rock",
    },
    {
        "type": "song",
        "title": "Blinding Lights",
        "creator": "The Weeknd",
        "duration": 200,
        "genre": "Pop",
    },
    {
        "type": "podcast",
        "title": "Lex Fridman #400",
        "creator": "Lex Fridman",
        "duration": 7200,
        "episode_number": 400,
    },
    {
        "type": "audiobook",
        "title": "Clean Code",
        "creator": "Robert Martin",
        "duration": 25200,
        "chapters": 17,
    },
]


class MediaItem(ABC):

    def __init__(self, title, creator, duration):

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
    def describe(self):
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
        return (
            f"Podcast: {self.title} by {self.creator} "
            f"(Episode {self.episode_number}) ({self.duration}s)"
        )


class Audiobook(MediaItem):

    def __init__(self, title, creator, duration, chapters):
        super().__init__(title, creator, duration)
        self.chapters = chapters

    def describe(self):
        return (
            f"Audiobook: {self.title} by {self.creator} "
            f"({self.chapters} chapters) ({self.duration}s)"
        )


class EventBus:

    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event, callback):
        self._subscribers.setdefault(event, []).append(callback)

    def publish(self, event, payload):
        for callback in self._subscribers.get(event, []):
            callback(payload)


class Playlist:

    def __init__(self, name, event_bus=None):
        self.name = name
        self._items = []
        self._event_bus = event_bus

    def add_item(self, item):

        if not isinstance(item, MediaItem):
            raise TypeError("Only MediaItem objects allowed")

        self._items.append(item)

        if self._event_bus:
            self._event_bus.publish(
                "item_added",
                {"title": item.title}
            )

    def total_duration(self):
        return sum(item.duration for item in self._items)
    def __len__(self):
        return len(self._items)

    def set_sort_strategy(self, strategy):
        self._sort = strategy

    def items_sorted(self):
        if not hasattr(self, "_sort"):
            return list(self._items)

        return self._sort.sort(self._items)
class Library:

    def __init__(self, name):
        self.name = name
        self._playlists = {}

    def add_playlist(self, playlist):
        self._playlists[playlist.name] = playlist

    def statistics(self):

        total_items = 0
        total_duration = 0

        for playlist in self._playlists.values():
            total_items += len(playlist)
            total_duration += playlist.total_duration()

        return {
            "total_items": total_items,
            "total_duration": total_duration
        }
class SortByTitle:

    def sort(self, items):
        return sorted(items, key=lambda item: item.title.lower())

class SortByDuration:

    def sort(self, items):
        return sorted(items, key=lambda item: item.duration)


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
        result = ""

        for row in rows:
            result += (
                f"{row['type']},"
                f"{row['title']},"
                f"{row['duration']}\n"
            )

        return result


def load_items(data):

    items = []

    for record in data:

        if record["type"] == "song":
            item = Song(
                record["title"],
                record["creator"],
                record["duration"],
                record["genre"]
            )

        elif record["type"] == "podcast":
            item = Podcast(
                record["title"],
                record["creator"],
                record["duration"],
                record["episode_number"]
            )

        elif record["type"] == "audiobook":
            item = Audiobook(
                record["title"],
                record["creator"],
                record["duration"],
                record["chapters"]
            )

        else:
            raise ValueError("Unknown type")

        items.append(item)

    return items
def run_media_hub():

    items = load_items(MEDIA_DATA)

    event_bus = EventBus()
    log = []

    event_bus.subscribe(
        "item_added",
        lambda p: log.append(f"added:{p['title']}")
    )

    playlist = Playlist("Favorites", event_bus)

    for item in items:
        playlist.add_item(item)

    library = Library("My Library")
    library.add_playlist(playlist)

    print(library.statistics())
    print(log)

    playlist.set_sort_strategy(SortByTitle())

    titles = [item.title for item in playlist.items_sorted()]
    print("Sorted: " + " | ".join(titles))

    exporter = CsvCatalogExporter()

    rows = [
        {
            "type": type(item).__name__,
            "title": item.title,
            "duration": item.duration
        }
        for item in items
    ]

    print()
    print(exporter.export(rows))


if __name__ == "__main__":
    run_media_hub()