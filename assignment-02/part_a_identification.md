# Part A — Identification
 
## Snippet 1 — Property (encapsulation) — **OOP**
 
This is the a decorator. It exposes the private attribute "_title" through a read-only getter, so outside code can do `item.title` without touching `_title` directly. this is encapsulation where you hide the real attribute and you only control the access to it.
 
## Snippet 2 — Composition — **OOP**
 
`Library` is built out of playlists . It holds them in a dictionart and manages them through `add_playlist`, instead of inheriting from some Playlist class. The library doesn't care how a playlist works internally it only cares that it just contains them.
 
## Snippet 3 — Strategy — **Pattern**
 
The sorting behavior is not hardcoded `items_sorted` delegates to whatever object is stored in `self._sort`. You can swap the sorting algorithm at runtime (by title, by duration...) without changing the Playlist class at all.
 
## Snippet 4 — Observer — **Pattern**
 
This is the publish side of Observer (pub/sub). When an event happens, the publisher loops through everyone subscribed to that event name and calls their callbacks with the payload. Subscribers don't need to know about the publisher's internals and vice versa.
 
