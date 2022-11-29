+++
title = "How I port forward through WireGuard on AWS Lightsail"
date = "2022-12-04"
tags = [
  "homelab",
  "networking"
]
description = "Here's how I port forward through WireGuard on AWS Lightsail."
draft = true
+++

**todo: rewrite description, first paragraph too maybe, and do something with the "more" comment**

A while ago I told a friend I would write up a tutorial on how I set up WireGuard and port forwarding through it. [Now that I have a personal website]({{< ref "/blog/good-enough" >}}) I actually have the motivation to do it! I also realized I accidentally picked the wrong region to put my AWS Lightsail instance in when I initially did it so I might as well fix that also. :)

<!--more-->

I'm going to assume you already know what [port forwarding](https://en.wikipedia.org/wiki/Port_forwarding) (passing along network traffic), [WireGuard](https://www.wireguard.com) (good <abbr title="virtual private network">VPN</abbr> software), and [AWS Lightsail](https://aws.amazon.com/lightsail/) (easy <abbr title="virtual machines">VMs</abbr> on <abbr title="Amazon Web Services">AWS</abbr>) are. Fair warning, I am _not_ a networking expert, I just managed to figure enough stuff out to do what I wanted to. My contact info is at the bottom of the home page if you want to give feedback; I'll make sure it ends up here! **todo: clarify that AWS Lightsail, Amazon Linux 2, etc. are just what I'm using here and not required, update footnotes #1 and #2 if necessary**

---

Assuming you already have an AWS account, start by going to the [AWS Lightsail home page](https://lightsail.aws.amazon.com) and clicking "Create instance". Pick an instance location that you think will have the lowest latency for clients connecting to it,[^1] in my case Ohio ({{% dont-break %}}us-east-2{{% /dont-break %}}). Don't worry about setting an availability zone. For your instance image, pick the "Linux/Unix" platform, click the "OS Only" tab, and then select the "Amazon Linux 2" blueprint.[^2] Skip setting a launch script. Under the "Change SSH key pair" section, create a new key pair,[^3] download the private key, and make sure that key pair is selected on the page. **todo: figure out how to best explain which instance size to pick or how to decide to go elsewhere**

**todo: finish everything else lol**

<!-- Personally, I don't put that much traffic through my VPN, so I chose the cheapest instance option, but you should pick what makes the most _economic_ sense. Just because I'm using AWS doesn't mean you should, you can still change your mind at this point without having spent any money and you can still follow most of the rest of the instructions in this guide. -->

[^1]: The site I was going to recommend to help with this seems to no longer exist so in an effort to avoid future [link rot](https://en.wikipedia.org/wiki/Link_rot) just use your favorite search engine to look for "aws latency test", "aws ping test", etc. I highly recommend testing the latency of regions from other cloud providers too.

[^2]: This is likely doable on any of the platforms listed there, but it's easier to write out instructions for just one operating system.

[^3]: As far as I'm aware, it's better to create new key pairs for each system, and [OpenSSH can make managing them all pretty easy](https://try.popho.be/ssh-keys.html).
