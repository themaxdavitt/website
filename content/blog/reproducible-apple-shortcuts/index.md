+++
layout = "blog"
title = "TIL: how to make reproducible Apple Shortcuts"
date = "2025-02-09"
tags = [
  "til",
]
description = "Rambling \"today I learned\" sharing how to make reproducible Apple Shortcuts using .plist files and the `shortcuts` CLI tool."
+++

I, like many other people, want to limit my exposure to blue light in the evening so I can fall asleep easier. My iPhone and MacBook have [a feature](https://support.apple.com/en-us/118583) for this, but even at the warmest color temperature I don't think it's effective enough. My workaround has been to use [their "Color Filters" feature](https://support.apple.com/en-us/111773) in the accessibility settings to set a really intense red tint and, on my iPhone, toggle it using [their "Accessibility Shortcut" feature](https://support.apple.com/en-us/111771) manually.

I wondered how I could easily toggle this on my MacBook though. Sure, I could manually navigate from Settings, to Accessibility, to Display, scroll down to the Color Filters section, and toggle the relevant checkbox, but I wanted something a little more convenient. I had heard about [Apple's Shortcuts app](https://support.apple.com/guide/shortcuts-mac/welcome/mac) in the past; why not try using that?

So I created a shortcut to toggle the color filter. It was easy enough, there was a built-in action to do exactly that, so my shortcut just contained that single action:

{{< figure src="set-color-filters.png" alt="Cropped screenshot of a shortcut containing the following action: toggle color filters" caption="Click the image to download the shortcut." link="Set Color Filters.shortcut" >}}

At first I would manually open the Shortcuts app and click the relevant button to run it, but I later realized I could use [the `shortcuts` command](https://support.apple.com/guide/shortcuts-mac/run-shortcuts-from-the-command-line-apd455c82f02/mac) to do that:

```bash
shortcuts run "Set Color Filters"
```

This is when things got complicated. I like the idea of having all of my little helper utilities version controlled in ["dotfiles"](https://wiki.archlinux.org/title/Dotfiles). I remembered that [AppleScript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html) existed and wondered if I could use that to toggle the color filter instead. I read through a dozen StackOverflow posts, tried a few things, ran into errors I didn't know how to work around, and gave up.[^1] Everything relied on how the Settings app's UI is organized to work, which inevitably breaks because Apple is apparently indecisive about how they want the app to work.

[^1]: [This](https://apple.stackexchange.com/a/413540) didn't work:

      ```
      46:116: execution error: System Settings got an error: Can’t set pane id "com.apple.preference.universalaccess" to pane id "com.apple.preference.universalaccess". (-10006)
      ```

      [This](https://tinyapps.org/blog/202102070700_macos_eink_applescript.html) didn't work:

      ```
      38:106: execution error: System Settings got an error: Can’t get anchor "Seeing_ColorFilters" of pane "Accessibility". (-1728)
      ```

      [These got close](https://discussions.apple.com/thread/254887700) (this is where someone pointed out that UI instability issue):

      ```
      408:417: execution error: System Events got an error: Can’t set application process "System Preferences" to true. (-10006)
      ```
      ```
      432:455: execution error: System Events got an error: osascript is not allowed assistive access. (-25211)
      ```

      Etc. For reference I'm on macOS Sequoia (version 15). Could I have somehow used [Script Editor](https://support.apple.com/guide/script-editor/welcome/mac) to figure out how to fix these things? Sure, but it just didn't seem worth it.
      
      Also, you're welcome for including the error messages here so this page came up in your searching.

So I went back to using Shortcuts and tried to learn a little bit more about how other people use them. You can apparently share them with other people using iCloud or as plain old files. AFAICT they use a binary-encoded [plist](https://en.wikipedia.org/wiki/Property_list) format with a cryptographic signature from Apple. You can't do it in the GUI, but based on [this](https://routinehub.co/shortcut/10060/) I was able to create a simple little helper shortcut to export any shortcut as a text-encoded plist:

{{< figure src="get-shortcut-plist.png" alt="Cropped screenshot of a shortcut containing the following actions: receive text from quick actions stopping if there's no input, get shortcuts from all shortcuts, filter my shortcuts where name is shortcut input limit 1, get file of type com.apple.property-list from files, stop and output file of type doing nothing if there's nowhere to output" caption="Short and sweet, though this took a lot more trial and error than you'd imagine. Making shortcuts kinda sucks, it's very hard to figure out where you made a mistake. You can click the image to download it and save yourself the trouble." link="Get Shortcut plist.shortcut" >}}

Using that `shortcuts` program, you can run it like this:

```bash
shortcuts run "Get Shortcut plist" --input-path "Set Color Filters" | tee
# Alternatively:
shortcuts run "Get Shortcut plist" --input-path "Set Color Filters" --output-path set-color-filters.plist
```

{{< details summary="Here's what the output looks like if you're curious." >}}
{{< embed source="set-color-filters.plist" >}}
{{< /details >}}

I don't know its full usage but the `--input-path` argument doesn't actually read input from a path you specify for it (at least when the shortcut input is text, maybe it does for files?). Also, it doesn't default to printing to stdout (probably because some shortcuts can output binary files), so if you want that you need to pipe it out, which is why I used `tee` above. 

Anyways, great, now I have these text files I can do whatever with. Apparently some people have written [nicer](https://www.jellycuts.com/) [editing](https://routinehub.co/shortcut/5217/) [tools](https://github.com/electrikmilk/cherri) that work with them! Probably never going to use them, but still, that's pretty cool. Now my only problem is to figure out how to take these `.plist` files and turn them back into shortcuts.

This is _supposed_ to be pretty easy. You can't import `.plist` files in the GUI, but you're _supposed_ to be able to pass one of these files to a `shortcuts` subcommand and it will do the same signature magic that the GUI does and spit back out a `.shortcut` file you can use.

{{< highlight plaintext "hl_Lines=1" >}}
$ shortcuts sign --help
OVERVIEW: Sign a shortcut file.

You can use this command to sign a shortcut file. It also supports signing a
shortcut in the old format.

USAGE: shortcuts sign [--mode <mode>] --input <input> --output <output>

OPTIONS:
  -m, --mode <mode>       The signing mode (anyone, people-who-know-me).
                          (default: people-who-know-me)
  -i, --input <input>     The shortcut file to sign.
  -o, --output <output>   Output path for the signed shortcut file.
  -h, --help              Show help information.

{{< /highlight >}}

But apparently [it's been broken for a while](https://github.com/electrikmilk/cherri/issues/49), so people are instead using a third-party server running a version of macOS which it isn't broken on to get shortcuts signed:

```bash
curl --request POST "https://hubsign.routinehub.services/sign" \
  --header "Content-Type: application/x-plist" \
  --data-binary "@set-color-filters.plist" \
  > set-color-filters.shortcut
```

Kinda weird, but whatever. The last thing I wanted to do was automatically install my shortcut. There's [a URL scheme for this](https://github.com/sebj/iOS-Shortcuts-Reference/blob/5fa176ed9af217c32edb5c98690016d323d07daf/README.md#key-url-schemes):

```
shortcuts://import-shortcut/?name=My%20Shortcut&url=https%3A%2F%2Fexample.com
```

But I tried a bunch of the strategies used in [GitHub code search results](https://github.com/search?q=%22shortcuts%3A%2F%2Fimport-shortcut%22&type=code) and nothing was working. In hindsight, maybe this is a good thing; that document I linked mentioned that there's apparently a `silent` argument that will import the shortcut without any user interaction??

Anyways... this is how I spent yesterday afternoon. Not worth it, though hopefully it saves someone out there some grief.
