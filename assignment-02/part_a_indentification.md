## Snippet 1 (OOP) — property / validation
@property
def title(self):
    return self._title

**Pattern**: Encapsulation
**Label**: OOP concept
**Explaination**: This snippet demostrates encapsulation by hidding the internal attribute _title behind a public getter method.

## Snippet 2 (OOP) — composition
class Library:
    def __init__(self, name):
        self._playlists = {}

    def add_playlist(self, playlist):
        self._playlists[playlist.name] = playlist

**Pattern**: Composition
**Label**: OOP concept
**Explaination**: This snippet shows compostion where the Library class "has-a" collection of Playlist objects stored inside the dictionary. Due to this composition relationship, the lifetime of these playlists is managed by the library container, building a complex object out of simpler parts.

## Snippet 3 (Pattern) — Strategy
def items_sorted(self):
    return self._sort.sort(self._items)

**Pattern**: Strategy Pattern
**Label**: Design Pattern
**Explaination**: This snippet defines a family of sorting algorithms, encapsulates each one, and make them interchangeable at runtime via self._sort. It allows the sorting behavior of items_sorted to vary independently from the class that calls it.

## Snippet 4 (Pattern) — Observer
def publish(self, event_name, payload):
    for callback in self._subscribers.get(event_name, []):
        callback(payload)

**Pattern**: Observer Pattern
**Label**: Design Pattern
**Explaination**: This snippet works like a YouTube subscription system. Instead of other parts of the app constantly checking for updates, they "subscribe" to specific events, and this code automatically sends out a notification to everyone on the list the moment an event happens.