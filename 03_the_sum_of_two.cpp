#include <fstream> 
#include <vector>
#include <string>

using namespace std;

int main() {
 ifstream infile ("input.txt");
 int target = -1;
 int target_length;
  vector<int> numbers;
  string s;
  int number;
 for (infile >> s; !infile.eof(); infile >> s) {
  if (target == -1) {
         number = stoi(s);
   target = number;
         target_length = s.length();
  } else if (target_length >= s.length()) {
         number = stoi(s);
         if (number < target) {
    numbers.push_back(number);
            }
  }
 }
 infile.close();
 int l = 0;
 int r = numbers.size() - 1;
 string result = "0";
 int sum;
 while (l < r) {
  sum = numbers[l] + numbers[r];
  if (sum > target) {
   r--;
  } else if (sum < target) {
   l++;
  } else {
   result = "1";
   break;
  }
 }
 ofstream outfile ("output.txt");
 outfile << result;
 outfile.close();
 return 0;
}