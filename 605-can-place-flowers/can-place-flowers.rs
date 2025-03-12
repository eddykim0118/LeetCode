impl Solution {
    pub fn can_place_flowers(flowerbed: Vec<i32>, n: i32) -> bool {
        let mut k = n;
        let mut temp = flowerbed;
        if k == 0 {
            return true;
        }

        let length = temp.len();
        let mut i = 0;

        while i < length {
            if temp[i] == 1 {
                i += 2;
                continue;
            }

            let prev_empty = i == 0 || temp[i - 1] == 0;
            let next_empty = i == length - 1 || temp[i + 1] == 0;

            if prev_empty && next_empty {
                temp[i] = 1;
                k -= 1;

                if k == 0 {
                    return true;
                }

                i += 2;
            } else {
                i += 1;
            }
        }

        return false;
    }
}