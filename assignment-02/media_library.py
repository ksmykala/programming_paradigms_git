from abc import ABC, abstractmethod

# Complete testing dataset
MEDIA_DATA = [
    {"type": "song",      "title": "Bohemian Rhapsody",     "creator": "Queen",           "duration": 354,   "genre": "Rock"},
    {"type": "song",      "title": "Blinding Lights",       "creator": "The Weeknd",      "duration": 200,   "genre": "Pop"},
    {"type": "podcast",   "title": "Lex Fridman #400",      "creator": "Lex Fridman",     "duration": 7200,  "episode_number": 400},
    {"type": "audiobook", "title": "Clean Code",            "creator": "Robert Martin",   "duration": 25200, "chapters": 17},
]

# ================================
# B1 — OOP HIERARCHY 
# ================================

class MediaItem(ABC):       #MediaItem(ABC) -> ABC is parent class (superclass)
    """
    Abstract Base Class for all media types.
    Handles data validation and encapsulates base fields.
    """

    def __init__(self, title: str, creator: str, duration: int):    # __init__: like Constructor in C++ OOP
        # Validation rules: strings cannot be empty, duration must be positive
        if not title or not title.strip():
            raise ValueError("Title cannot be empty.")
        
        if not creator or not creator.strip():
            raise ValueError("Creator cannot be emppty.")
        
        if duration <= 0:
            raise ValueError("Duration must be grater than zero.")
        
        self._title = title                 #self: equilvalent to this pointer in C++
        self._creator = creator             #single underscore _: equil. private member in C++
        self._duration = duration

    @property                               # @: decorator, e.g: make item.title possible. Without @property, it would be item.title()
    def title(self) -> str:
        return self._title

    @property
    def creator(self) -> str:
        return self._creator

    @property
    def duration(self) -> int:
        return self._duration

    @abstractmethod
    def describe(self) -> str:
        """Polymorphic method to be implemented by child classes."""
        pass

# Depend on the media type, the corresponsing object (either Song, Podcast, or Audiobook will overwrite the parent/superclass MediaItem)
class Song(MediaItem):      # C++ equil.: class Song : public MediaItem. Song is a child class of MediaItem
    def __init__(self, title: str, creator: str, duration: int, genre: str):
        super().__init__(title, creator, duration)      # call superclass (MediaItem) constructor
        self._genre = genre                             # since Python doesn't automatically try to call the default base constructor (MediaItem()) like C++ does

    @property
    def genre(self) -> str:
        return self._genre

    def describe(self) -> str:
        return f"Song: {self.title} by {self.creator} [{self.genre}] ({self.duration}s)"

class Podcast(MediaItem):
    def __init__(self, title: str, creator: str, duration: int, episode_number: int):
        super().__init__(title, creator, duration)
        self._episode_number = episode_number

    @property
    def episode_number(self) -> int:
        return self._episode_number

    def describe(self) -> str:
        return f"Podcast: {self.title} by {self.creator} [Episode {self.episode_number}] ({self.duration}s)"


class Audiobook(MediaItem):
    def __init__(self, title: str, creator: str, duration: int, chapters: int):
        super().__init__(title, creator, duration)
        self._chapters = chapters

    @property
    def chapters(self) -> int:
        return self._chapters

    def describe(self) -> str:
        return f"Audiobook: {self.title} by {self.creator} [{self.chapters} Chapters] ({self.duration}s)"   

# ================================
# B2 — COMPOSITION 
# ================================     
# Library "has-a" Playlist objects. Each Playlist object "has-a" MediaItem objects
class Playlist:
    """
    The Context class. It delegates the sorting behavior to an external 
    strategy object instead of hardcoding the sorting logic itself.
    """
    def __init__(self, name: str, event_bus: "EventBus" = None):
        self._name = name
        self._items = []
        self._event_bus = event_bus
        
        # Default Strategy: Initialize with title sorting out-of-the-box
        self._sort_strategy = SortByTitle()

    @property
    def name(self) -> str:
        return self._name

    def set_sort_strategy(self, strategy):
        """Allows swapping the sorting algorithm dynamically at runtime."""
        self._sort_strategy = strategy

    def items_sorted(self) -> list:
        """
        Executes the strategy. It does NOT modify self._items.
        It passes the list to the strategy worker and returns the sorted copy. (part B5)
        """
        return self._sort_strategy.sort(self._items)

    def add_item(self, item: MediaItem):
        if not isinstance(item, MediaItem):
            raise TypeError("Only MediaItem instances can be added.")
        self._items.append(item)
        if self._event_bus is not None:
            self._event_bus.publish("item_added", {"title": item.title})

    def total_duration(self) -> int:
        return sum(item.duration for item in self._items)

    def __len__(self) -> int:
        return len(self._items)
    
