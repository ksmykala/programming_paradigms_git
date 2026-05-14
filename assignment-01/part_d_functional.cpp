#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <numeric>
#include <algorithm>
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

int numExpenses = 12;

// D1 - Total using accumulate (like sum in python)
double getTotalFunctional() {
    vector<double> amountVec(amounts, amounts + numExpenses);
    return accumulate(amountVec.begin(), amountVec.end(), 0.0);
}

// D2 - Category totals using for_each and lambda
void getCategoryTotalsFunctional() {
    vector<string> uniqueCategories = {"Entertainment", "Food", "Transport", "Utilities"};

    cout << "\nCategory breakdown:" << endl;
    for_each(uniqueCategories.begin(), uniqueCategories.end(), [](string cat) {
        double total = 0;
        vector<int> indices = {0,1,2,3,4,5,6,7,8,9,10,11};
        total = accumulate(indices.begin(), indices.end(), 0.0, [&cat](double sum, int i) {
            return (categories[i] == cat) ? sum + amounts[i] : sum;
        });
        cout << fixed << setprecision(2);
        cout << "  " << cat << " : " << total << endl;
    });
}

// D3 - Above average using copy_if and lambda (like filter in python)
void getAboveAverageFunctional() {
    vector<double> amountVec(amounts, amounts + numExpenses);
    double average = accumulate(amountVec.begin(), amountVec.end(), 0.0) / numExpenses;

    vector<int> indices = {0,1,2,3,4,5,6,7,8,9,10,11};
    vector<int> filtered;
    copy_if(indices.begin(), indices.end(),
            back_inserter(filtered),
            [average](int i) { return amounts[i] > average; });

    cout << "\nAverage expense: " << fixed << setprecision(2) << average << endl;
    cout << "Expenses above average:" << endl;
    for_each(filtered.begin(), filtered.end(), [](int i) {
        cout << fixed << setprecision(2);
        cout << "  - " << descriptions[i] << " (" << amounts[i] << ")" << endl;
    });
}

// D4 - Format expenses using transform and lambda (like map in python)
void formatExpenses() {
    vector<int> indices = {0,1,2,3,4,5,6,7,8,9,10,11};
    vector<string> formatted(numExpenses);

    transform(indices.begin(), indices.end(), formatted.begin(), [](int i) {
        ostringstream oss;
        oss << fixed << setprecision(2) << amounts[i];
        return dates[i] + " | " + categories[i] + " | " + descriptions[i] + " | $" + oss.str();
    });

    cout << "\nFormatted expenses:" << endl;
    for_each(formatted.begin(), formatted.end(), [](string line) {
        cout << line << endl;
    });
}

int main() {
    cout << fixed << setprecision(2);
    cout << "Total expenses: " << getTotalFunctional() << endl;
    getCategoryTotalsFunctional();
    getAboveAverageFunctional();
    formatExpenses();
    return 0;
}
