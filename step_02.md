# Step 2: Create the Music Library

You've completed Fizzbuzz, learned basic variable manipulation, conditional
logic, as well as how to use functions and unit testing. Now it's time to start
making our music player!

We'll start by making a music library.

## Objectives

Learn to:
* Test-drive classes

## Classes

Let's walk through some classes in Python:

```python
class SecretDiary:
    # __init__ is a special method name that is called
    # when a new instance is created
    def __init__(self, diary):
        #        ^^^^ `self` is the current instance
        #             It is given as the first
        #             parameter of all instance methods
        self._diary = diary
        self._locked = True
        #    ^ This `_` prefix indicates a private instance variable.

    def unlock(self):
        self._locked = False
        # Methods that don't return anything return the type `None`
        # Which is like Python's version of null or nil

    def lock(self):
        self._locked = True

    def read(self):
        if self._locked:
            return "Go away!"
        else:
            return self._diary.read()


class Diary:
    def __init__(self, contents):
        self._contents = contents

    def read(self):
        return self._contents


diary = Diary("Eric Cantona is the best footballer")
secret_diary = SecretDiary(diary)

print(secret_diary.read())
# Prints: "Go away!"

secret_diary.unlock()
print(secret_diary.read())
# Prints: "Eric Cantona is the best footballer"

```

There's nothing too unusual here. As we mentioned previously, Python is designed
to be a very straightforward and obvious language. 

## Setup

In the `seed/` directory, you'll find a Python project set up. You'll build on
this seed to complete the exercise.

Here's what it looks like:

```shell
; tree
.
├── Pipfile # Python configuration and dependencies
├── Pipfile.lock # The specific versions you've installed. Don't edit!
├── README.md # Sage guidance on how to use the program
├── data # For program data
│   └── tunes # We'll keep our mp3s in here!
├── player # This directory is another package, this one is for you.
│   ├── __init__.py # Anything directory with __init__.py in is a 'package'.
│   └── music_library.py # Source file to be used for your music library
├── tests # A package for your tests
│   ├── __init__.py  # These files are often empty.
│   └── test_music_library.py # Your test suite.
└── ui # I'll give you an interface at first, and later on you can edit.
    ├── __init__.py # Yep, another one.
    ├── __main__.py # This file gets run if we run the whole package.
    ├── interface.py # Source file for the interface
    ├── mocks.py # Mocks for use by the interface test suite
    └── test_interface.py # Test suite for the interface
```

### Packages and Modules

Directories with `__init__.py` in are known as
[**packages**](https://docs.python.org/3/tutorial/modules.html#packages). They
group related modules according to their holistic purpose. Some projects might
have many packages — some might have just one, or even none!

Python files like `interface.py` are known as
[**modules**](https://docs.python.org/3/tutorial/modules.html). Modules contain
a related set of classes and/or functions.

## Exercise

You're working for a cool new music start up called Player. You're the second
developer on the team! Exciting. The other developer, Kez, is a front-end
engineer and so has created the user interface. Take a look:

```shell
; cd seed
; pipenv install
; pipenv shell
; python -m ui
Welcome to your music library!
Enter:
  a: to add a track
  d: to delete a track
  l: to list your tracks
  q: to quit
What do you pick? a
What's the title? The Rest of Us Still Care
What's the artist? Hood
Traceback (most recent call last):
  File "/usr/local/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/local/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File ".../seed/ui/__main__.py", line 4, in <module>
    interface.run()
  File ".../seed/ui/interface.py", line 20, in run
    music_library.add(f"{title} by {artist}")
AttributeError: 'MusicLibrary' object has no attribute 'add'
```

The problem is that there's no back-end yet. That's your job!

Test-drive the `MusicLibrary` class in `player/music_library.py` to implement
`add`, `remove`, and `all` methods that behave like this:

```python
>>> music_library = MusicLibrary()
>>> music_library.add("Rolling Blackouts by The Go! Team")
None
>>> music_library.add("Oh Yeah by Locust")
None
>>> music_library.add("Sleep on the Wing by Bibio")
None
>>> music_library.all()
["Rolling Blackouts by The Go! Team", "Oh Yeah by Locust", "Sleep on the Wing by Bibio"]
>>> music_library.remove(1) # Removes track 1
True # Returns True on successful removal
>>> music_library.remove(20) # If you remove a track that doesn't exist...
False # It should return False
>>> music_library.all()
["Rolling Blackouts by The Go! Team", "Sleep on the Wing by Bibio"]
```

Write your tests in `tests/test_music_library.py`. The UI test suite won't pass
until you've implemented all of the above, so to ignore those run your tests
with like so:

```shell
; python -m unittest discover tests
```

When you're done, you can run the full test suite with:

```shell
; python -m unittest
```

And see the interface work like this:

```shell
; python -m ui
```

## Done?

[Go to the next challenge](./step_03.md)


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_02.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_02.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_02.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_02.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_02.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
