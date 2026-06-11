# Media Library Hub

This program implements a small media library that manages different types of media items – songs, podcasts, and audiobooks. It demonstrates core object-oriented principles and common design patterns in a single runnable script. Users can load a predefined dataset, orgzanize items into playlists, receive notifications when items are added, sort the playlist, and export the catalogue as CSV.

## How to Run
Execute the script with any Python compiler or cli client:
python media_library.py
No additional dependencies are required. The script prints directly to the console.

## OOP Example – Inheritance and Polymorphism
The hierarchy is built around the abstract base class `MediaItem`, which defines shared attributes (`title`, `creator`, `duration`) and an abstract `describe()` method. Three subclasses – `Song`, `Podcast`, and `Audiobook` – each implement `describe()` with type‑specific details (genre, episode number, chapter count). In the main flow, a loop calls `describe()` on every item without knowing its  type, illustrating polymorphism.

## Design Pattern Example – Observer
The `EventBus` class implements the Observer pattern. A `Playlist` accepts an optional `EventBus` and, when `add_item` is called, publishes an `"item_added"` event. In `run_media_hub()`, a log subscriber is attached to record the title of each added item. This decouples the playlist from the logging logic and allows any number of "subscribers" to react to the same event.

## Sample Output (basically full output)
Song: Bohemian Rhapsody by Queen [Rock] (354s)
Song: Blinding Lights by The Weeknd [Pop] (200s)
Podcast: Lex Fridman #400 by Lex Fridman (Ep. 400) (7200s)
Audiobook: Clean Code by Robert Martin (17 chapters) (25200s)
{'total_items': 4, 'total_duration': 33054}
['added:Bohemian Rhapsody', 'added:Blinding Lights', 'added:Lex Fridman #400', 'added:Clean Code']
Sorted: Blinding Lights | Bohemian Rhapsody | Clean Code | Lex Fridman #400
type,title,duration
Song,Bohemian Rhapsody,354
Song,Blinding Lights,200
Podcast,Lex Fridman #400,7200
Audiobook,Clean Code,25200
