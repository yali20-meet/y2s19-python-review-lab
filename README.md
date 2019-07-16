## Y2 2019 Summer: Python Cipher Lab

Welcome to the Python Cipher lab! Please read all the instructions so you don't
get lost halfway through, but definitely feel free to ask for help if you
get stuck. Good luck, and have fun!

### Part 1: Basic functions

The stubs for these functions can be found in `part1.py`. You can test your functions by running `part1-test.py`.

1. Write a function to `hello_world`, which takes in no inputs
and returns `hello world`. 

2. Write a function `greet_by_name` which takes in a string, `name`,
and returns `hello <name>`

3. Write a function, `encode`, that takes in a number, `x` and returns
the product of `x` and 3953531.

4. Write a function, `decode`, which takes in the output from the previous function and
finds `x`. You may use the value 3953531 in this function.

5. Ask for a checkoff from an instructor or TA.

### Part 2: Loops

The stubs for these functions can be found in `part2.py`.

1. First, update your function `encode`, to take in 2 numbers `x` and `y`, and compute their product.
This function should require `1 < y < 250` and `500 < x < 1,000`. If this isn't true, the function should print
`Invalid input: Outside range.`, and return None.

2. Update your encode function to guarantee that the inputs `x` and `y` are prime. If `x` is not prime,
then keep incrementing the value of `x` until it is prime; then, do the same process for `y`. If this
causes the new values of `x` and `y` to be out of the range, print `Invalid input: Outside range.`,
and return None.

3. Write a function, `decode`, which takes in the output (the value of the product)
from your updated `encode` function and tries to compute values for `x` and `y`.
This function only takes in, as input,
the `coded_message`, which is output from `encode`. You may also use the ranges of possible values for `x` and `y` - that is, `1 < y < 250` and `500 < x < 1,000`.
Consider trying all possible values for `x` and `y`!
*Hint: The mod function might be useful here! The mod function can be used to calculate the remainder.
For instance, `500 % 6` returns the remainder when 500 is divided by 6.*

4. A good programmer always writes test cases! Test your `encode` and `decode` functions to
make sure they work in `part2-test.py`. Make sure to include test cases for all possible cases of x and y. Note that the `encode` function changes your input to make sure that it's prime. Thus, if your original input was not prime, `decode(encode(x, y))`, might not return the original values of `x` and `y`. Make sure you account for this when writing test cases.

5. Ask for a checkoff from an instructor or TA.

### Part 3: Dictionaries

The stubs for these functions can be found in `part3.py`. For this section, we wrote the test cases for you. You can test your functions by running `part3-test.py`.

1. In cryptography, the easiest form of cipher is known as a Caesar cipher. In a Caesar cipher, we encode letters by shifting the characters in the alphabet by some value. For this first exercise, write a function that returns a dictionary mapping lowercase letters to lowercase letters based upon some shift s. For example, if we shift the alphabet by 3, `a`s get mapped to `d`s, `b`s to `e`s, ... `z`s to `c`s. You can use the two dictionaries given in the script.

2. Use the function you wrote in the previous step to encodes a plaintext string given some shift s. You can assume that the entire string is in lowercase and ignore punctuation. Make sure to return the ciphertext.

3. Use the function you wrote in step 1 to write a decode function that takes in the ciphertext and some shift s to produce the plaintext. Make sure to return the plaintext.

4. Uh oh! You lost the shift s for your cipher. Write a function that returns all possible plaintexts for your ciphertext in a list. Try swapping ciphertexts with a friend and look through all the possible plaintexts to guess their meaning.

5. Ask for a checkoff from an instructor or TA.

### BONUS:

Read about Vignere ciphers here: http://www.crypto-it.net/eng/simple/vigenere-cipher.html?tab=1.

Implement Vignere cipher encode and decode functions. Remember that your encode function must take in both a plaintext string and a keyword. Make sure your keyword is short (less than 10 characters). Your decode function should also take in a ciphertext string and a keyword. Also, be sure to write test cases for your functions!

Alternatively, research and implement a different cipher of your choice.