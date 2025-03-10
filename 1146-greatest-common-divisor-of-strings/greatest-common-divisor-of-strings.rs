impl Solution {
    pub fn gcd_of_strings(str1: String, str2: String) -> String {
        if str1.clone() + &str2 != str2.clone() + &str1 {
            return "".to_string();
        }

        let gcd_length = Self::gcd(str1.len(), str2.len());
        str1[0..gcd_length].to_string()
    }

    fn gcd(a: usize, b:usize) -> usize {
        let mut a = a;
        let mut b = b;

        while b != 0 {
            let temp = b;
            b = a % b;
            a = temp;
        }

        a
    }
}