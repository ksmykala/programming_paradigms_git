#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

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

/*
 * getTotal
 * Calculates the total amount of all expenses.
 * Parameters: none (uses global arrays)
 * Returns: double - sum of all amounts
 */
double getTotal() {
    double total = 0;
    for (int i = 0; i < count; i++) {
        total = total + amounts[i];
    }
    return total;
}

/*
 * getCount
 * Returns the number of expense records.
 * Parameters: none
 * Returns: int - number of expenses
 */
int getCount() {
    return count;
}

/*
 * getCategoryTotals
 * Builds a breakdown of total amount spent per category.
 * Prints each category sorted alphabetically.
 * Parameters: none
 * Returns: void
 */
void getCategoryTotals() {
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
}

/*
 * getMostExpensive
 * Finds the most expensive expense without using max().
 * Parameters: none
 * Returns: int - index of the most expensive expense
 */
int getMostExpensive() {
    int maxIndex = 0;
    for (int i = 1; i < count; i++) {
        if (amounts[i] > amounts[maxIndex]) {
            maxIndex = i;
        }
    }
    return maxIndex;
}

/*
 * getLeastExpensive
 * Finds the least expensive expense without using min().
 * Parameters: none
 * Returns: int - index of the least expensive expense
 */
int getLeastExpensive() {
    int minIndex = 0;
    for (int i = 1; i < count; i++) {
        if (amounts[i] < amounts[minIndex]) {
            minIndex = i;
        }
    }
    return minIndex;
}

/*
 * getAverage
 * Calculates the average expense amount.
 * Parameters: none
 * Returns: double - average of all amounts
 */
double getAverage() {
    double total = getTotal();
    return total / count;
}

/*
 * getAboveAverage
 * Finds and prints all expenses strictly above the average amount.
 * Parameters: none
 * Returns: void
 */
void getAboveAverage() {
    double average = getAverage();
    cout << "\nAverage expense: " << average << endl;
    cout << "Expenses above average:" << endl;
    for (int i = 0; i < count; i++) {
        if (amounts[i] > average) {
            cout << "  - " << descriptions[i]
                 << " (" << amounts[i] << ")" << endl;
        }
    }
}

/*
 * printSummary
 * Prints the full summary report by calling all helper functions.
 * Parameters: none
 * Returns: void
 */
void printSummary() {
    cout << fixed << setprecision(2);

    cout << "Total expenses: " << getTotal() << endl;
    cout << "Number of records: " << getCount() << endl;

    getCategoryTotals();

    int maxIndex = getMostExpensive();
    int minIndex = getLeastExpensive();

    cout << "\nMost expensive : " << descriptions[maxIndex]
         << " (" << categories[maxIndex] << ")"
         << " - " << amounts[maxIndex] << endl;

    cout << "Least expensive: " << descriptions[minIndex]
         << " (" << categories[minIndex] << ")"
         << " - " << amounts[minIndex] << endl;

    getAboveAverage();
}

int main() {
    printSummary();
    return 0;
}
