# Step 5: Add Search

This is fine for a small number of tracks, but the original iPod could store one
thousand songs! Just listing them out wouldn't be manageable.

We're going to add search, and in the process we'll touch on applying functional
programming in python.

## Objectives

Learn to:
* Use Python Lambdas.

## Filtering

### In the Functional Style

Our basic task is to filter a list of tracks so we only get the ones we want.
If we've just bought Weezer's back catalogue but we really want to listen to 
CAKE, we'll want to filter through our library for just songs with the artist
CAKE.

So let's look at a few ways to filter lists. We'll use the example of trying to
get only the odd numbers out of a list of numbers.

Here's one way:

```python
numbers = [1, 2, 3, 4, 5]
odd_numbers = []

for number in numbers:
    if number % 2 == 1:  # Remember `%` means 'remainder when divided by' (modulo)
        odd_numbers.append(number)

print(odd_numbers)
# => [1, 3, 5]
```

The above program is written in an _imperative_ style. That means it works by
using loops and ifs to change the state (variables) of the program until it
produces the correct result. In this case, the program loops over `numbers` and
changes the contents of `odd_numbers`.

### In the Functional Style

Here's another approach:

```python
numbers = [1, 2, 3, 4, 5]

# We'll use the `filter` function.
# It takes two arguments, a lambda and a list.
odd_numbers = filter(
    lambda number: number % 2 == 1,  # A Lambda is a small function with no name.
                                     # In this case, it takes a number as an
                                     # argument and returns True if it is odd or
                                     # False if it is even.
    numbers,  # And here's our list of numbers.
)
# `filter` will
#   1. Execute the lambda for each number in the list
#   2. If the lambda returns True, it will keep the item
#   3. If the lambda returns False, it will discard the item
#   4. It will return a new list* with all the kept items.

# This could have been on one line too, I just broke it out for you to read.

print(list(odd_numbers))
# => [1, 3, 5]

# Note: `filter` actually returns an iterable, which acts very similarly to a
# list. We need to convert it into a list in order to print it properly.
# We do this with `list()`. You won't need to do this most of the time.
```

The above is in a more _functional_ style. It does its job by creating and 
applying functions — in this case a lambda function.

### Using List Comprehensions

<!-- OMITTED -->

Here's another way:

```python
numbers = [1, 2, 3, 4, 5]

odd_numbers = [number for number in numbers if number % 2 == 1]

print(odd_numbers)
```

This is also a typical functional approach, but it uses a Python feature called
_list comprehensions._ We won't dig too much into those just now, but it's 
important you can recognise them when you encounter them. Here's a brief
schematic:

```python
def square_all_odd_numbers(numbers):
    return [                # Create a list by:
        number**2             # Evaluating this expression
        for number            # For every item, which we'll call `number`
        in numbers            # In the list called `numbers`
        if number % 2 == 1    # Where that number is odd
    ]


print(square_all_odd_numbers([1, 2, 3, 4, 5]))
# => [1, 9, 25]
```

