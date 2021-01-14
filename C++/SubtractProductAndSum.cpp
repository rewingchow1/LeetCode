//#include <iostream>
//#include <vector>
//#include <string>
//using namespace std;
//
//int subtractProductAndSum(int n) {
//	string str = to_string(n);
//	vector<int> list;
//	int product = 1;
//	int sum = 0;
//	for (int i = 0; i < str.size(); i++) {
//		string s(1, str[i]);
//		list.push_back(stoi(s));
//	}
//	for (int j = 0; j < list.size(); j++) {
//		product = product * list[j];
//
//	}
//	for (int k = 0; k < list.size(); k++) {
//		sum = sum + list[k];
//
//	}
//	return product - sum;
//}
//
//
//int main() {
//	int n = 4421;
//	int out;
//	out = subtractProductAndSum(n);
//	cout << out << endl;
//	return 0;
//}