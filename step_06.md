# Step 6: Make it Yours

The application is now yours to develop as you see fit. Here are some pathways
you might choose depending on what you want to learn, how much challenge you
want to take on, and how much structure or freedom you would like. Tackle them
in any order you like — you almost certainly won't complete them all.

* **[Refactor Track Formatting.](#refactor-track-formatting)**
  Kez has left a lot of repetition when it comes to generating 'Song by Artist'
  strings. Let's fix that. You'll get your hands dirty modifying the interface
  and tests, and learn some Python best practices.

* **[Refactor search even further.](#refactor-search-even-further)**  
  We've still got a big block of `elifs` in `interface.py` — what can we do
  about that? You'll learn more about functional programming in Python.

* **[Allow the user to play tracks by searching for
  them.](#allow-the-user-to-play-tracks-by-searching-for-them)**  
  To develop your understanding of the user interface code and tests, and
  improve your refactoring skill in Python.

* **[Add summary statistics about which artists are in the
  library.](#add-summary-statistics-about-which-artists-are-in-the-library)**  
  To learn about working with Python dictionaries (known in other languages as
  maps, hashes, or associative arrays).

* **[Automatically detect track information just by giving the file
  path.](#automatically-detect-track-information-just-by-giving-the-file-path)**  
  To learn about installing packages in Python and develop your mocking skills.

* **[Show a song playing progress bar.](#show-a-song-playing-progress-bar)**  
  To learn about threads and background processing in Python.

* **[Implement shuffle.](#implement-shuffle)**  
  To learn about randomness and stubbing it out in your tests.

* **[Store the music library.](#store-the-music-library)**  
  To Learn about file and/or database access using Python.

* **[Implement playlists.](#implement-playlists)**  
  Take on a complex and challenging task in Python.

## Refactor Track Formatting

Take a look at the method `#_play_track` in `ui/interface.py`. It contains a
line like this:

```python
self.console.print(f"Playing {track.title} by {track.artist}...")
```

There are quite a few places where messages like "Song by Artist" are generated.
There is an opportunity to refactor this out into the `Track` class.

Python has a tool for situations like this — where we want a class to have a
human-friendly string representation. It's called `__str__`, or sometimes "the
string dunder (double underscore) method".

It works like this:

```python
class DiaryEntry:
    def __init__(self, time, contents):
        self.time = time
        self.contents = contents

    def __str__(self):
        return f"({self.time}) {self.contents}"


diary_entry = DiaryEntry("12:00", "Time to get some tunes on!")
print(f"Here's a diary entry: {diary_entry}")

# Prints:
# Here's a diary entry: (12:00) Time to get some tunes on!
```

Use this technique to extract the repetition of `{track.title} by
{track.artist}` out of `ui/interface.py`.

<!-- OMITTED -->

## Refactor search even further

Right now, your search interface probably looks something like this:

```python
library.search(lambda track: 'D.A.N.C.E.' in track.title)
```

This is OK, but as the codebase grows you're going to end up with loads of
lambdas all over the place which may work in subtly different ways. Users might
find that sometimes their searches are case sensitive, and sometimes they
aren't, depending on whether the programmer remembered to downcase everything
properly.

What if we could do this?

```python
library.search(Searchers.by_title_case_insensitive('D.A.N.C.E.'))
```

Nice, right? I'm going to show you how to do this refactor in stages. Let's
start with a case insensitive version of the first example.

```python
query = "D.A.N.C.E."
library.search(lambda track: query.lower() in track.title.lower())
```

Let's move that lambda into a variable:

```python
query = "D.A.N.C.E."
searcher = lambda track: query.lower() in track.title.lower()
library.search(searcher)
```

And then extract a function:

```python
def search_for_my_favourite_track():
    query = "D.A.N.C.E."
    return lambda track: query.lower() in track.title.lower()


searcher = search_for_my_favourite_track()
library.search(searcher)
```

And then extract the query variable as a parameter:

```python
def search_for_my_favourite_track(query):
    return lambda track: query.lower() in track.title.lower()


searcher = search_for_my_favourite_track("D.A.N.C.E.")
library.search(searcher)
```

And rename the function to make it more appropriate:

```python
def search_by_title_case_insensitive(query):
    return lambda track: query.lower() in track.title.lower()


library.search(search_by_title_case_insensitive("D.A.N.C.E."))
```

Pretty close! Let's review how this works: we've got a function which... returns
another function, which we then give to `search` to use to filter the library.

Functions that return other functions are called [Higher Order
Functions](https://en.wikipedia.org/wiki/Higher-order_function). They're a very
powerful functional programming technique.

To get to our original intention, we finally need to extract
`search_by_title_case_insensitive` to another module.

```python
# Into: player/search.py

def by_title_case_insensitive(query):
    return lambda track: query.lower() in track.title.lower()
```

```python
# To call it:

import searchers as Searchers
from player.music_library import MusicLibrary, Track

lib = MusicLibrary()
lib.add(Track("D.A.N.C.E.", "Justice", "dance.mp3"))
lib.add(Track("My Favourite Game", "The Cardigans", "game.mp3"))
lib.add(Track("Feel Good Inc.", "Gorillaz", "feelgood.mp3"))
lib.search(Searchers.by_title_case_insensitive("D.A.N.C.E."))
```

### Exercise

#### Part One

Refactor your search implementation to use the above pattern. Add any other
searching methods you'd like (perhaps a case sensitive one).

See how clean you can get `Interface#_search_tracks`.

#### Part Two (Optional & Challenging)

You probably have some repetition where searching by any field involves a big
`or` expression with all of the other queries in it. Can you think of a way to
refactor it to use the other functions instead?

#### Part Three (Optional & Challenging)

It's annoying to have case sensitive and insensitive versions of all the
searchers. Imagine if we could do this:

```python
def ByTrackTitle(query):
    return lambda track: query in track.title


def _insensitive(searcher):
    return  # ???


by_title_case_insensitive = _insensitive(ByTrackTitle)
```

Is this just some code-fuelled fantasy? Or can it be done?

## Allow the user to play tracks by searching for them

Here's the interface you should be aiming for:

```shell
; python -m ui
Welcome to your music library!
# You add some tracks
Enter:
  a: to add a track
  p: to play a track
  d: to delete a track
  l: to list your tracks
  s: to search your tracks
  q: to quit
What do you pick? p
Search by:
  t: title
  a: artist
  f: file
  *: anything
What do you want to search by? *
What do you want to search for? 
1. Northfield, MN by Casiotone for the Painfully Alone @ northfield.mp3
2. It's Grim Up North by The KLF @ north.mp3
Which do you want to play? 2
Playing It's Grim Up North by The KLF...
```

You could do this with a big copy-paste fest. That's OK to start, but can you
see a way to reuse your existing searching, listing, and playing methods?

## Add summary statistics about which artists are in the library

Looking forward to [Spotify Wrapped](http://spotify.com/wrapped/) this year? I
am. We're probably not going to make anything _that_ sophisticated, but it'd be
nice to see a breakdown of the artists in our library. Something like this:

```shell
; python -m ui
Welcome to your music library!
# You add some tracks
Enter:
  a: to add a track
  p: to play a track
  d: to delete a track
  l: to list your tracks
  s: to search your tracks
  S: to summarise your top 15 artists
  q: to quit
What do you pick? S
1. Piano Magic: 217 tracks
2. Bright Eyes: 181 tracks
3. Radiohead: 174 tracks
4. Bibio: 154 tracks
5. Casiotone for the Painfully Alone: 129 tracks
6. Broadcast: 126 tracks
7. The Avalanches: 102 tracks
8. Boards of Canada: 101 tracks
9. Misophone: 100 tracks
10. U4ia: 96 tracks
11. The Books: 95 tracks
12. Vegyn: 93 tracks
13. Islands: 92 tracks
14. Aphex Twin: 92 tracks
15. cLOUDDEAD: 89 tracks
```

Think a bit about how to achieve that. You'll probably need to learn about
[Python
dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
and perhaps [Python
tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences). Consider
carefully how you want to build this into the system — what would a good Object
Oriented developer do?

## Automatically detect track information just by giving the file path

Most music files contain metadata. That metadata contains information
identifying the artist, track title, year of release and so on.

It would be pretty great to use that metadata if it is present, instead of
forcing our users to type it in manually.

To do this, you'll need to:

* Take a breeze through [this archive of free
  music](https://freemusicarchive.org/) until you find something you like the
  sound of. Download it, and use it as your test file.
* Install the [`eyed3`](https://github.com/nicfit/eyeD3) module using
  [`pipenv`](https://pipenv-fork.readthedocs.io/en/latest/basics.html)
* Try it out with your test file using the docs available for `eyed3`.
* Test-drive integrating it into your app. 
* Apply your mocking skills to isolate your unit tests from `eyed3`.
* Take not that not all tracks will have metadata, so you may want to give the
  user the option of not using it.

## Show a song playing progress bar

<!-- OMITTED -->


Right now, when you play a song, the interface is:

```shell
Playing It's Grim Up North by The KLF...
# silently waits for however long it takes to play the song...
Done.
```

Let's implement a progress meter. You can design it however you like.

You will encounter the challenge that while your program is running `afplay` it
can't do anything else. You'll need to find a way to run `afplay` 'in the
background', know if it has completed, and perhaps have some idea how long it
will run for. Some search keywords are 'fork', 'run background process', 'don't
wait for `subprocess`'.

This will be a real challenge — good luck!

## Implement shuffle

<!-- OMITTED -->

You can't live without a shuffle when the moment strikes. Here's an interface to
aim for:

```shell
; python -m ui
Welcome to your music library!
# You add some tracks
Enter:
  a: to add a track
  p: to play a track
  z: to play all your tracks on shuffle
  d: to delete a track
  l: to list your tracks
  s: to search your tracks
  q: to quit
What do you pick? z
Playing It's Grim Up North by The KLF...
Done.
Playing Northfield, MN by Casiotone for the Painfully Alone...
Done.
# Keeps on shuffling...
```

To implement the latter, you'll need to:

* Learn how to shuffle a list in Python.
* Use that in combination with the music player to play tracks in sequence.
* Learn how to mock that behaviour to ensure your tests are still deterministic
  and don't randomly pass or fail.

## Store the music library

<!-- OMITTED -->

Putting in all the tracks every single time is going to annoy the users, and is
probably already annoying you. Is there a way you can store the music library
and load it in when the application is run?

To implement this you'll need to decide how to store data. Here are two
possibilities:

1. Store them in a list in a file.
2. Store them in an SQL database.

What do you think the pros and cons are? Which path will provide more useful
learning to you? Decide on this basis.

## Implement playlists

<!-- OMITTED -->

Users often like to curate playlists of their music. Add this to your app.
You'll need to consider the following questions:

1. How should playlists be created?
2. Should they be saved? If so, how?
3. How do they fit into the current user interface?
4. How will you model them in your application? What classes will you have? In
   which modules will you put them? What methods should they have?

## Done?

Much like Ruby, Python has a nuanced and deliberate design philosophy which it
has brought to our industry. This is summed up in a secret feature included with
the Python interpreter. You can access it by running:

```shell
; python
>>> import this
```

I hope you've enjoyed it — Pyth-on!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_06.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_06.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_06.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_06.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_06.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