The python
[docs](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
describe this syntax as 'concise and readable'. We can certainly see that it is
concise — readable depends on what you're used to. When you get used to this
syntax you will probably find it very readable — in any case, it is widely used
in Python and so worth learning.

## Implementing Search

We're going to use a functional approach to implement our search. Why? Let's
first talk about the specification based on the latest user interface.

```shell
# We want to implement the ability to search our music library by title, artist,
# file, or all of the above depending on what the user chooses.
; python -m ui
Welcome to your music library!
# Add some tracks etc
Enter:
  a: to add a track
  p: to play a track
  d: to delete a track
  l: to list your tracks
  s: to search your tracks
  q: to quit
What do you pick? s
Search by:
  t: title
  a: artist
  f: file
  *: anything
What do you want to search by? t
What do you want to search for? letter
1. Friend Is A Four Letter Word by CAKE @ friend.mp3
2. Dead Letters by P.S. Eliot @ dl.mp3
3. Letters '98 by Havergal @ 98.mp3
```

And let's try a naïve imperative implementation:

```python
class MusicLibrary:
    def __init__(self):
        self._tracks = []

    # ... omitted other methods

    def search(self, field, query):
        query = query.lower()
        found = []
        for track in self._tracks:
            if field == "title" and query in track.title.lower():
                #                         ^^
                # The 'substring in string' operator returns true if `substring` exists
                # within `string`. So:
                #  'cat' in 'a cat is nice' is True, whereas
                #  'dog' in 'a cat is nice' is False
                found.append(track)
            elif field == "artist" and query in track.artist.lower():
                found.append(track)
            elif field == "artist" and query in track.file.lower():
                found.append(track)
            elif (
                field == "any"
                and (query in track.title.lower())
                or (query in track.artist.lower())
                or (query in track.file.lower())
            ):
                found.append(track)
        return found


# Usage:
lib = MusicLibrary()
lib.add(Track("Dead Letters", "P.S. Eliot", "dl.mp3"))
lib.add(Track("Friend Is A Four Letter Word", "CAKE", "friend.mp3"))
lib.add(Track("Letters '98", "Havergal", "98.mp3"))
lib.search("title", "Dead")
```

This has a few disadvantages:

1. It's pretty long and unwieldy.
2. If we want to add more criteria, this string of else ifs will get longer and
   longer. If you've ever done the Gilded Rose exercise, you'll know the result.
3. We're passing strings around to dictate the type of query, which will be
   harder to refactor since if you need to change the format, you'll need to
   search the codebase for `"title"` and hope you catch them all.

Let's try using a list comprehension:

```python
    def search(self, field, query):
        query = query.lower()
        if field == "title":
            return [track for track in self._tracks if query in track.title.lower()]
        elif field == "artist":
            return [track for track in self._tracks if query in track.artist.lower()]
        elif field == "file":
            return [track for track in self._tracks if query in track.file.lower()]
        elif field == "any":
            return [
                track
                for track in self._tracks
                if (query in track.title.lower())
                or (query in track.artist.lower())
                or (query in track.file.lower())
            ]
```

Or `filter`?

```python
    def search(self, field, query):
        query = query.lower()
        if field == "title":
            return filter(lambda track: query in track.title.lower(), self._tracks)
        elif field == "artist":
            return filter(lambda track: query in track.artist.lower(), self._tracks)
        elif field == "file":
            return filter(lambda track: query in track.file.lower(), self._tracks)
        elif field == "any":
            return filter(
                lambda track: (query in track.title.lower())
                or (query in track.artist.lower())
                or (query in track.file.lower()),
                self._tracks,
            )
```

Are either of those better? Only marginally. They're a tiny bit shorter, but
both still have all of the above problems.

A seasoned functional programmer would notice that there are only a few things
that really differentiate the branches:

1. The field string, which we don't really like anyway.
2. The contents of the lambda.

If, instead of this, we pass in a lambda to do the filtering, we get:

```python
    def search(self, condition):
        return filter(condition, self._tracks)


# Usage:
from player.music_library import MusicLibrary, Track

lib = MusicLibrary()
lib.add(Track("Dead Letters", "P.S. Eliot", "dl.mp3"))
lib.add(Track("Friend Is A Four Letter Word", "CAKE", "friend.mp3"))
lib.add(Track("Letters '98", "Havergal", "98.mp3"))
lib.search(lambda track: "dead" in track.title.lower())
```

What a result! The advantages:

1. The `search` method is much more concise and readable.
2. It's also much less likely to need to change, meaning less work for the devs.
3. And it's much more powerful. Users of `MusicLibrary` can now get it to search
   case sensitively, by totally new fields yet to be invented, or whatever they
   like.

There is one disadvantage, which is that you may find custom lambdas popping up
all over the code. Any ideas what could improve that? You'll have the
opportunity to improve that later in the module.

## Exercise

Good news! Kez has won the lottery and is off on a round-the-world cruise. That
means the user interface is now yours to maintain.

Kez did leave you with some pointers though. Copy in
[`interfaces/step_05/ui`](./interfaces/step_05) to your project and get started.

### Part One

Test-drive a new `search` method in `MusicLibrary` that takes a lambda as an
argument and uses it to filter the tracks as above. Don't touch the UI yet.

### Part Two

Open up `ui/interface.py`. You'll see some `TODO` markers. Implement those.

Kez has already written some tests for you. Once you've implemented the
functionality effectively throughout, the interface tests should pass:

```shell
python -m unittest discover ui
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

### Part Three

List comprehensions are considered to be more
[idiomatic](https://softwareengineering.stackexchange.com/questions/94563/what-is-idiomatic)
than `filter` in Python.

Refactor `MusicLibrary#search` to use a list comprehension instead of `filter`.

## Done?

[Go to the next challenge](./step_06.md)


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_05.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_05.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_05.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_05.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_05.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
