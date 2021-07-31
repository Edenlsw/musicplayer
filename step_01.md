# Step 1: Get Started with Fizzbuzz

Let's start off by writing Fizzbuzz in Python. In the process, we'll set up a
new project and show you around the rudiments of the language.

As with all Makers materials, we will leave space for you to do your own
research, discovery, and experimentation. You will need to do this as part of
your job regularly, as every developer does. If you want some extra challenge,
go straight to [the exercise](#Fizzbuzz) and only return to the guidance if you
need it.

## Objectives

Learn to:
* Set up a new Python project
* Manipulate variables
* Use conditional and looping logic
* Use functions with parameters
* Test-drive using `unittest`

## Getting Started

First, I must apologise — the Python ecosystem is great, but it does have a few
quirks. I'm going to navigate you around those as best as possible, but it's
important you know about them so that you can understand what you read on the
internet.

Let's get started by typing `python` into the terminal and hitting return. You
probably see something like this:

```shell
; python

WARNING: Python 2.7 is not recommended.
This version is included in macOS for compatibility with legacy software.
Future versions of macOS will not include Python 2.7.
Instead, it is recommended that you transition to using 'python3' from within Terminal.

Python 2.7.16 (default, Dec 21 2020, 23:00:36)
[GCC Apple LLVM 12.0.0 (clang-1200.0.30.4) [+internal-os, ptrauth-isa=sign+stri on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

We're being warned that we're using Python 2.7 here, which is an old version.
For historical reasons, Python 2 and Python 3 are treated as somewhat different
languages. The migration was hard work for a lot of teams and so many people
were still using Python 2. Thankfully we are in the final stages of that now,
_but_ you will see people talking about the differences so bear that in mind. 

If you see something like `Python 3.x.x` then — congratulations on living in the
future!

So, let's go ahead and run `python3`:

```shell
; python3
Python 3.8.2 (default, Dec 21 2020, 15:06:04)
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You can play around in the REPL a bit:

```shell
>>> 2 + 3
5
>>> "Apples" + "Pears"
'ApplesPears'
>>> hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
```

However, we're not done yet. To set up a new project we'll need some tools.
Let's go ahead and install them and then I'll tell you a little about them:

```shell
; pip3 install --user pipenv
```

* `pip3` is the Python 3 version of [`pip`](https://pypi.org/project/pip/) — the
  Python package manager. We're using it to install `pipenv` for use on your
  user account (i.e. not just as a package local to this project).
* `pipenv` is an environment manager. It sets up a version and environment for
  Python for you and makes sure the packages you install are all available.
  This will also let us use newer versions of Python. Its competitors are called
  things like `venv`, `virtualenv`, `pyenv`. They're all fine, but we're going
  to use `pipenv`.

When `pipenv` is installed, run this:

```shell
; mkdir fizzbuzz
; cd fizzbuzz
; pipenv --python 3.9 # This creates a new virtual environment
# You'll see some output here that should end with 
# Successfully created virtual environment!
; pipenv shell # This is how we 'log in' to the new virtual environment
# You'll see some more messages telling you what pipenv is doing
; python --version # No need for 'python3' anymore, pipenv has it sorted.
Python 3.9.5 # Or something very similar
; ls
Pipfile
; cat Pipfile
# This file will register our dependencies when we have some.
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]

[dev-packages]

[requires]
python_version = "3.9"
```

Ready to write some code? Me too. Open up a text editor in the current directory
and let's get started.

## Greetings

Here's some Python:

```python
# For: greeter.py

# We create a method using `def`, parameters in brackets
def greet(name):  # <--  Don't forget the colon!
    print(f"Hello, {name}!")  # Note the `f` before the string here enables string
    # interpolation. Try removing it and see.


# Looking for the end?
# That's the great thing about Python: there's no end!

# Now we call the method like so:
greet("World")

```

You can run it like this:

```shell
; pipenv run python greeter.py
Hello, World!
# Or 
; pipenv shell
; python greeter.py
Hello, World!
# From now on I'll assume you know to run `pipenv shell` before
# executing Python.
```

### No end?

Python is based on a language called ABC, which was itself designed for people
who weren't really software engineers but wanted to make simple software. They
tried to design the language around the expectations of those people.

Those people were very annoyed when they missed off an `end` and then their
program did all this weird stuff they didn't want.

So ABC decided — can't miss off the ends if there _are no ends._

Instead, they designed the language around indentation. This had the additional
benefit that their users couldn't ignore good indentation and write programs
no one could ever read again. By convention Python indents by 4 spaces.

Here are some invalid programs so you get the idea:

```python
def say():
print("Nope")


say()
```

```python
def say():
    print("Nope")
     print("Not even one extra space")


say()
```

```python
def say():


# Empty methods aren't indented right, so aren't allowed
say()
```

That last one can be annoying if you genuinely do want a method that does
nothing, so if you want an empty method, you can do:

```python
def say():
    pass # Doesn't do anything, but it _is_ indented correctly


say()
```

Let's move on to Fizzbuzz.

## Fizzbuzz

Your task is to test-drive a program that takes a max number and returns a 
string. The string should list out the numbers counting up to and including the
given max number, substituting Fizz where the number is divisible by 3, Buzz 
where it is divisible by 5, and FizzBuzz where it is divisible by both 3 and 5.

Here's an example:

```
CALLING:
  fizzbuzz(15)
SHOULD RETURN:
  "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz"
```

You're going to test drive this, which will be much easier if you avoid printing
to the terminal.

Here is a starting point:

```python
# For: fizzbuzz.py
def generate(upto):
    return "1"
```

```python
# For: test_fizzbuzz.py
import unittest  # This is the default Python testing library, unittest

from fizzbuzz import generate
# We import our generate function (def) from the fizzbuzz module (file)

class TestFizzbuzz(unittest.TestCase):  # Sets up a new test case
    def test_lists_values_up_to_one(self):  # This is a test, don't forget `self`!
        self.assertEqual(generate(1), "1")  # And an assertion

    # def test_lists_values_up_to_two(self):
    #   self.assertEqual(generate(2), "1, 2")

    # Start by uncommenting the above, and when you've made that pass move 
    # forward with your own tests.

```

And you can run your tests with:

```shell
; python -m unittest
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

You're done when your code passes the following acceptance criteria:

```
CALLING:
  fizzbuzz(100)
SHOULD RETURN:
  "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, FizzBuzz, 31, 32, Fizz, 34, Buzz, Fizz, 37, 38, Fizz, Buzz, 41, Fizz, 43, 44, FizzBuzz, 46, 47, Fizz, 49, Buzz, Fizz, 52, 53, Fizz, Buzz, 56, Fizz, 58, 59, FizzBuzz, 61, 62, Fizz, 64, Buzz, Fizz, 67, 68, Fizz, Buzz, 71, Fizz, 73, 74, FizzBuzz, 76, 77, Fizz, 79, Buzz, Fizz, 82, 83, Fizz, Buzz, 86, Fizz, 88, 89, FizzBuzz, 91, 92, Fizz, 94, Buzz, Fizz, 97, 98, Fizz, Buzz"
```

### What you'll need to learn

Amongst other things, you'll need to learn:

* [How to write a test using `unittest`](https://docs.python.org/3/library/unittest.html)
* [Python functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) <!-- OMITTED -->
* [Python conditions and loops](https://docs.python.org/3/tutorial/controlflow.html)

<!-- OMITTED -->

## Done?

[Go to the next challenge](./step_02.md)


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_01.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_01.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_01.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_01.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_01.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
