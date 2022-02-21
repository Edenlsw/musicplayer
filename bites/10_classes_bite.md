# Classes

_**This is a Makers Bite.** Bites are designed to train specific skills or
tools. They contain an intro, a demonstration video, some exercises with an
example solution video, and a challenge without a solution video for you to test
your learning. [Read more about how to use Makers
Bites.](https://github.com/makersacademy/course/blob/main/labels/bites.md)_

Learn to use classes in Python

## Introduction

Classes are blueprints for objects (sometimes called instances). Objects are
entities in a program that have both state (data) and behaviour (functions that
operate on that data, sometimes called methods).

<details>
  <summary>I still don't really understand objects...</summary>

  Explaining OOP is beyond the scope of this material, but please do contact
  your coach for help with this.

</details>

In Python, they work like this:

```python
class Greeter:
  def __init__(self, name):
    self.name = name
  
  def greet(self):
    return f'Hello, {self.name}!'


greeter = Greeter("Kay")
print(greeter.greet())
# Prints: "Hello, Kay!"
```

## What is `self`? Why do I need it?

`self` refers to the instance of the class being called. Imagine if you had
fifty instances of `Greeter` all with different names — when you called
`greeter_32.greet()`, how would it know which name to look at?

`self` fixes this problem. It is a reference to the current instance being
called so that instance variables can be set and retrieved. In other languages
this is magically available to you, but in Python you have to specify it
explicitly as the first argument of every instance method.

<details>
  <summary>I still don't understand...</summary>

  Keep going through the demonstration materials and exercise. If you still
  don't understand, do bring this up with your coach.

</details>

## Demonstration

Stop this video before the exercise starts so you have the chance to try it
yourself first.

[Demonstration Video](https://www.youtube.com/watch?v=sxkGQeNvqTM&t=3823s)

## Exercise

Create an `Introducer` class that has two methods, `announce` and `introduce`.

It should work like this:

```python
introducer = Introducer("Kay")

print(introducer.announce())
# Should print: "I am Kay!"

print(introducer.introduce("Fred"))
# Should print: "Hello Fred, I am Kay!"
```

[Example Solution](https://www.youtube.com/watch?v=sxkGQeNvqTM&t=4209s)

## Challenge

Create a class called `Reminder`. It should work like this:

```python
reminder = Reminder("Kay")

reminder.remind_me_to("Walk the dog")

print(reminder.remind())
# Should print: "Kay! Walk the dog!"
```


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/10_classes_bite.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/10_classes_bite.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/10_classes_bite.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/10_classes_bite.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=bites/10_classes_bite.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
