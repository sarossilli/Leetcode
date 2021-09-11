class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        if(nums.size() == 1){
            return nums[0];
        }
        
        int max = nums[0], cur = nums[0];
        
        for(int i = 1; i<nums.size(); i++){
            int number = nums[i];
                
            if (cur+number<number){
                cur = number;
            }
            else{
                cur += number;
            }
            
            if (cur > max){
                max = cur;
            }
        }
        
        return max;
        
    }
};


// [-2,1,-3,4,-1,2,1,-5,4]
//   l r                    p = -2, c= -1, move r -> -4
//   l    r                 p = -1, c= -4, move l -> -2
//     l  r                 p = -4, c= -2, move r -> -4