#include <unordered_map>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        unordered_map<int, int> seen; //o(1) lookups
        vector<int> res;
        for(int i = 0; i < nums.size(); ++i) {
            int num = nums[i];
            if(seen.count(target - num)) { // if in seen
                res.push_back(i);       // add index into ans
                res.push_back(seen[target - num]); // add index of the seen that ads to target
            } else {
                seen.insert({ num, i });   //otherwise just add val to seen
            }
        }
        return res;
    }
};
