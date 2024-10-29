function generateHashtag(str) {
  // Remove extra spaces, split by spaces, capitalize each word, and join them
  const hashtag = "#" + str
    .trim()
    .split(/\s+/)
    .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join("");

  // Check if the result is a valid hashtag and not too long
  return hashtag.length > 1 && hashtag.length <= 140 ? hashtag : false;
}

// Test cases
console.log(generateHashtag(" Hello there thanks for trying my Kata")); // "#HelloThereThanksForTryingMyKata"
console.log(generateHashtag("    Hello     World   ")); // "#HelloWorld"
console.log(generateHashtag("")); // false
