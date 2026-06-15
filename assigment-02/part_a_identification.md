Snippet 1 (OOP) — property / validation
@property
def title(self):
    return self._title

Read-only
OOP
Provides read-only access to internal _title

Snippet 2 (OOP) — composition
class Library:
    def __init__(self, name):
        self._playlists = {}

    def add_playlist(self, playlist):
        self._playlists[playlist.name] = playlist

Menager
OOP
class Libary manages Playlist objets useing dictionary.

Snippet 3 (Pattern) — Strategy
def items_sorted(self):
    return self._sort.sort(self._items)

One Responsibility principle
Pattern
a special class for sorting objects

Snippet 4 (Pattern) — Observer
def publish(self, event_name, payload):
    for callback in self._subscribers.get(event_name, []):
        callback(payload)

Observer
Pattern
enables event‑driven communication without coupling between components
