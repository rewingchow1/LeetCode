//#include <iostream>
//#include <vector>
//#include <string>
//using namespace std;
//
//string defangIPaddr(string address) {
//	string out;
//	for (int i = 0; i < address.size(); i++) {
//		if (address[i] == '.') {
//			out.push_back('[');
//			out.push_back('.');
//			out.push_back(']');
//		}
//		else {
//			out.push_back(address[i]);
//		}
//	}
//	return out;
//}
//
//
//int main() {
//	string IP = "10.6.139.281";
//	string out;
//	out = defangIPaddr(IP);
//	cout << out;
//	return 0;
//}