class Library:
    """
    Composition: A Library 'has-a' dictionary to store Playlist objects.
    """
    def __init__(self, name: str):
        self._name = name
        self._playlists = {}  # Key: playlist name (str), Value: Playlist object

    def add_playlist(self, playlist: Playlist):
        # Store the playlist using its name string as the lookup key
        self._playlists[playlist.name] = playlist

    def statistics(self) -> dict:
        # Calculate item count and playtime durations across all stored playlists
        total_items = sum(len(pl) for pl in self._playlists.values())
        total_duration = sum(pl.total_duration() for pl in self._playlists.values())
        
        # Returns a backend-style data layout payload
        return {
            "total_items": total_items,
            "total_duration": total_duration
        } 

# ================================
# B3 — FACTORY METHOD: load_items 
# ================================      
def load_items(data:list) -> list:      # data:list expects an incoming parameter named data and its type should be a list (Python's version of dynamic array)
                                        # -> list: return type is a list
    """
    Factory Method: Reads raw dictionaries (typically from a JSON backend or database)
    and instantiates the correct concrete subclass of MediaItem.
    """
    created_items = []

    for record in data:
        media_type = record.get("type")
        
        # Branching logic to decide which object to construct
        if media_type == "song":
            item = Song(
                title=record["title"], 
                creator=record["creator"], 
                duration=record["duration"], 
                genre=record["genre"]
            )
        elif media_type == "podcast":
            item = Podcast(
                title=record["title"], 
                creator=record["creator"], 
                duration=record["duration"], 
                episode_number=record["episode_number"]
            )
        elif media_type == "audiobook":
            item = Audiobook(
                title=record["title"], 
                creator=record["creator"], 
                duration=record["duration"], 
                chapters=record["chapters"]
            )
        else:
            # Enforce error handling if a bad or malicious type string is parsed
            raise ValueError(f"Unknown media type encountered: {media_type}")
            
        created_items.append(item)
        
    return created_items

# ================================
# B4 — OBSERVER 
# ================================ 
class EventBus:
    """
    The Subject/Broker: Tracks subscribers and broadcasts events.
    C++ equivalent: A manager class holding a map of event strings 
    to vectors of std::function callbacks.
    """
    def __init__(self):
        # Dictionary mapping event names to a list of callback functions
        self._subscribers = {}

    def subscribe(self, event_name: str, callback):
        # If the event doesn't exist yet, initialize an empty list
        if event_name not in self._subscribers:
            self._subscribers[event_name] = []
        # Register the callback function
        self._subscribers[event_name].append(callback)

    def publish(self, event_name: str, payload: dict):
        # Fire every callback registered to this specific event
        for callback in self._subscribers.get(event_name, []):
            callback(payload)

# ================================
# B5 — STRATEGY 
# ================================            
class SortByTitle:
    """
    Concrete Strategy: Sorts media items alphabetically by title.
    """
    def sort(self, items: list) -> list:
        # key=lambda x: x.title.lower() makes the sort case-insensitive
        # sorted() automatically returns a BRAND NEW list, leaving original intact
        return sorted(items, key=lambda x: x.title.lower())

# ====================================================
# B6 — TEMPLATE METHOD PATTERN
# ====================================================

class CatalogExporter(ABC):
    """
    Abstract Class (Template Pattern Base).
    """
    def export(self, rows: list) -> str:
        # The core Template Method: controls the sequence of execution
        header = self.format_header()
        body = self.format_rows(rows)
        return f"{header}\n{body}"

    @abstractmethod
    def format_header(self) -> str:
        """Hook method for processing headers."""
        pass

    @abstractmethod
    def format_rows(self, rows: list) -> str:
        """Hook method for mapping dataset content loops."""
        pass


class CsvCatalogExporter(CatalogExporter):
    """
    Concrete Implementer specializing in flat standard CSV outputs.
    """
    def format_header(self) -> str:
        return "type,title,duration"

    def format_rows(self, rows: list) -> str:
        csv_lines = []
        for row in rows:
            line = f"{row["type"]},{row["title"]},{row["duration"]}"
            csv_lines.append(line)
        return "\n".join(csv_lines)


# ====================================================
# B6 — FACADE PATTERN
# ====================================================

def run_media_hub():
    """
    The Facade: Provides a clean, simplified entryway to mask the complexity 
    of the underlying components interacting together.
    """
    print("--- Running Media Hub Facade ---")

    # 1. Initialize Observer Infrastructure
    bus = EventBus()
    log = []
    bus.subscribe("item_added", lambda p: log.append(f"added:{p["title"]}"))

    # 2. Instantiate structural Composition blocks
    playlist = Playlist("Facade Master Mix", event_bus=bus)
    library = Library("Global Central Library")
    library.add_playlist(playlist)

    # 3. Use Factory Method to parse raw data block
    loaded_items = load_items(MEDIA_DATA)

    # 4. Inject items into playlist (automatically triggers background events)
    for item in loaded_items:
        playlist.add_item(item)

    # 5. Output Subsystem Metrics (Composition Validation)
    print("\n[Facade Report] Library Statistics:")
    stats = library.statistics()
    print(f"Total Items Count: {stats["total_items"]} | Total Combined Duration: {stats["total_duration"]}s")

    # 6. Output Intercepted Events (Observer Validation)
    print("\n[Facade Report] Log Tracker Records:")
    for entry in log:
        print(f"  * {entry}")

    # 7. Dynamic Algorithm Swapping (Strategy Validation)
    print("\n[Facade Report] Running Sort Strategies:")
    playlist.set_sort_strategy(SortByTitle())
    print("Alphabetical Output:")
    for item in playlist.items_sorted():
        print(f"  - {item.title}")

    # 8. Document Conversion 
    print("\n[Facade Report] Generating CSV String Compilation:")
    
    export_rows = []
    for item in playlist.items_sorted():
        # Extracted explicitly using required specification parameters
        row_dict = {
            "type": type(item).__name__,
            "title": item.title,
            "duration": item.duration
        }
        export_rows.append(row_dict)

    exporter = CsvCatalogExporter()
    csv_output = exporter.export(export_rows)
    print(csv_output)

