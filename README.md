# soteris_anagram

## Setup
```sh
# Install dependencies
pipenv install --dev # python3.8

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Testing
```sh
pipenv run pytest --cov --cov-fail-under=90
```

## A sample program
Run `pipenv run python`, then you can do this from the py-shell
```Python
from soteris_anagram.anagram_game import AnagramGame
game = AnagramGame() # This initial load can take several seconds. It could be accelerated by pre-serializing the dictionary mappings and histograms, etc
p = game.get_puzzle(2) # 2 is the difficulty. 0-9 should work
print("Your anagram is: ", p.word)
print(p.check_answer("racecar"))
print(p.is_trick())

tp = game.get_trick_puzzle(2) # 2 is the difficulty. 0-9 should work
print("Your anagram is: ", tp.word)
print(tp.check_answer("racecar")) # Always false
print(tp.is_trick()) # True
```


## Credits
This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.




## Choices
2 points of ambiguity:

### Difficulty levels
"Difficulty" is hard to quantify, but we have several knobs available to us:
##### Word length
This is intuitive. The longer the word, the harder it is to fit permutations in your head.
##### Number of solutions
This is also intuitive. A long word with many solutions makes it more likely the user will find one.
##### Permutation 'distance' from solutions
Rather than spend a bunch of time learning about various text distance algos, I opted for a pluggable library making this decision very flexible. See https://pypi.org/project/textdistance/. We're running with Hamming for now.

Combining these factors is somewhat difficult:
Word length and number of solutions we precalculate, so these are quite usable. Calculating permutation string distance ahead of time will take a prohibitively long time (n (words) * m (wordlen)!), so we don't do that ahead of time and don't use it in our initial difficulty allocation, but we do use it to make the anagram puzzles we choose more difficult.

#### The Combined Solution

Distributions of word lengths by index:
[0, 52, 126, 1046, 3868, 8110, 14759, 21264, 27856, 30824, 29927, 25533, 20200, 14814, 9695, 5881, 3342, 1792, 832, 421, 195, 78, 39, 17, 5

Distributions of answers by index:
[0, 208486, 9987, 1637, 395, 119, 32, 15, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

To combine them, we normalize each metric by calculating a percentile from a sample, then we can weight each metric and divide by the sum of the weights to
get a normalized percentile, multiplying by 10 and rounding down should get us a number 0-9

Approximate ending normalized distribution of difficulties:
[4909, 3945, 24484, 46061, 30099, 29270, 45108, 30161, 6639, 0]

### Unsolvable puzzles that "seem solvable"

Simplest answer here is probably to take a set of common letters, remove one from the set, try adding it,
see if we have a word, if not, use it, if we do, remove that letter and try again. This process could fail,
in which case we just grab another word.


## Possible extensions
Session based caches of prior puzzles to avoid repeats
