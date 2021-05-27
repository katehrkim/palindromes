// Can you translate this driver code to unit tests?

const pal = require("./palindrome");

test('one', () => {
  expect(pal('racecar')).toEqual(true);
});
test('two', () => {
  expect(pal('Noon')).toEqual(true);
});
test('three', () => {
  expect(pal('ciVic')).toEqual(true);
});
test('four', () => {
  expect(pal('nice')).toEqual(false);
});
test('five', () => {
  expect(pal(434)).toEqual(true);
});
test('six', () => {
  expect(pal(123)).toEqual(false);
});
// The following should be true if you're trying to do the extra portion of this challenge
test('seven', () => {
  expect(pal("Sore was I ere I saw Eros.")).toEqual(true);
});
test('eight', () => {
  expect(pal("A man, a plan, a canal -- Panama")).toEqual(true);
});
