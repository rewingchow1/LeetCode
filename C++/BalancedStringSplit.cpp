//#include <iostream>
//#include <vector>
//#include <string>
//using namespace std;
//
//int balancedStringSplit(string s) {
//	int count = 0;
//	int countl = 0;
//	int countr = 0;
//	bool flag = true;
//	for (int i = 0; i < s.size(); i++) {
//		if ((i > 0) && (s[i] != s[i - 1])) {
//			if (flag == true) flag = false;
//			else flag = true;
//		}
//		if (flag) {
//			countl++;
//		}
//		if (!flag) {
//			countr++;
//		}
//		if (countl == countr) {
//			countl = 0;
//			countr = 0;
//			count++;
//		}
//	}
//	return count;
//}
//
//int main() {
//	string s = "RLRRLLRLRL";
//	int out;
//	out = balancedStringSplit(s);
//	cout << out << endl;
//	return 0;
//}