# Media Library Hub

This project implements a small Media Library Hub using Object-Oriented Programming principles and several design patterns. The application manages different types of media items including songs, podcasts, and audiobooks. Media items are loaded from a dataset, stored inside playlists, and organized within a library. The program demonstrates inheritance, composition, polymorphism, and multiple design patterns in a single Python file.

## How to Run

```bash
python3 media_library.py
```

## OOP Example

Inheritance is used through the MediaItem abstract base class. Song, Podcast, and Audiobook inherit from MediaItem and provide their own implementation of the describe() method.

Composition is used because a Library contains Playlist objects and a Playlist contains MediaItem objects.

## Pattern Example

The Factory Method pattern is implemented in the load_items() function, which creates the correct object type based on the value of record["type"].

The Observer pattern is implemented through EventBus. When an item is added to a playlist, subscribers receive an event notification.

The Strategy pattern is implemented using SortByTitle and SortByDuration classes. A playlist can switch sorting behavior without modifying its internal data.

The Template Method pattern is implemented by CatalogExporter and CsvCatalogExporter for CSV export.

The Facade pattern is implemented through run_media_hub(), which coordinates loading items, creating the library, event handling, sorting, and exporting.

## Sample Output

```text
{'total_items': 4, 'total_duration': 32954}

['added:Bohemian Rhapsody',
 'added:Blinding Lights',
 'added:Lex Fridman #400',
 'added:Clean Code']

Sorted: Blinding Lights | Bohemian Rhapsody | Clean Code | Lex Fridman #400

type,title,duration
Song,Bohemian Rhapsody,354
Song,Blinding Lights,200
Podcast,Lex Fridman #400,7200
Audiobook,Clean Code,25200
```