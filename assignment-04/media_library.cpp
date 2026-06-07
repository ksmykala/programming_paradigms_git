#include <iostream>
#include <vector>
#include <string>
#include <functional>
#include <stdexcept>

using namespace std;


// ── Dataset ───────────────────────────────────────────────────────────────────

struct MediaData {
    string type;
    string title;
    string creator;
    int duration;
    string genre;
    int episode_number;
    int chapters;
};

MediaData MEDIA_DATA[] = {
    {"song",      "Bohemian Rhapsody", "Queen",         354,   "Rock", 0,   0 },
    {"song",      "Blinding Lights",   "The Weeknd",    200,   "Pop",  0,   0 },
    {"podcast",   "Lex Fridman #400",  "Lex Fridman",   7200,  "",     400, 0 },
    {"audiobook", "Clean Code",        "Robert Martin", 25200, "",     0,   17},
};

int MEDIA_DATA_SIZE = 4;


// ── B1: OOP Hierarchy ─────────────────────────────────────────────────────────

class MediaItem {
protected:
    string title;
    string creator;
    int duration;

public:
    MediaItem(string t, string c, int d) {
        if (t.empty()) {
            throw invalid_argument("title cannot be empty");
        }
        if (c.empty()) {
            throw invalid_argument("creator cannot be empty");
        }
        if (d <= 0) {
            throw invalid_argument("duration must be greater than 0");
        }
        title    = t;
        creator  = c;
        duration = d;
    }

    string getTitle()    { return title; }
    string getCreator()  { return creator; }
    int    getDuration() { return duration; }

    virtual string typeName() = 0;
    virtual string describe() = 0;

    virtual ~MediaItem() {}
};


class Song : public MediaItem {
    string genre;
public:
    Song(string t, string c, int d, string g) : MediaItem(t, c, d) {
        genre = g;
    }

    string typeName() { return "Song"; }

    string describe() {
        return "Song: " + title + " by " + creator + " [" + genre + "] (" + to_string(duration) + "s)";
    }
};


class Podcast : public MediaItem {
    int episode_number;
public:
    Podcast(string t, string c, int d, int ep) : MediaItem(t, c, d) {
        episode_number = ep;
    }

    string typeName() { return "Podcast"; }

    string describe() {
        return "Podcast: " + title + " by " + creator + " [Episode " + to_string(episode_number) + "] (" + to_string(duration) + "s)";
    }
};


class Audiobook : public MediaItem {
    int chapters;
public:
    Audiobook(string t, string c, int d, int ch) : MediaItem(t, c, d) {
        chapters = ch;
    }

    string typeName() { return "Audiobook"; }

    string describe() {
        return "Audiobook: " + title + " by " + creator + " [" + to_string(chapters) + " chapters] (" + to_string(duration) + "s)";
    }
};


// ── B4: Observer ──────────────────────────────────────────────────────────────

struct Payload {
    string title;
};

class EventBus {
    // for each event name we keep a list of callbacks
    vector<string> eventNames;
    vector<vector<function<void(Payload)>>> callbacks;

public:
    void subscribe(string eventName, function<void(Payload)> callback) {
        // find if we already have this event
        for (int i = 0; i < eventNames.size(); i++) {
            if (eventNames[i] == eventName) {
                callbacks[i].push_back(callback);
                return;
            }
        }
        // new event
        eventNames.push_back(eventName);
        vector<function<void(Payload)>> list;
        list.push_back(callback);
        callbacks.push_back(list);
    }

    void publish(string eventName, Payload payload) {
        for (int i = 0; i < eventNames.size(); i++) {
            if (eventNames[i] == eventName) {
                for (int j = 0; j < callbacks[i].size(); j++) {
                    callbacks[i][j](payload);
                }
            }
        }
    }
};


// ── B5: Strategy ──────────────────────────────────────────────────────────────

class SortStrategy {
public:
    virtual vector<MediaItem*> sort(vector<MediaItem*> items) = 0;
    virtual ~SortStrategy() {}
};


class SortByTitle : public SortStrategy {
public:
    vector<MediaItem*> sort(vector<MediaItem*> items) {
        for (int i = 0; i < items.size(); i++) {
            for (int j = i + 1; j < items.size(); j++) {
                string a = items[i]->getTitle();
                string b = items[j]->getTitle();
                // convert to lowercase for comparison
                for (int k = 0; k < a.size(); k++) a[k] = tolower(a[k]);
                for (int k = 0; k < b.size(); k++) b[k] = tolower(b[k]);
                if (a > b) {
                    MediaItem* temp = items[i];
                    items[i] = items[j];
                    items[j] = temp;
                }
            }
        }
        return items;
    }
};


class SortByDuration : public SortStrategy {
public:
    vector<MediaItem*> sort(vector<MediaItem*> items) {
        for (int i = 0; i < items.size(); i++) {
            for (int j = i + 1; j < items.size(); j++) {
                if (items[i]->getDuration() > items[j]->getDuration()) {
                    MediaItem* temp = items[i];
                    items[i] = items[j];
                    items[j] = temp;
                }
            }
        }
        return items;
    }
};


