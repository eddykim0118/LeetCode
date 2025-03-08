impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut result = String::with_capacity(word1.len() + word2.len());
        let (word1_chars, word2_chars) = (word1.chars().collect::<Vec<_>>(), word2.chars().collect::<Vec<_>>());
        let max_len = word1.len().max(word2.len());

        for i in 0..max_len {
            if i < word1.len() {
                result.push(word1_chars[i]);
            }
            if i < word2.len() {
                result.push(word2_chars[i]);
            }
        }

        result
    }
}