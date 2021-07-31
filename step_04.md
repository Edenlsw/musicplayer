# Step 4: Play Some Tunes

Nothing like a few tunes to soundtrack your coding session right? Let's get
playing. But we can't have our tests playing music — that would cause a huge
racket around the office. So we'll need to learn how to use mocking to isolate
our tests from their dependencies

## Objectives

Learn to:
* Test classes in isolation using mocks

## Mocking

Let's take another look at the Secret Diary example:

```python
class SecretDiary:
    def __init__(self, diary):
        self._diary = diary
        # ^^^ Note that we've already injected our diary dependency here.
        # You'll need to do that in order to mock. If SecretDiary references the
        # Diary class directly, it's going to be pretty hard to isolate them.
        self._locked = True

    def unlock(self):
        self._locked = False

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

And put some tests together for `SecretDiary`:

```python
import unittest
from diary import SecretDiary, Diary


class TestSecretDiary(unittest.TestCase):
    def test_refuses_to_read_when_locked(self):
        diary = Diary("My Secret Information!")
        subject = SecretDiary(diary)
        self.assertEqual(subject.read(), "Go away!")

    def test_reads_when_unlocked(self):
        diary = Diary("My Secret Information!")
        subject = SecretDiary(diary)
        subject.unlock()
        self.assertEqual(subject.read(), "My Secret Information!")
```

This is OK — but what if Geoff comes in and breaks the `Diary` class? Then my
tests for `SecretDiary` will fail even though _I didn't do anything wrong._

We can fix this by mocking out `Diary` class, so that our tests for
`SecretDiary` aren't dependant on `Diary` at all.

Here's one way to do it:

```python
import unittest
from diary import SecretDiary


class TestSecretDiary(unittest.TestCase):
    def test_refuses_to_read_when_locked(self):
        mock_diary = MockDiary()  # We create a MockDiary instead of a Diary
        subject = SecretDiary(mock_diary)
        self.assertEqual(subject.read(), "Go away!")
        # And for good measure let's check our mock hasn't been called
        self.assertFalse(mock_diary.has_been_read)

    def test_reads_when_unlocked(self):
        mock_diary = MockDiary()
        subject = SecretDiary(mock_diary)
        subject.unlock()
        self.assertEqual(subject.read(), "Mocked diary contents")
        self.assertTrue(mock_diary.has_been_read)


# We create a mock class for Diary. It has the same methods, but it doesn't do
# anything except keep track of whether it has been called.
class MockDiary:
    def __init__(self):
        self.has_been_read = False

    def read(self):
        self.has_been_read = True
        return "Mocked diary contents"
```

We've now fully isolated `SecretDiary` from `Diary`. Geoff is powerless to
intervene. Try deleting the `Diary` class to prove it!

Here's another way, using the Python [`unittest.mock`
library](https://docs.python.org/3/library/unittest.mock.html):

```python
import unittest
from unittest.mock import Mock
from diary import SecretDiary


class TestSecretDiary(unittest.TestCase):
    def test_refuses_to_read_when_locked(self):
        mock_diary = Mock()
        subject = SecretDiary(mock_diary)
        self.assertEqual(subject.read(), "Go away!")
        mock_diary.read.assert_not_called()

    def test_reads_when_unlocked(self):
        mock_diary = Mock()
        mock_diary.read = Mock(return_value="Mocked diary contents")
        subject = SecretDiary(mock_diary)
        subject.unlock()
        self.assertEqual(subject.read(), "Mocked diary contents")
        mock_diary.read.assert_called()
```

They work in a similar way. Pick whichever approach feels better to you for now.

<!-- OMITTED -->

## Playing

There's a shell command on Macs called `afplay`. We'll use that to play our
sound files.

In [`interfaces/step_04`](./interfaces/step_04) you'll find a new `data` 
directory to paste into your project. Once it's there, run this in the terminal:

```shell
; afplay data/tunes/myfav.wav
```

You should hear a lovely tone.

To do the same in a Python project, you'll need to do something like:

```python
import subprocess

subprocess.call(["afplay", "data/tunes/myfav.wav"])
```

## Exercise

Kez has developed yet another version of the interface for you in
[`interfaces/step_04`](./interfaces/step_04). Copy it into your project.

Your task is to test-drive a `MusicPlayer` class in a new package at
`player/music_player.py`. It should have a method called `play` which takes one
string argument which is a path to a sound file. It then plays the file using
`subprocess` and `afplay` as above. 

It should behave like this:

```python
>>> import subprocess
>>> player = MusicPlayer(subprocess) 
    #                    ^^^^^^^^^^
    # We'll need to pass in (inject) `subprocess`
    # in order to isolate our tests.
>>> player.play("/Users/kay/Code/player/data/tunes/myfav.wav")
    # A pause while it plays the file.
>>>
```

Once you've done this, you can run the UI:

```shell
; python -m ui
Welcome to your music library!
Enter:
  a: to add a track
  p: to play a track
  d: to delete a track
  l: to list your tracks
  q: to quit
What do you pick? a
What's the title? Fav
What's the artist? Artist
What's the file? data/tunes/myfav.wav
Added successfully.
Enter:
  a: to add a track
  p: to play a track
  d: to delete a track
  l: to list your tracks
  q: to quit
What do you pick? p
1. Fav by Artist @ data/tunes/myfav.wav
Which do you want to play? 1
Playing Fav by Artist...
Done.
```

And the UI tests to verify everything is working:

```shell
; python -m unittest discover ui
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

And if your tests yodel, you'll know you've not isolated them properly.

## Done?

[Go to the next challenge](./step_05.md)


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_04.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_04.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_04.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_04.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_04.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
