# Assignment 04 — Media Library Hub

## What the program does

This program manages a small media library in C++. It has three types of media which are songs, podcasts and audiobooks. All of them share a base class called `MediaItem`. The items are loaded from a hardcoded dataset using a factory function and then added to a `Playlist`. The playlist is stored inside a `Library`. The program also shows four design patterns: Factory Method, Observer, Strategy and Facade. There is also a CSV export feature using the Template Method pattern.

## How to run

```
clang++ -std=c++17 -o media_library media_library.cpp
./media_library
```

## OOP Example — Inheritance

`Song`, `Podcast` and `Audiobook` all inherit from `MediaItem`. The base class has the common stuff like title, creator and duration. Each subclass has its own `describe()` method that prints the info in its own way. So when we loop over all items and call `describe()`, each one prints differently depending on what type it is. This is polymorphism.

## Pattern Example — Observer

We have an `EventBus` class with `subscribe()` and `publish()`. In `run_media_hub()` we subscribe a callback to the `"item_added"` event that appends to a `log` vector. When an item is added to the playlist using `add_item()`, it calls `eventBus->publish("item_added", ...)` with a payload, and the callback runs automatically. The playlist doesnt know about the log at all, it just fires the event. This is the Observer pattern.

## Sample Output

```
Song: Bohemian Rhapsody by Queen [Rock] (354s)
Song: Blinding Lights by The Weeknd [Pop] (200s)
Podcast: Lex Fridman #400 by Lex Fridman [Episode 400] (7200s)
Audiobook: Clean Code by Robert Martin [17 chapters] (25200s)
{total_items: 4, total_duration: 32954}
['added:Bohemian Rhapsody', 'added:Blinding Lights', 'added:Lex Fridman #400', 'added:Clean Code']
Sorted: Blinding Lights | Bohemian Rhapsody | Clean Code | Lex Fridman #400
type,title,duration
Song,Bohemian Rhapsody,354
Song,Blinding Lights,200
Podcast,Lex Fridman #400,7200
Audiobook,Clean Code,25200
```