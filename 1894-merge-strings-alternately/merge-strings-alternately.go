func mergeAlternately(word1 string, word2 string) string {
    maxLen := len(word1)
    if len(word2) > maxLen {
        maxLen = len(word2)
    }

    result := make([]byte, 0, len(word1) + len(word2))

    for i := 0; i < maxLen; i++ {
        if i < len(word1) {
            result = append(result, word1[i])
        }

        if i < len(word2) {
            result = append(result, word2[i])
        }
    }

    return string(result)
} 