# Media Library System

### 1. Project Overview

The Media Library System is a unified console application designed to catalog, manage, and analyze a dynamic collection of digital media assets like songs, podcasts, and audiobooks. It consumes raw incoming metadata streams, validates field values at runtime, organizes tracking pools using internal composition structures, and coordinates updates across the system using an event-driven architecture. The core pipeline exposes runtime algorithm modifications for sorting asset records on the fly and streamlines report generation using a consolidated operational facade.

### 2. How to Run the Project

To execute the entire media library simulation subsystem and trigger the diagnostic integration test block, run the following command in your terminal:

```bash
python media_library.py
```

### 3. OOP Example

This codebase leverages Composition to establish a clean "has-a" structural hierarchy between classes:

`Library` composed of `Playlist` objects: The `Library` class manages a dictionary collection of `Playlist` instances, delegating aggregated metric collections down to its components.

`Playlist` composed of `MediaItem` objects: A `Playlist` instance holds a dynamic array (`self._items`) containing references to concrete `MediaItem` subclasses.

```python
class Playlist:
    def __init__(self, name: str, event_bus: "EventBus" = None):
        self._name = name
        self._items = []  # Composition: Playlist manages a list of MediaItem objects
```

### 4. Design Pattern Example

**Strategy Pattern** (SortByTitle & SortByDuration)

The system uses the Strategy Pattern to decouple the sorting behavior from the Playlist context. Instead of embedding rigid conditional branches inside the playlist code, execution logic is delegated to interchangeable strategy layout workers. This allows the system to swap sorting mechanics dynamically at runtime without mutating the internal structural ordering of the asset array.

```python
# The context relies on duck-typing to run whichever strategy is loaded
def items_sorted(self) -> list:
    return self._sort_strategy.sort(self._items)
```

### 5. Sample Output

When the application's unified facade entry point executes, the console outputs the following functional verification stream:

```text
--- Running Media Hub Facade ---

[Facade Report] Library Statistics:
Total Items Count: 4 | Total Combined Duration: 32954s

[Facade Report] Log Tracker Records:
  * added:Bohemian Rhapsody
  * added:Blinding Lights
  * added:Lex Fridman #400
  * added:Clean Code

[Facade Report] Running Sort Strategies:
Alphabetical Output:
  - Blinding Lights
  - Bohemian Rhapsody
  - Clean Code
  - Lex Fridman #400

[Facade Report] Generating CSV String Compilation:
type,title,duration
Song,Blinding Lights,200
Song,Bohemian Rhapsody,354
Audiobook,Clean Code,25200
Podcast,Lex Fridman #400,7200
```