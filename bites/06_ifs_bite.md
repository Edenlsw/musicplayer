# Ifs

_**This is a Makers Bite.** Bites are designed to train specific skills or
tools. They contain an intro, a demonstration video, some exercises with an
example solution video, and a challenge without a solution video for you to test
your learning. [Read more about how to use Makers
Bites.](https://github.com/makersacademy/course/blob/main/labels/bites.md)_

Learn to use if to compare values in Python.

## `if` and `else`

Python has an `if` statement like this:

```python
switch = True

if switch:
  print("Switch is true")
else:
  print("Switch is false")

```

Python doesn't use `end` keywords or close brackets for `if` statements.
Instead, it uses indentation. Consider:

```python
switch = True

if switch:
  print("Switch is true")
else:
  print("Switch is false")

print("This always runs")
```

So it is critical to ensure your indentation is correct.

## Comparison

Python has all the normal operators and data types to assist with comparing
values.

```python
>>> 2 > 1 # Greater than
True
>>> 2 < 1 # Less than
False
>>> 2 >= 2 # Greater than or equal to
True
>>> 2 <= 2 # Less than or equal to
True

>>> 2 == 2 # Equal to
True
>>> 2 != 2 # Not equal to
False
>>> "Hello" == "Hello" # == and != work on strings too
True
>>> "Hello" != "Hello"
False
>>> 2 == "2" # Values of different types aren't equal
False

>>> not True # Negation (note that True must be capitalised)
False
>>> not False # Likewise False
True

>>> [1, 2, 3] == [1, 2, 3] # `==` compares equality even on data structures
True
>>> my_list = [1, 2, 3]
>>> my_list is my_list # `is` means strictly the same object, not just the same contents
True
>>> [1, 2, 3] is [1, 2, 3] # Same contents but not same object
False

>>> False is None # We also have `None` which is like null or undefined, neither True nor False
False
```

## Demonstration

Stop this video before the exercise starts so you have the chance to try it
yourself first.

[Demonstration Video](https://www.youtube.com/watch?v=sxkGQeNvqTM&t=1092s)

## Exercise

Complete this program:

```python
import random

random_number = random.randint(1, 5)

# Print "One" if `random_number` is 1
# Print "Two" if `random_number` is 2
# Print "More" if `random_number is above 2
```

[Example Solution](https://www.youtube.com/watch?v=sxkGQeNvqTM&t=1607s)

## Challenge

Complete this program:

```python
import time

seconds = int(time.time())

# Print "Fizz" if `seconds` is divisible by 3
# Print "Buzz" if `seconds` is divisible by 5
# Print "FizzBuzz" if `seconds` is divisible by 3 and 5
# Otherwise, print `seconds`
```


[Next Challenge](07_loops_bite.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/06_ifs_bite.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/06_ifs_bite.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/06_ifs_bite.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/06_ifs_bite.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/06_ifs_bite.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
