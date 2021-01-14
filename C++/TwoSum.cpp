//#include <iostream>
//#include <vector>
//using namespace std;
//
//
//vector<int> twosum(vector<int> nums, int target) {
//	vector<int> out;
//	int check = 0;
//	for (int i = 0; i < nums.size(); i++) {
//		if (nums[i] < target){
//			for (int j = 0; j < nums.size(); j++) {
//				if (nums[j] < target) {
//					check = nums[i] + nums[j];
//					if (check == target) {
//						out.push_back(i);
//						out.push_back(j);
//						break;
//					}
//				}
//			}
//			if (check == target) {
//				break;
//			}
//		}
//	}
//	return out;
//}
//
//
//
//int main() {
//
//	vector<int> nums = { 11, 15, 2, 7 };
//	int target = 9;
//	vector<int> out;
//	out = twosum(nums, target);
//	for (auto i = out.begin(); i != out.end(); ++i)
//		cout << *i << " ";
//	return 0;
//}