class SortByDuration:
    """
    Concrete Strategy: Sorts media items by duration in ascending order.
    """
    def sort(self, items: list) -> list:
        return sorted(items, key=lambda x: x.duration)
    

# ================================================
# ENTRY POINT (Using global MEDIA_DATA)
# ================================================
if __name__ == "__main__":

    # --------------------------------------------
    # PART B1: OOP Hierarchy & Polymorphism
    # --------------------------------------------
    print("--- Instantiating Objects from MEDIA_DATA ---")

    # 1. Manually unpack dictionaries from MEDIA_DATA into Constructors
    # C++ equivalent: Accessing elements from a std::vector<std::unordered_map<std::string, std::variant>>
    song1 = Song(
        title=MEDIA_DATA[0]["title"],
        creator=MEDIA_DATA[0]["creator"],
        duration=MEDIA_DATA[0]["duration"],
        genre=MEDIA_DATA[0]["genre"]
    )

    song2 = Song(
        title=MEDIA_DATA[1]["title"],
        creator=MEDIA_DATA[1]["creator"],
        duration=MEDIA_DATA[1]["duration"],
        genre=MEDIA_DATA[1]["genre"]
    )

    podcast = Podcast(
        title=MEDIA_DATA[2]["title"],
        creator=MEDIA_DATA[2]["creator"],
        duration=MEDIA_DATA[2]["duration"],
        episode_number=MEDIA_DATA[2]["episode_number"]
    )

    audiobook = Audiobook(
        title=MEDIA_DATA[3]["title"],
        creator=MEDIA_DATA[3]["creator"],
        duration=MEDIA_DATA[3]["duration"],
        chapters=MEDIA_DATA[3]["chapters"]
    )

    # 2. Group the instantiated instances into a polymorphic tracking list
    media_list = [song1, song2, podcast, audiobook]

    print("\n--- Testing Polymorphism (B1 Requirement) ---")

    # 3. Polymorphic Loop
    # Every item automatically runs its own overridden version of describe()
    for item in media_list:
        print(item.describe())

    # --------------------------------------------
    # PART B4: Observer Pattern (EventBus)
    # --------------------------------------------
    print("\n--- B4: Testing Observer Pattern ---")

    # 1. Instantiate the central event broker
    # C++ equivalent: EventBus bus;
    bus = EventBus()

    # 2. Create the empty tracking list required by the assignment rules
    log = []

    # 3. Subscribe to the event bus using an anonymous lambda function
    # C++ equivalent: bus.subscribe("item_added", [&log](const auto& p) { log.push_back("added:" + p["title"]); });
    bus.subscribe("item_added", lambda p: log.append(f"added:{p["title"]}"))

    # 4. Instantiate a Playlist with the EventBus injected as a dependency
    # C++ equivalent: Playlist playlist("My Mix", &bus);
    playlist = Playlist("My Mix", event_bus=bus)

    print("Adding items to the playlist...")
    
    # 5. These calls will internally trigger: bus.publish("item_added", ...)
    playlist.add_item(song1)
    playlist.add_item(podcast)

    # 6. Print out the log array to prove the Observer intercepted the actions successfully
    print("\nVerification - Event Log Contents:")
    for entry in log:
        print(entry)

    # --------------------------------------------
    # PART B5: Strategy Pattern (Sorting)
    # --------------------------------------------
    print("\n--- B5: Testing Strategy Pattern ---")

    # 1. Add the remaining items to the playlist
    playlist.add_item(song2)
    playlist.add_item(audiobook)

    # 2. Inject the Title Sort Strategy dynamically
    # C++ equivalent: playlist.set_sort_strategy(std::make_unique<SortByTitle>());
    playlist.set_sort_strategy(SortByTitle())

    # 3. Request the sorted items array copy
    title_sorted_items = playlist.items_sorted()

    # 4. Print titles from items_sorted() 
    print("Titles sorted via SortByTitle strategy:")
    for item in title_sorted_items:
        print(f"- {item.title}")

    # 5. SortByDuration()
    playlist.set_sort_strategy(SortByDuration())
    duration_sorted_items = playlist.items_sorted()

    print("\nTitles sorted via SortByDuration strategy:")
    for item in duration_sorted_items:
        print(f"- {item.title} ({item.duration}s)")

    # --------------------------------------------
    # PART B6: 
    # --------------------------------------------  
    run_media_hub()    
        