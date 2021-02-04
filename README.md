<img height="120px" src="img/Julius-Caesar.png" />

# rot13

ROT13 ("rotate by 13 places", sometimes hyphenated ROT-13) is a simple letter [substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher) that replaces a letter with the 13th letter after it in the alphabet. ROT13 is a special case of the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) which was developed in ancient Rome. &mdash; [Wikipedia Article: ROT13](https://en.wikipedia.org/wiki/ROT13)

## Instructions
Complete the `rotate()` function inside of `rot13.py` so that it returns the message provided from the command line in its encoded/decoded form. Note that the only real difference between encoding and decoding is whether you provide an encoded or decoded message to the program. This is because you will be rotating 13 letters within the 26-letter English alphabet, so every rotation moves exactly halfway through the alphabet. (e.g., a->n->a->n->...)

This assignment will test your knowledge of strings, loops, conditionals, and general problem solving.

## Considerations
In addition to lowercase messages, your program should preserve the original case of a mixed case message (e.g., "HelLo") along with any non-letter characters such as numbers, symbols, or punctuation (e.g., "Let's rotate 13 times.").

The program requires a single command line argument in order to run.
- `message` &mdash; the message to encode or decode

## Example

### Encoding a message
```
% python rot13.py "hello"
uryyb
```

### Decoding a message
```
% python rot13.py "uryyb"
hello
```

### Encoding mixed case
```
% python rot13.py "HelLo"
UryYb
```

### Decoding mixed case
```
% python rot13.py "UryYb"
HelLo
```

### Encoding non-letter characters
```
% python rot13.py "Let's rotate 13 times."
Yrg'f ebgngr 13 gvzrf.
```

### Decoding non-letter characters
```
% python rot13.py "Yrg'f ebgngr 13 gvzrf."
Let's rotate 13 times.
```

## Notes
- When running your program from the command line as shown above, wrap your message in quotes if it contains spaces or special characters.
- Some special characters typed on the command line will be intercepted as shell operators. If your terminal behaves weird when running your program, it could be because you used a special shell operator (e.g., `!`, `` ` ``, etc.) in your message. Press Ctrl-c to return to your terminal prompt, and avoid using characters that cause that behavior.
- You can use the modulo operator (`%`) as a neat mathematical trick to put a maximum cap on a number.
- Two strings, `ascii_lowercase` and `ascii_uppercase`, have been imported from a Python module for your convenience. Take a look at them to see how they might be useful!
 
## Testing with Unittest
This assignment also has separate unit tests to help you during development. The unit tests are located in the `tests` folder; you should not modify these. Make sure all unit tests are passing before you submit your solution. You can invoke the unit tests from the command line at the root of your project folder:

    $ python -m unittest discover tests

You can also run these same tests using the `Test Explorer` extension built in to the VS Code editor by enabling automatic test discovery. This is a really useful tool and we highly recommend to learn it.

https://code.visualstudio.com/docs/python/testing#_test-discovery

- Test framework is `unittest`
- Test folder pattern is `tests`
- Test name pattern is `test*`

## Submitting your work
To submit your solution for grading, you will need to create a GitHub [Pull Request (PR)](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests). Refer to the `PR Workflow` article in your course content for details.
