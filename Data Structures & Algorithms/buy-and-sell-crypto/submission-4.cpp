class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty() || prices.size() == 1) return 0;

        size_t buy_idx = 0;
        size_t sell_idx = 1;

        int max_profit = 0;
        while(sell_idx < prices.size() && buy_idx <= sell_idx){
            while(sell_idx < prices.size() && prices[buy_idx] <= prices[sell_idx]){
                max_profit = std::max(max_profit,prices[sell_idx] - prices[buy_idx]);
                sell_idx++;
            }
            buy_idx = sell_idx;
        }


        return max_profit;
    }
};
