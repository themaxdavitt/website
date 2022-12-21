+++
title = "Brain cookies #1"
date = "2022-12-20"
tags = [
  "braincookies"
]
+++

At any given point in time I'll have lots of _stuff_ running through my brain and sometimes I want to write the interesting bits down somewhere. Usually I just throw them in my [to-do app](https://todoist.com) or in a new [VS Code](https://code.visualstudio.com) tab, but I'm always reluctant to delete them later since it feels like they'll be lost forever. This series aims to solve that problem by broadcasting those ideas into the ether, in a way giving me permission to delete and forget about them. "Brain cookies" was just the first phrase to pop into my head to describe them and they _sorta_ get the concept across so I'm sticking with it.

<!--more-->

These are in no particular order and they're definitely not fully thought through; all I did was clean them up, add some context, and do a few minutes of research. They are a bit rambly too. If you're looking for more lists like this, check out [Samuel Squire's "ideas" repos](https://github.com/samsquire/ideas) and a ["Software I want" list](https://github.com/themaxdavitt/software-i-want) I made a while ago. Enjoy, and if you have any thoughts about these, [share them on the fediverse](https://fosstodon.org/@themaxdavitt/109549047400049154)!

## Using Datasette for habit tracking

[Datasette](https://datasette.io) is pretty cool. I've been interested in open data portals and data exploration in general for a long time, and while I've known about Datasette for a little while too, I hadn't figured out exactly what I want to use it for yet.

Over the last few months I've been practicing [plain text accounting](https://plaintextaccounting.org) using [hledger](https://hledger.org). It's really nice and has completely changed my relationship with money for the better. Because I store my "journal" files in a private GitHub repo I've been able to use the contribution graph on [my profile](https://github.com/themaxdavitt) as a habit tracker. Tracking it like that wasn't intentional and it has the potential to be inaccurate, but currently I'm not doing open-source until I figure the legal stuff out with my employer, so it basically only tracks accounting activity for now anyways. 

I would also like to start tracking my physical activity in the same way though. I made a [database schema](https://gist.github.com/themaxdavitt/563e349613cc41a0456d38a1215e5ec0) outlining everything I'd want to collect[^1] and eventually I would like some way to compare my stats to the table produced by the [NIDDK's Body Weight Planner tool](https://www.niddk.nih.gov/bwp). I'd like to figure out if/how I can solve this and improve my hledger habit tracking situation with Datasette so I don't have to develop my own solution (I can already see where I'm heading in the [Max Project Pipeline](https://max.davitt.me/blog/good-enough/#fn:4)).

[^1]: Yes, [my last TIL](https://max.davitt.me/blog/turn-bash-array-into-cmd-args/) was related to this, but don't worry, I haven't really worked on it much since then.

## Industry-specific marketing can be outsourced

I got my wisdom teeth removed recently and leading up to that I got pretty familiar with my oral surgeon's website. When I mentioned how detailed it was to him he told me that he was paying some [some company](https://www.pbhs.com) to manage the content on it for him.

I was vaguely aware of "digital presence" offerings but I hadn't realized how prevalent they were until now. They're used by [CPAs](https://www.cpasitesolutions.com), [townships](https://www.townweb.com), [staffing agencies](https://www.haleymarketing.com/services/websites/), [assisted living facilities](https://www.ltcwebsitesolutions.com), [car dealerships](https://www.sincrodigital.com), and probably every other type of business. A little bit of [WordPress](https://wordpress.org) goes a long way I guess.[^2]

[^2]: Also, it's not just website hosting: I found [a compliance/cybersecurity firm](https://complyauto.com) targeted towards dealerships...

## Corporate redesign guarantors

<!-- todo: link Syd's website when it's back up -->

A friend of mine was doing brand redesigns for a class she's taking and had to mock up things like letterheads, envelopes, and business cards. In theory there's a lot that can be customized about those, but in reality I'm not sure how many companies feel comfortable with large customizations. Like, if you suggest that they use envelopes folded a certain way or business cards with a certain material, how are they supposed to feel confident they can reliably get those for years to come?

So here's the pitch: stationary companies should work with design studios to let them contractually guarantee to their clients that they will have a supplier for their fun little designs for a minimum quantity or length of time. This guarantees to clients that their redesign is achievable (at least the stationary part) and helps design studios feel confident that their clients will actually follow their redesign long-term.

Full disclosure: I have no experience with or real knowledge about that industry, so I'm probably either misunderstanding the relationship between designers and clients and/or reinventing a process that already exists. I just like fun branding. :)

## Accidental bookmarking tools

I was in the process of going through the list of accounts I'm following on Twitter for an eventual move to Mastodon when I realized that I was kinda using it as a really bad bookmarking tool. All the quirky little startups I'd followed as I discovered them rarely ever ended up on my timeline because they were competing with like 400 other accounts, and so I had forgotten about many of them. Same with a lot of cool concepts I'd favorited from artists and designers I followed.

I'm not sure what to do about that. I have a [Pinboard](https://pinboard.in) account but [the site seems to be unmaintained](https://news.ycombinator.com/item?id=34062802). I should probably migrate stuff over to my [are.na](https://are.na) account but I'm not quite sure how to categorize things yet. Anything is better than the unsorted mess I have across Twitter, TikTok, and my Safari reading list though.

Speaking of bookmarks, I've noticed that a handful of the TikToks I bookmarked have been deleted. While it's nice that it shows me that they were deleted, it concerns me that the deletions even happened, because I bookmarked them so I could refer back to them. Maybe I need to set up something like [ArchiveBox](https://archivebox.io), and then refer to those archives on are.na? Hmm...

## Taking advantage of movie theater schedules

Movie theaters typically show a lot of movies at a lot of different times throughout the day, and all the movie theaters I've gone to check your ticket at the front of the building and expect you to find your way to where they're showing whatever movie your ticket was for.

So... I wonder if there's a website that lets you visualize how showtimes are staggered at your local theater to plan out what movies you can see right after your first one ends (without having to buy an additional ticket). I don't go to the movies very often, and I don't think I'd ever do this for moral reasons anyways, but I'd be surprised if this didn't exist. It could help people with less money make sure they were getting the most out of their visit.

I know employees can be diligent and try to remember faces but I'm curious what movie theaters do to combat this at the scheduling level. I'm sure people have been doing this manually for decades so I'm doubtful that they haven't at least attempted to address it. 
