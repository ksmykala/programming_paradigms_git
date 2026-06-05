Part C — README (10 points)
File: README.md

# Media Library Hub

## Overview

This project implements a simple Media Library Hub in Python. 
It loads songs, podcasts, and audiobooks from a dataset, stores them in a playlist and library, 
and demonstrates object-oriented programming concepts such as inheritance, polymorphism, and composition. 
The program also uses several design patterns, including Factory Method, Observer, Strategy, Facade, 
and a simple Template Method for CSV export.

## How to run: python media_library.py

Run the program from the project directory:

```bash
python media_library.py
```

## OOP Example

Inheritance is used through the `MediaItem` abstract base class. 
The `Song`, `Podcast`, and `Audiobook` classes inherit from `MediaItem` and provide their own implementation of the `describe()` method. 
This allows polymorphic calls to `describe()` without checking the object type.

## Pattern Example

The Strategy pattern is implemented by the `SortByTitle` and `SortByDuration` classes. 
A `Playlist` can switch sorting behavior by calling `set_sort_strategy()`, 
and `items_sorted()` uses the selected strategy to return a sorted list.

## Sample Output

```text
Song: Bohemian Rhapsody by Queen [Rock] (354s)
Song: Blinding Lights by The Weeknd [Pop] (200s)
Podcast: Lex Fridman #400 by Lex Fridman (Episode 400) (7200s)
Audiobook: Clean Code by Robert Martin (17 chapters) (25200s)

{'total_items': 4, 'total_duration': 32954}

['added:Bohemian Rhapsody', 'added:Blinding Lights', 'added:Lex Fridman #400', 'added:Clean Code']

Sorted: Blinding Lights | Bohemian Rhapsody | Clean Code | Lex Fridman #400
```