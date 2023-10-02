#include <iostream>
using namespace std;

struct NumberFrequency {
    int number;
    int freq;
};

void sortBasedOnFrequency(NumberFrequency arr[], int size) {
    // Simple bubble sort based on frequency (and then number as a tiebreaker).
    for (int i = 0; i < size; i++) {
        for (int j = i + 1; j < size; j++) {
            if (arr[j].freq > arr[i].freq || (arr[j].freq == arr[i].freq && arr[j].number < arr[i].number)) {
                swap(arr[i], arr[j]);
            }
        }
    }
}

void topKFrequent(int intArray[], int size, int k) {
    NumberFrequency freqArr[size];
    for (int i = 0; i < size; i++) {
        freqArr[i].freq = 0; // Initialize frequencies to zero
        
        // Check if the number was seen before
        bool seenBefore = false;
        for (int j = 0; j < i; j++) {
            if (intArray[i] == intArray[j]) {
                freqArr[j].freq++;
                seenBefore = true;
                break;
            }
        }

        // If the number is not seen before, set its frequency to 1
        if (!seenBefore) {
            freqArr[i].number = intArray[i];
            freqArr[i].freq = 1;
        }
    }

    // Sort numbers based on frequency
    sortBasedOnFrequency(freqArr, size);

    // Print top k frequent numbers
    cout << "Top " << k << " frequent numbers are: ";
    for (int i = 0; i < k && i < size; i++) {
        cout << freqArr[i].number << " ";
    }
    cout << endl;
}

void runTests() {
    // Automated tests
    int test1[] = {1,1,2,2,3};
    cout << "Test 1... ";
    topKFrequent(test1, 5, 2);  // Expected: 1 2

    int test2[] = {5,5,5,2,2,9,9};
    cout << "Test 2... ";
    topKFrequent(test2, 7, 1);  // Expected: 5
}

int main() {
    try {
        runTests();

        // Defining the size of the array
        int size;
        cout << "Choose the size of your array: ";
        cin >> size;

        // Check if size is valid
        if(size <= 0) {
            throw runtime_error("Invalid size for the array.");
        }

        // Store numbers in the array
        int intArray[size];
        for(int i = 0; i < size; i++) {
            cout << "Type the " << i+1 << "st number of the array: ";
            cin >> intArray[i];
        }

        // Defining k
        int k;
        cout << "Type the value of k (number of most frequent elements you want to return): ";
        cin >> k;

        // Check if k is valid
        if(k <= 0 || k > size) {
            throw runtime_error("Invalid value for k.");
        }

        // Calling function to calculate and print the k most frequent elements
        topKFrequent(intArray, size, k);
    } catch (const exception& e) {
        cerr << "Error: " << e.what() << endl;
    }

    return 0;
}


