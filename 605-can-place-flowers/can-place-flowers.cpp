class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if (n == 0) {
            return true;
        }

        int i = 0;
        int length = flowerbed.size();

        while (i < length) {
            if (flowerbed[i] == 1) {
                i += 2;
                continue;
            }

            if ((i == 0 || flowerbed[i - 1] == 0) && (i == length - 1 || flowerbed[i + 1] == 0)) {
                flowerbed[i] = 1;
                n--;

                if (n == 0) {
                    return true;
                }

                i += 2;
            } else {
                i++;
            }
        }
        return false;
    }
};