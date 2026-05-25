class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int mProfit = 0;

        while (r < prices.length) {
            mProfit = Math.max(mProfit, prices[r] - prices[l]);
            if (prices[r] < prices[l]) {
                l = r;
            }
            r++;
        }

        return mProfit;
    }
}
