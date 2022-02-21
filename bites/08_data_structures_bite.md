# Data Structures

_**This is a Makers Bite.** Bites are designed to train specific skills or
tools. They contain an intro, a demonstration video, some exercises with an
example solution video, and a challenge without a solution video for you to test
your learning. [Read more about how to use Makers
Bites.](https://github.com/makersacademy/course/blob/main/labels/bites.md)_

Learn how to use simple data structures in Python

## Introduction

Python has the usual everyday data structures:

* Lists
* Dictionaries (key-value stores)

As well as a number of others, including Tuples.

### Lists

Lists work like this:

```python
my_list = ["Apples", "Oranges", "Pears"]

my_list[0] # => "Apples"
my_list[1] # => "Oranges"
my_list[2] # => "Pears"
my_list[3] # IndexError: list index out of range
len(my_list) # => 3

if "Apples" in my_list:
  print("We got apples!")
```

### Tuples

Tuples are like lists but you can't change them, and overall they're a bit
more simple.

```python
my_tuple = ('I', 'Like', 'Python')

my_tuple[1] # => 'Like'
len(my_tuple) # => 3
```

You might see them used without the parentheses for conveniently assigning
multiple variables. Example:

```python

a, b, c = 1, 2, 3

a # => 1
b # => 2
c # => 3
```

### Dictionaries

Dictionaries (known as hashes in Ruby, and objects in Javascript) work like this:

```python
my_dict = { 'apples': 23, 'oranges': 32, 'pears': 21 }

my_dict['apples'] # => 23
my_dict['kiwi'] # KeyError: 'kiwi'

if "apples" in my_dict:
  print("We got apples!")
```

## Demonstration

Stop this video before the exercise starts so you have the chance to try it
yourself first.

[Demonstration Video](https://www.youtube.com/watch?v=sxkGQeNvqTM&t=2196s)

## Exercise

Complete these programs:

```python
my_list = ["Cat", "Mouse", "Frog"]

# Write some code to amend the list here.

print(my_list)
# Should print:
# ['Mouse', 'Lynx', 'Cat', 'Frog']
```

```python
my_list = ["Cat", "cat", "frog", "cat", "dog", "Dog"]
counters = {}

# Write some code to count the items in the list here

print(counters)
# Should print (in any order)
# { 'cat': 3, 'dog': 2, 'frog': 1 }
```

[Example Solution](https://www.youtube.com/watch?v=sxkGQeNvqTM&t=2544s)

## Challenge

Complete this program:

```python
my_cohort = [ ] # Put the names of the people in your cohort here

# Program should print a dictionary with each of the letters of the alphabet
# and the number of people whose first name begins with that letter.
# E.g. { 'a': 2, 'b': 0, ... }
```


[Next Challenge](09_functions_bite.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/08_data_structures_bite.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/08_data_structures_bite.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/08_data_structures_bite.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/08_data_structures_bite.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/08_data_structures_bite.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
