#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {

    int n;

    // Read sequence length

    while ( cin >> n ) {

        if (n == 1) {

            cout << "Jolly" << endl;
            cin >> n;
            continue;
        }

        // Read sequence

        int sequence[n];

        for (int i = 0; i < n; i++) {

            cin >> sequence[i];
        }

        int check[n-1];
        std::fill_n(check, n-1, 0);

        // Check the sequence is jolly jumper

        bool fail = false;

        for (int i = 0; i < n-1; i++) {

            int diff = abs(sequence[i] - sequence[i+1]);

            if ( diff > 0 and diff < n ) {

                check[diff-1] = 1;
            }

            else{

                cout << "Not jolly" << endl;
                fail = true;
                break;
            }
        }

        if (!fail) {

            fail = false;

            for (int i = 0; i < n-1; i++) {

                if ( check[i] == 0 ) {

                    cout << "Not jolly" << endl;
                    fail = true;
                    break;
                }
            }

            if (!fail) {

                cout << "Jolly" << endl;
            }
        }
    }

    return 0;
}
