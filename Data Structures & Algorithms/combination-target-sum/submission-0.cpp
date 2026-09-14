class Solution {
public:

    void helper(vector<int>& candidates,
                vector<vector<int>>& ans,
                vector<int>& temp,
                int start,
                int target)
    {
        if (target == 0)
        {
            ans.push_back(temp);
            return;
        }

        for (int i = start; i < candidates.size(); i++)
        {
            if (candidates[i] > target)
                continue;

            temp.push_back(candidates[i]);

            helper(candidates,
                   ans,
                   temp,
                   i,
                   target - candidates[i]);

            temp.pop_back();
        }
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target)
    {
        vector<vector<int>> ans;
        vector<int> temp;

        helper(candidates, ans, temp, 0, target);

        return ans;
    }
};