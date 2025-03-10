func kidsWithCandies(candies []int, extraCandies int) []bool {
    most := candies[0]
    for _, candy := range candies {
        if candy > most {
            most = candy
        }
    }

    result := make([]bool, len(candies))

    for i, candy := range candies {
        result[i] = candy + extraCandies >= most
    }

    return result
}

