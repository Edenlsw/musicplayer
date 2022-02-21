# Strings

_**This is a Makers Bite.** Bites are designed to train specific skills or
tools. They contain an intro, a demonstration video, some exercises with an
example solution video, and a challenge without a solution video for you to test
your learning. [Read more about how to use Makers
Bites.](https://github.com/makersacademy/course/blob/main/labels/bites.md)_

Learn to use manipulate strings using Python.

## Introduction

Strings in Python are surrounded by single or double quotes.

```python
>>> "Hello"
'Hello'
>>> 'world'
'world'
```

You can also create multiline strings using `"""`.

```python
>>> "Hello
... world"""
'Hello\nworld'
```

There are a number of ways to do string interpolation in Python (putting
variables into strings). 

The most popular is called f-strings.

```python
# f-strings
>>> name = "Kay"
>>> f"Hello, {name}!"
'Hello, Kay'
```

<details>
  <summary>I get an error here...</summary>

  Make sure you are running `python3`, not `python`. Look back at the [Running
  Python](./running_python_bite.md) to find out why.

</details>

F-strings are now considered best practice for Python 3. However you may see
some other methods in your travels. Here they are so that you can recognise
them:

```python
# %-formatting
>>> name = "Kay"
>>> "Hello, %s!" % name
'Hello, Kay!'
```

```python
# str.format()
>>> name = "Kay"
>>> "Hello, {}!".format(name)
'Hello, Kay!'
```

```python
# String Concatenation
>>> name = "Kay"
>>> "Hello, " + name + "!"
'Hello, Kay!'
```

## Demonstration

Stop this video before the exercise starts so you have the chance to try it
yourself first.

[Demonstration Video](https://www.youtube.com/watch?v=sxkGQeNvqTM&t=734s)

## Exercise

Complete the following programs:

```python
# Make this program print "Hello to the Frog!"

animal = "Frog"
# ...
```

```python
# Make this program print "There are 5 directories."

count = 5
thing = "directories"
# ...
```

[Example Solution](https://www.youtube.com/watch?v=sxkGQeNvqTM&t=909s)

## Challenge

Complete this program:

```python
# Make this program print:
# One Sunday morning the warm sun came up and - pop!

day = "Sunday"
time_of_day = "morning"
star_quality = "warm"
star_name = "sun"
star_direction = "up"
mysterious_sound = "pop"
```



[Next Challenge](06_ifs_bite.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/05_strings_bite.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/05_strings_bite.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/05_strings_bite.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/05_strings_bite.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/05_strings_bite.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
