# Step 3: Add a Track Class

Back-end complete! But adding simple strings isn't going to cut it. We want to
link these tracks to music files. Let's use another class to implement this.

## Objectives

Learn to:
* Test-drive classes

## Exercise

Kez has implemented a new interface to account for adding the filenames. Copy it
into your project from [interfaces/step_03](./interfaces/step_03).

To support it, implement a new class called `Track`. It should take three
arguments: the track's title, artist, and file. It should assign them to public
fields, so that you can do this:

```python
>>> track = Track("The Boys of Summer", "DJ Sammy", "summer.mp3")
>>> track.title
"The Boys of Summer"
>>> track.artist
"DJ Sammy"
>>> track.file
"summer.mp3"
```

You can do this with a normal class. _Or_ you can be super fancy and use Python
Data Classes. It's merely a web search away.

### Organising your classes

We spoke about Python files being modules before. Unlike other languages, it is
very common in Python to have more than one class per file. Python tends to
prefer flat directory structures without lots of folders in folders. 

Let's keep to that here and implement the `Track` class within 
`player/music_library.py`.

### What about `MusicPlayer`? Do I need to change it to use `Track`?

No! Take a look at `ui/interface.py` if you want to know why.

It's a great feature of software design if you can add functionality without
changing current classes, merely adding new ones. This is called the Open/Closed
principle and it contributes the 'O' to the SOLID principles.

### What about the tests for `MusicPlayer`?

Yes, that's a good idea — update those to add instances of `Track` rather than
strings.

## Done?

[Go to the next challenge](./step_04.md)


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_03.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_03.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_03.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_03.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/python-music-player-challenges&prefill_File=step_03.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
