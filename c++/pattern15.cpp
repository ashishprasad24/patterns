class Solution {
  public:
    void printTriangle(int n) {
        for (int i=0;i<n;i++){
            for(char ch='A'; ch<='A'+(n-i-1); ch++){
                cout<< ch;
            }
            cout<<endl;
        }
    
    }
};
