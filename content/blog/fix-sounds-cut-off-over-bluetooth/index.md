+++
layout = "blog"
title = "TIL: fix cut off sounds on Bluetooth headphones using FFmpeg"
date = "2025-01-21"
tags = [
  "til",
]
description = "Very brief \"today I learned\" sharing how to fix sounds being cut off on Bluetooth headphones using FFmpeg."
+++

This is a "today I learned" that I _actually_ learned back in October/November and forgot to write up. :) Anyways...

From what I can tell, many Bluetooth audio devices quickly disconnect from their audio source after playing and automatically reconnect when needed. This probably works well for most pieces of media, but it can be extremely annoying when what you're playing has a really short duration, e.g. word pronunciations in Anki, _because the beginning and end[^1] of the clip can be cut off_. Imagine the word "ba-na-na" sounding like "a-na-n"!

[^1]: Yes, the end too. I understand how the beginning could be cut off (maybe the O.S. starts "playing" the audio before the Bluetooth device is ready?), but why the end can also get cut off has me very confused.

I don't really understand how this is still a problem in `$CURRENT_YEAR`, but it is. There are so many Reddit threads about it with hacky solutions like "play quiet white noise" or "open up a YouTube video in the background"... Here's how I solved it with a "simple" [FFmpeg](https://www.ffmpeg.org/) command:

```bash
ffplay -nodisp -f lavfi -i anullsrc=r=44100:cl=stereo
```

I'll be honest, ChatGPT helped me out with this. My initial solution was to use [`afplay`](https://ss64.com/mac/afplay.html) on macOS but I couldn't come up with a good one-liner I liked. Its explanation is that this plays an endless silent audio stream ([`anullsrc`](https://ffmpeg.org/ffmpeg-filters.html#anullsrc) via [`lavfi`](https://ffmpeg.org/ffmpeg-devices.html#lavfi)) with no display output ([`-nodisp`](https://ffmpeg.org/ffplay.html#Main-options)) to prevent the disconnects from happening, and it's been working for me for months.

Hope this helps!
