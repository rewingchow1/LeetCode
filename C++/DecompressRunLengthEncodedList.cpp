//#include <iostream>
//#include <vector>
//#include <string>
//using namespace std;
//
//vector<int> decompressRLElist(vector<int> nums) {
//	vector<int> out;
//	int a, b;
//	int stop = nums.size() / 2;
//	for (int i = 0; i < stop; i++) {
//		a = nums[2 * i];
//		b = nums[2 * i + 1];
//		for (int j = 0; j < a; j++) {
//			out.push_back(b);
//		}
//	}
//	return out;
//}
//
//
//int main() {
//	vector<int> nums = { 5,2,3,4 };
//	vector<int> out;
//	out = decompressRLElist(nums);
//	for (auto i = out.begin(); i != out.end(); ++i)
//		cout << *i << " ";
//	return 0;
//}