// ── B2: Composition ───────────────────────────────────────────────────────────

struct Stats {
    int total_items;
    int total_duration;
};

class Playlist {
    string name;
    vector<MediaItem*> items;
    SortStrategy* sortStrategy;
    EventBus* eventBus;

public:
    Playlist(string n, EventBus* bus = NULL) {
        name          = n;
        sortStrategy  = NULL;
        eventBus      = bus;
    }

    string getName() { return name; }

    void add_item(MediaItem* item) {
        items.push_back(item);
        if (eventBus != NULL) {
            Payload p;
            p.title = item->getTitle();
            eventBus->publish("item_added", p);
        }
    }

    int total_duration() {
        int total = 0;
        for (int i = 0; i < items.size(); i++) {
            total += items[i]->getDuration();
        }
        return total;
    }

    int size() { return items.size(); }

    void set_sort_strategy(SortStrategy* s) {
        sortStrategy = s;
    }

    vector<MediaItem*> items_sorted() {
        if (sortStrategy == NULL) return items;
        return sortStrategy->sort(items);
    }
};


class Library {
    string name;
    vector<Playlist*> playlists;

public:
    Library(string n) {
        name = n;
    }

    void add_playlist(Playlist* p) {
        playlists.push_back(p);
    }

    Stats statistics() {
        Stats s;
        s.total_items    = 0;
        s.total_duration = 0;
        for (int i = 0; i < playlists.size(); i++) {
            s.total_items    += playlists[i]->size();
            s.total_duration += playlists[i]->total_duration();
        }
        return s;
    }
};


// ── B3: Factory Method ────────────────────────────────────────────────────────

MediaItem* createMediaItem(MediaData record) {
    if (record.type == "song") {
        return new Song(record.title, record.creator, record.duration, record.genre);
    }
    if (record.type == "podcast") {
        return new Podcast(record.title, record.creator, record.duration, record.episode_number);
    }
    if (record.type == "audiobook") {
        return new Audiobook(record.title, record.creator, record.duration, record.chapters);
    }
    throw invalid_argument("unknown media type: " + record.type);
}

vector<MediaItem*> load_items() {
    vector<MediaItem*> items;
    for (int i = 0; i < MEDIA_DATA_SIZE; i++) {
        items.push_back(createMediaItem(MEDIA_DATA[i]));
    }
    return items;
}


// ── B6: Template Method + Facade ─────────────────────────────────────────────

class CatalogExporter {
public:
    virtual ~CatalogExporter() {}

    string exportCatalog(vector<MediaItem*> items) {
        return format_header() + format_rows(items);
    }

protected:
    virtual string format_header() = 0;
    virtual string format_rows(vector<MediaItem*> items) = 0;
};


class CsvCatalogExporter : public CatalogExporter {
protected:
    string format_header() {
        return "type,title,duration\n";
    }

    string format_rows(vector<MediaItem*> items) {
        string result = "";
        for (int i = 0; i < items.size(); i++) {
            result += items[i]->typeName() + "," + items[i]->getTitle() + "," + to_string(items[i]->getDuration()) + "\n";
        }
        return result;
    }
};


// ── Facade ────────────────────────────────────────────────────────────────────

void run_media_hub() {
    // 1. Load items
    vector<MediaItem*> items = load_items();

    // 2. Setup EventBus + log subscriber
    EventBus bus;
    vector<string> log;
    bus.subscribe("item_added", [&log](Payload p) {
        log.push_back("added:" + p.title);
    });

    // 3. Create playlist and library
    Playlist playlist("My Playlist", &bus);
    Library library("My Library");
    library.add_playlist(&playlist);

    // Add all items to playlist
    for (int i = 0; i < items.size(); i++) {
        playlist.add_item(items[i]);
    }

    // Polymorphism demo
    for (int i = 0; i < items.size(); i++) {
        cout << items[i]->describe() << endl;
    }

    // Statistics
    Stats stats = library.statistics();
    cout << "{total_items: " << stats.total_items << ", total_duration: " << stats.total_duration << "}" << endl;

    // Observer log
    cout << "[";
    for (int i = 0; i < log.size(); i++) {
        cout << "'" << log[i] << "'";
        if (i < log.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    // Sort demo
    SortByTitle sortByTitle;
    playlist.set_sort_strategy(&sortByTitle);
    vector<MediaItem*> sorted = playlist.items_sorted();
    cout << "Sorted: ";
    for (int i = 0; i < sorted.size(); i++) {
        cout << sorted[i]->getTitle();
        if (i < sorted.size() - 1) cout << " | ";
    }
    cout << endl;

    // CSV export
    CsvCatalogExporter exporter;
    cout << exporter.exportCatalog(items) << endl;

    // Cleanup
    for (int i = 0; i < items.size(); i++) {
        delete items[i];
    }
}


int main() {
    run_media_hub();
    return 0;
}