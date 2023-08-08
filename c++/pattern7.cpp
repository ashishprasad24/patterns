class Solution {

  public:
    void printTriangle(int n) {

        for (int i = n; i >= 1; i--) {
            for (int j = 1; j < i; j++) {
                cout << " ";
            }
            for (int j = 1; j <= 2 * (n - i) + 1; j++) {
                cout << "*";
            }
            cout << endl;
        }
    }
};
