#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main() {

    string dates[] = {
        "2024-01-05", "2024-01-07", "2024-01-09", "2024-01-10",
        "2024-01-12", "2024-01-14", "2024-01-15", "2024-01-17",
        "2024-01-20", "2024-01-22", "2024-01-25", "2024-01-28"
    };

    string categories[] = {
        "Food", "Transport", "Entertainment", "Food",
        "Utilities", "Food", "Transport", "Entertainment",
        "Food", "Utilities", "Transport", "Entertainment"
    };

    double amounts[] = {
        42.50, 15.00, 60.00, 8.75, 120.00, 55.20,
        30.00, 14.99, 38.00, 45.00, 22.00, 25.00
    };

    string descriptions[] = {
        "Groceries", "Bus pass", "Concert ticket", "Coffee & snack",
        "Electricity bill", "Restaurant dinner", "Taxi",
        "Streaming subscription", "Groceries", "Internet bill",
        "Train ticket", "Book"
    };

    int count = 12;

    cout << fixed << setprecision(2);

    double total = 0;
    for (int i = 0; i < count; i++) {
        total = total + amounts[i];
    }

    cout << "Total expenses: " << total << endl;
    cout << "Number of records: " << count << endl;

    string uniqueCategories[] = {"Entertainment", "Food", "Transport", "Utilities"};
    double categoryTotals[] = {0, 0, 0, 0};
    int numCategories = 4;

    for (int i = 0; i < count; i++) {
        for (int j = 0; j < numCategories; j++) {
            if (categories[i] == uniqueCategories[j]) {
                categoryTotals[j] = categoryTotals[j] + amounts[i];
            }
        }
    }

    cout << "\nCategory breakdown:" << endl;
    for (int i = 0; i < numCategories; i++) {
        cout << "  " << uniqueCategories[i] << " : " << categoryTotals[i] << endl;
    }

    int maxIndex = 0;
    int minIndex = 0;

    for (int i = 1; i < count; i++) {
        if (amounts[i] > amounts[maxIndex]) {
            maxIndex = i;
        }
        if (amounts[i] < amounts[minIndex]) {
            minIndex = i;
        }
    }

    cout << "\nMost expensive : " << descriptions[maxIndex]
         << " (" << categories[maxIndex] << ")"
         << " - " << amounts[maxIndex] << endl;

    cout << "Least expensive: " << descriptions[minIndex]
         << " (" << categories[minIndex] << ")"
         << " - " << amounts[minIndex] << endl;

    double sum = 0;
    for (int i = 0; i < count; i++) {
        sum = sum + amounts[i];
    }
    double average = sum / count;

    cout << "\nAverage expense: " << average << endl;

    cout << "Expenses above average:" << endl;
    for (int i = 0; i < count; i++) {
        if (amounts[i] > average) {
            cout << "  - " << descriptions[i]
                 << " (" << amounts[i] << ")" << endl;
        }
    }

    return 0;
}
