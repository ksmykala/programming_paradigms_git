#include <iostream>
#include <vector>
#include <string>
#include <memory>
#include <map>
#include <functional>
#include <algorithm>
#include <sstream>
using namespace std;


// data


struct MediaRecord {
    string type;
    string title;
    string creator;
    int duration;

    string genre;
    int episodeNumber = 0;
    int chapters = 0;
};

vector<MediaRecord> MEDIA_DATA = {
    {"song", "Bohemian Rhapsody", "Queen", 354, "Rock"},
    {"song", "Blinding Lights", "The Weeknd", 200, "Pop"},
    {"podcast", "Lex Fridman #400", "Lex Fridman", 7200, "", 400},
    {"audiobook", "Clean Code", "Robert Martin", 25200, "", 0, 17}
};


// B1


class MediaItem {
protected:
    string title;
    string creator;
    int duration;

public:
    MediaItem(string t, string c, int d)
        : title(t), creator(c), duration(d) {

        // B1 - walidacja
        if (title.empty() || creator.empty()) {
            throw invalid_argument("Title and creator cannot be empty");
        }

        if (duration <= 0) {
            throw invalid_argument("Duration must be > 0");
        }
    }

    virtual ~MediaItem() = default;

    string getTitle() const {
        return title;
    }

    int getDuration() const {
        return duration;
    }

    // B1 - metoda abstrakcyjna
    virtual string describe() const = 0;
};

class Song : public MediaItem {
private:
    string genre;

public:
    Song(string t, string c, int d, string g)
        : MediaItem(t, c, d), genre(g) {
    }

    string describe() const override {
        return "Song: " + title + " by " + creator +
            " [" + genre + "] (" +
            to_string(duration) + "s)";
    }
};

class Podcast : public MediaItem {
private:
    int episodeNumber;

public:
    Podcast(string t, string c, int d, int ep)
        : MediaItem(t, c, d), episodeNumber(ep) {
    }

    string describe() const override {
        return "Podcast: " + title +
            " Episode #" + to_string(episodeNumber) +
            " by " + creator +
            " (" + to_string(duration) + "s)";
    }
};

class Audiobook : public MediaItem {
private:
    int chapters;

public:
    Audiobook(string t, string c, int d, int ch)
        : MediaItem(t, c, d), chapters(ch) {
    }

    string describe() const override {
        return "Audiobook: " + title +
            " by " + creator +
            " (" + to_string(chapters) +
            " chapters, " +
            to_string(duration) + "s)";
    }
};

// B4 - Observer


class EventBus {
private:
    map<string, vector<function<void(map<string, string>)>>> subscribers;

public:
    void subscribe(
        const string& eventName,
        function<void(map<string, string>)> callback) {

        subscribers[eventName].push_back(callback);
    }

    void publish(
        const string& eventName,
        map<string, string> payload) {

        for (auto& callback : subscribers[eventName]) {
            callback(payload);
        }
    }
};


// B5 - Strategy


class SortStrategy {
public:
    virtual vector<shared_ptr<MediaItem>>
        sort(const vector<shared_ptr<MediaItem>>& items) = 0;

    virtual ~SortStrategy() = default;
};

class SortByTitle : public SortStrategy {
public:
    vector<shared_ptr<MediaItem>>
        sort(const vector<shared_ptr<MediaItem>>& items) override {

        auto result = items;

        std::sort(result.begin(), result.end(),
            [](auto a, auto b) {
                return a->getTitle() < b->getTitle();
            });

        return result;
    }
};

class SortByDuration : public SortStrategy {
public:
    vector<shared_ptr<MediaItem>>
        sort(const vector<shared_ptr<MediaItem>>& items) override {

        auto result = items;

        std::sort(result.begin(), result.end(),
            [](auto a, auto b) {
                return a->getDuration() < b->getDuration();
            });

        return result;
    }
};


// B2 - Kompozycja


class Playlist {
private:
    vector<shared_ptr<MediaItem>> items;

    EventBus* eventBus;

    // B5 - aktualna strategia sortowania
    shared_ptr<SortStrategy> strategy;

public:
    Playlist(EventBus* bus = nullptr)
        : eventBus(bus) {
    }

    void addItem(shared_ptr<MediaItem> item) {

        items.push_back(item);

        // B4 - publikacja zdarzenia
        if (eventBus) {
            eventBus->publish(
                "item_added",
                { {"title", item->getTitle()} }
            );
        }
    }

