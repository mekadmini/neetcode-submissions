class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen_numbers;
        for (int i=0; i < nums.size(); i++){
            auto it = seen_numbers.find(nums[i]);

            if (it != seen_numbers.end()){
                vector<int> result = {it->second, i};
                return result;
            }

            seen_numbers[target-nums[i]] = i;



        }
        
    }
};
