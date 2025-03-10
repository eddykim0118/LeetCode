/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    if (str1 + str2 !== str2 + str1) {
        return "";
    }

    const gcdLength = gcd(str1.length, str2.length);

    return str1.substring(0, gcdLength);
};

/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */

 function gcd(a, b) {
    while (b !== 0) {
        const temp = b;
        b = a % b;
        a = temp;
    }

    return a;
 }