#include <unordered_set>
using namespace std;
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) { 
        unordered_set<int> hashSet;

        for(int i = 0; i < nums.size();i++){
            int currentNumber = nums.at(i);
            if(hashSet.find(currentNumber) != hashSet.end()){
                return true;
            }
            hashSet.insert(currentNumber);
        }
    return false;
    }

};
