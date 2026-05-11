class Solution {
public:
    int maxProfit(vector<int>& prices) {

        // by low sell high to create highest profit
        // minimum will always be seen before the next current max
        // (if that makes sense)
        
        // maintain our current highest profit
        int curr = 0;

        // maintain a global minimum (highest will be 100)
        int globMin = prices[0];

        // start from first index to be able to calculate a diff. on the 
        // on the first iteration
        for (int i = 1; i < prices.size(); i++) {

            // calculate new global minimum (wont be lower than 0)
            globMin = globMin > prices[i] ? prices[i] : globMin;

            // update best current profit
            curr = (prices[i] - globMin) > curr ? (prices[i] - globMin) : curr;
        }

        return curr;

    }
};
