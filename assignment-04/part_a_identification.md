# Part A — Identification

## Snippet 1
**Concept:** Property / Getter (Encapsulation)
**Label:** OOP

This is a property/getter. The data members like `title`, `creator` and `duration` are marked as `protected` in the `MediaItem` class so they cant be accessed directly from outside. Instead we use getter methods like `getTitle()` and `getDuration()` to read them. This is how encapsulation works, we hide the data and only let it be read through these methods.

---

## Snippet 2
**Concept:** Composition
**Label:** OOP

The `Library` class has a vector of `Playlist` pointers inside it. So Library owns Playlist objects, it doesnt inherit from them. Same thing with `Playlist` which owns a vector of `MediaItem` pointers. This is composition, one class contains objects of another class.

---

## Snippet 3
**Concept:** Strategy Pattern
**Label:** Pattern

The `Playlist` class has a `sortStrategy` pointer. We can call `set_sort_strategy()` to set it to either `SortByTitle` or `SortByDuration`. Then when we call `items_sorted()` it uses whatever strategy is set. We can change the sorting without touching the Playlist code at all which is the whole point of the Strategy pattern.

---

## Snippet 4
**Concept:** Observer Pattern
**Label:** Pattern

The `EventBus` class has a `publish()` method. When we add an item to a Playlist it calls `eventBus->publish("item_added", ...)`. This fires and adds a log entry to the `eventLog` vector. The Playlist doesnt care about the log, it just publishes the event and whoever is listening will react to it. This is the Observer pattern.