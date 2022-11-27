+++
title = "Good enough!"
date = "2022-11-27"
tags = [
  "personal",
  "meta",
  "webdev"
]
+++

I finally have a personal website!

<!--more-->

I've always been a little scared to have a public-facing web presence, mainly out of a fear of embarrassment, but I've also always wanted my own place where I can just share _stuff_ (hence the name "Max's Stuff")[^0]. These are kinda conflicting, but I know that. I often struggle with worrying too much about things relative to how much they actually matter and over-planning to the point where I end up accomplishing nothing[^1]. Those plus perfectionism is why this site has taken forever to set up.

[^0]: I also have a large personal goal that, among _many_ other things, involves being pretty active online. If all goes right you'll definitely hear about it someday!

[^1]: To be completely honest, I think I struggle with anxiety in general (with those being symptoms of it), but it's kind of a cliché for people to just say they have whatever condition pretending that their temporary experience is comparable to the actual thing and I don't want to unintentionally promote that.

_(Tech terminology soup begins.)_

It all started sometime around early 2021. I initially wanted to implement a [digital garden](https://maggieappleton.com/garden-history) using a tool called [Foam](https://foambubble.github.io/foam/). It seemed pretty cool and I used it for a few weeks, but I recall disliking [that wikilinks had to be made compatible with other tools](https://foambubble.github.io/foam/user/features/wikilinks#markdown-compatibility), that it was [unclear how to control page visibility](https://github.com/foambubble/foam/issues/149), and that I couldn't create or use components (using something like [MDX](https://mdxjs.com)) to deduplicate patterns within pages (in that case, to encapsulate content to show/hide based on environment variables when building), so I didn't want to use it for my website. I'm now seeing that I could've just used a third-party template to support MDX and configurable page visibility; I don't remember why I didn't do that at the time, I was probably just unaware of the project's ecosystem. I'll try it out again someday since in hindsight I don't think I gave it a fair shot. I recall also playing with [Eleventy](https://www.11ty.dev) around then though I don't remember much about why I didn't use it.

I had a pretty extensive mental requirement list for the solutions I was evaluating at the time. Being born and raised on the [orange site](https://news.ycombinator.com), I wanted to be able to [own my data](https://indieweb.org/own_your_data), store everything in plaintext (or [close enough](https://en.wikipedia.org/wiki/Markdown)), use [Git](https://git-scm.com) for tracking changes, restrict usage of JavaScript to [progressive enhancement](https://en.wikipedia.org/wiki/Progressive_enhancement), be compatible with the [IndieWeb](https://indieweb.org/Category:building-blocks), [archive](https://www.gwern.net/Archiving-URLs) references, etc. I eventually decided to try [creating my own <abbr title="content management system">CMS</abbr> for accomplishing all this](https://github.com/themaxdavitt/hast-stuff) and wrote custom [Node.js module loaders](https://nodejs.org/docs/latest-v18.x/api/esm.html#loaders) allowing me to import and process `.html`, `.js` / `.jsx`, and `.mdx` files inside <abbr title="EcmaScript module">ESM</abbr>-based Node.js scripts using the [`unified`](https://unifiedjs.com) ecosystem and [`acorn`](https://github.com/acornjs/acorn). Based on the state of the source code and when I last modified many of the files, I think I was planning on adding support for processing CSS (using [PostCSS](https://postcss.org) if I recall correctly) and sorta had saving [SingleFile](https://github.com/gildas-lormeau/SingleFile) archives of referenced webpages finished before picking my internship back up that summer. Sure, it'd be satisfying to have a consistent asset pipeline and convenient little helper components and all that someday when I'd finish, but _why the fuck_ would I (and did I) spend so much time trying to do all that? _Did I really need all of that?_ 

No, I didn't.

_(Tech terminology soup ends (for the most part).)_

I can't quite pinpoint when I became bothered enough about my behavior to start actively trying to be more pragmatic in how I approach problem solving, but it was probably around spring of this year. Things in my personal life and at work made me reflect on how I treat conflict avoidance and risk (and their downstream effects on how I act). I do still struggle with this today, but from a technology standpoint I am at least actually trying to improve. Around that time I started to use [Notion](https://www.notion.so), and while I did eventually move off of it to "own my data" (and also because I'm not sure I actually want to maintain a digital garden), it felt nice to not have to worry about the tech stack involved in what I'm working on top of. I appreciated the decrease in "cognitive overhead"[^2].

[^2]: David Demaree describes "cognitive overhead" in [a blog post](https://web.archive.org/web/20210327093208/https://log.demaree.me/notes/2011/google-and-cognitive-overhead/) as "how many logical connections or jumps your brain has to make in order to understand or contextualize the thing you’re looking at."

This site is built using a tool called [Hugo](https://gohugo.io). It's a flat-file static site generator that provides templating and "shortcodes" and [enough other things](https://gohugo.io/about/features/) that I think I can say it's good enough for me. Actually, I'm barely even using it to it's full potential, and I think that's for the better! I started to get carried away building a theme but I caught myself before I was stuck in the "sunk cost fallacy stage"[^3] and went with [this](https://themes.gohugo.io/themes/hugo-bearblog/), which is nice and simple. I also really like how [this site](https://seirdy.one) works (the author's posts are also pretty interesting) and almost adapted it into a theme, but I decided against it because I felt like I'd be stealing their hard work and it seemed kinda laborious anyways (maybe I'll try commissioning them to do it in the future if they're interested?).

[^3]: The Max Project Pipeline seems to be:

      1. Get interested in a thing and learn a lot about it
      2. Daydream about how you can use it in some cool way without estimating how much work it'd take
      3. Start doing the work but only slowly build a mental estimate of how much work is left
      4. You feel like you'd have wasted your time to not see it to completion now so you want to keep working but it's demotivating since you now have a much clearer idea of the complexity of the problem
      5. Finish all the work and be proud of yourself (rarely gets reached)

      I've never actually wrote it out like this before but I'm glad I just did. To say I've spent a lot of time in steps #2 and #4 would be an understatement (easily thousands of hours). In this case thankfully I actually realized I was wasting my time in step #3 so I avoided being stuck in #4.

Anyways... it's nice to have a place to call home, even if it's not perfect! Expect to see life updates (hopefully they won't be too boring), tutorials (I owe people quite a few), "Today I Learned"s (inspired by [Simon Willison's site dedicated to them](https://til.simonwillison.net)), and whatever else. Feedback is more than welcome and my contact info is at the bottom of the home page. Thanks for reading!
