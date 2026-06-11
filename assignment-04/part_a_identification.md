# Part A — Identification

## Snippet 1
- **Concept/Pattern**: Encapsulation
- **Label**: OOP  
- **Explanation**: The `@property` decorator lets`title`, be accesible as a normal attribute while actually being a method. This access can help with validation if it is added.

## Snippet 2
- **Concept/Pattern**: Composition  
- **Label**: OOP  
- **Explanation**: The `Library` class holds a collection of `Playlist` objects in a "dictionary". This relation lets the class use objects behaviours without any inheritance.

## Snippet 3
- **Concept/Pattern**: Strategy Pattern  
- **Label**: Pattern  
- **Explanation**: The sorting logic is handed off to a `_sort` object. The `items_sorted` method doesn't need to know the algorithm, and the sorting approach can be changed when ran.

## Snippet 4
- **Concept/Pattern**: Observer Pattern  
- **Label**: Pattern  
- **Explanation**: The `publish` method loops through all callbacks registered for a specific event and invokes them. This makes the code events independent from the reacting code.
