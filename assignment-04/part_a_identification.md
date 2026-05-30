Part A — Identification
File: part_a_identification.md

For each snippet: name the OOP concept or pattern, label OOP or Pattern, write 1–2 sentences.

Snippet 1 (OOP) — property / validation

    @property
    def title(self):
        return self._title

Name: Property 
Label: OOP
The "@property" makes "title" accessible like an attribute while actually calling the method. 
In this snippet, accessing "title" returns the value stored in the protected attribute "_title".
(Note: There is no validation only getters in this snippet, so I will only use the property "hint" of the "Snippet 1 (OOP) — property / validation" title.)

Snippet 2 (OOP) — composition

    class Library:
        def __init__(self, name):
            self._playlists = {}

        def add_playlist(self, playlist):
            self._playlists[playlist.name] = playlist

Name: Composition
Label: OOP
The "Library" object stores "Playlist" objects in its "_playlists" dictionary through the "add_playlist()" method. 
This shows composition because a library contains and manages multiple "Playlist" objects as part of its internal structure.

Snippet 3 (Pattern) — Strategy
    
    def items_sorted(self):
        return self._sort.sort(self._items)

Name: Strategy
Label: Pattern
The "items_sorted()" method does not perform the sorting itself. 
Instead, it delegates sorting to the object stored in "self._sort", 
allowing different sorting strategies to be used without changing this method.


Snippet 4 (Pattern) — Observer

    def publish(self, event_name, payload):
        for callback in self._subscribers.get(event_name, []):
            callback(payload)

Name: Observer
Label: Pattern
The "publish()" method loops through all callbacks associated with a specific event and calls each one with the event data. 
This allows multiple observers to be notified whenever that event is published.
