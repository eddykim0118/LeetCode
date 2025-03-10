function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
    const most = Math.max(...candies);
    return candies.map(candy => candy + extraCandies >= most);
};