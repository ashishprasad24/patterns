#include <iostream>

using namespace std;
int row, col;
int
main ()
{
  for (row = 1; row <= 5; row++)
    {
      for (col = 1; col <= 5 - row; col++)
	cout << " ";

      for (col = 1; col <= row; col++)
	cout << col << " ";

      for (col = row - 1; col >= 1; col--)
	cout << col << " ";

      cout << endl;
    }

}
