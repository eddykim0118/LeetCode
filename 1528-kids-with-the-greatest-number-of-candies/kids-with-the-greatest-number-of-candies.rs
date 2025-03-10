impl Solution {
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
        let most = *candies.iter().max().unwrap();
        candies.iter().map(|&candy| candy + extra_candies >= most).collect()
    }
}