function palindrome(word) {
  if (typeof word == "string") {
    word = word.toLowerCase();
  }
  if (typeof word == "number") {
    word = word.toString();
  }
  let cleaned = word.replace(/[.,\/#!$% \^&\*;:{}=\-_`~()]/g,"");
  let half_len = Math.floor(cleaned.length / 2);
  for (let i = 0; i < half_len; ++i) {
    if (cleaned[i] != cleaned[cleaned.length - 1 - i]) {
      return false;
    }
  }
  return true;
};

module.exports = palindrome;