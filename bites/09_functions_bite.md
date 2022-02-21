# Functions

_**This is a Makers Bite.** Bites are designed to train specific skills or
tools. They contain an intro, a demonstration video, some exercises with an
example solution video, and a challenge without a solution video for you to test
your learning. [Read more about how to use Makers
Bites.](https://github.com/makersacademy/course/blob/main/labels/bites.md)_

Learn to use functions in Python.

## Introduction

Functions are units of code that you can call on demand. They are similar to
methods. In Python they work like this:

```python
def greet(name):
  return f'Hello, {name}!'

print(greet("Kay"))
# Prints: "Hello, Kay!"

print(greet("Eric Cantona"))
# Prints: "Hello, Eric Cantona!"
```

## Demonstration

Stop this video before the exercise starts so you have the chance to try it
yourself first.

[Demonstration Video](https://www.youtube.com/watch?v=sxkGQeNvqTM&t=3191s)

## Exercise

Complete these programs:

```python
# Your code goes here.

print(add_five(4))
# Should print: "9"

print(add_five(2132))
# Should print: "2137"
```

```python
# Your code goes here.

print(subtract_low_from_high(2, 3))
# Should print "1"

print(subtract_low_from_high(3, 2))
# Should print "1"

print(add_five(subtract_low_from_high(1463, 16475)))
# Should print "15017"
```

[Example Solution](https://www.youtube.com/watch?v=sxkGQeNvqTM&t=3349s)

## Challenge

Write a method called `superify` which takes a string and adds the word
"super" to the start. So given 'woman' it returns 'superwoman', given 'dog' it
returns 'superdog'.

Then use it to create the ultimate feline superhero, like this:

```python
print(superify(superify(superify(superify("cat")))))
# Should print:
"supersupersupersupercat"
```


[Next Challenge](10_classes_bite.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/09_functions_bite.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/09_functions_bite.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/09_functions_bite.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/09_functions_bite.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/09_functions_bite.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