    int totalDuration() const {

        int total = 0;

        for (auto item : items) {
            total += item->getDuration();
        }
        return total;
    }

    size_t size() const {
        return items.size();
    }
    const vector<shared_ptr<MediaItem>>& getItems() const {
        return items;
    }

    // B5
    void setSortStrategy(shared_ptr<SortStrategy> s) {
        strategy = s;
    }

    vector<shared_ptr<MediaItem>> itemsSorted() {

        if (!strategy) {
            return items;
        }

        return strategy->sort(items);
    }
};

class Library {
private:
    vector<shared_ptr<Playlist>> playlists;

public:
    void addPlaylist(shared_ptr<Playlist> playlist) {
        playlists.push_back(playlist);
    }

    // B2 - statystyki biblioteki

    map<string, int> statistics() {

        int totalItems = 0;
        int totalDuration = 0;

        for (auto playlist : playlists) {
            totalItems += playlist->size();
            totalDuration += playlist->totalDuration();
        }

        return {
            {"total_items", totalItems},
            {"total_duration", totalDuration}
        };
    }
};


// B6 - Template Method
class CatalogExporter {
public:
    virtual string formatHeader() = 0;
    virtual string formatRows(
        const vector<map<string, string>>& rows) = 0;

    string exportCatalog(
        const vector<map<string, string>>& rows) {

        return formatHeader() + formatRows(rows);
    }
    virtual ~CatalogExporter() = default;
};

class CsvCatalogExporter : public CatalogExporter {
public:
    string formatHeader() override {
        return "type,title,duration\n";
    }

    string formatRows(
        const vector<map<string, string>>& rows) override {

        stringstream ss;

        for (auto& row : rows) {

            ss << row.at("type") << ","
                << row.at("title") << ","
                << row.at("duration") << "\n";
        }

        return ss.str();
    }
};


// B3 - Factory Method


vector<shared_ptr<MediaItem>>
loadItems(const vector<MediaRecord>& data) {

    vector<shared_ptr<MediaItem>> items;

    for (const auto& r : data) {

        if (r.type == "song") {

            items.push_back(
                make_shared<Song>(
                    r.title,
                    r.creator,
                    r.duration,
                    r.genre
                )
            );

        }
        else if (r.type == "podcast") {

            items.push_back(
                make_shared<Podcast>(
                    r.title,
                    r.creator,
                    r.duration,
                    r.episodeNumber
                )
            );

        }
        else if (r.type == "audiobook") {

            items.push_back(
                make_shared<Audiobook>(
                    r.title,
                    r.creator,
                    r.duration,
                    r.chapters
                )
            );

        }
        else {
            throw runtime_error("Unknown media type");
        }
    }

    return items;
}


// B6 - Facade
void runMediaHub() {

    auto items = loadItems(MEDIA_DATA);

    EventBus bus;

    vector<string> log;

    bus.subscribe(
        "item_added",
        [&](map<string, string> payload) {
            log.push_back("added:" + payload["title"]);
        }
    );

    auto playlist = make_shared<Playlist>(&bus);
    auto library = make_shared<Library>();

    library->addPlaylist(playlist);

    for (auto item : items) {
        playlist->addItem(item);
    }

    // B1 - polimorfizm
    for (auto item : items) {
        cout << item->describe() << endl;
    }

    auto stats = library->statistics();

    cout << "\nStatistics:" << endl;
    cout << "{ total_items: "
        << stats["total_items"]
        << ", total_duration: "
        << stats["total_duration"]
        << " }" << endl;

    cout << "\nLog:" << endl;
    for (auto& entry : log) {
        cout << entry << endl;
    }

    // B5
    playlist->setSortStrategy(
        make_shared<SortByTitle>()
    );

    cout << "\nSorted: ";

    auto sortedItems = playlist->itemsSorted();

    for (size_t i = 0; i < sortedItems.size(); i++) {

        cout << sortedItems[i]->getTitle();

        if (i < sortedItems.size() - 1) {
            cout << " | ";
        }
    }

    cout << endl;

    // B6 - eksport CSV
    vector<map<string, string>> rows;

    for (auto item : items) {

        rows.push_back({
            {"type", typeid(*item).name()},
            {"title", item->getTitle()},
            {"duration", to_string(item->getDuration())}
            });
    }
    CsvCatalogExporter exporter;

    cout << "\nCSV Export:\n";
    cout << exporter.exportCatalog(rows);
}
int main() {
    runMediaHub();
    return 0;
}