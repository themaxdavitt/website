+++
layout = "blog"
title = "TIL: how to turn a Bash array into command arguments"
date = "2022-12-03"
tags = [
  "til",
  "sqlite",
  "shell"
]
description = "Just a quick \"today I learned\" sharing how to turn a Bash array into command arguments with GNU xargs using SQLite as an example."
+++

Hey everyone, this is just a quick "today I learned" post to share how I was able to pass a Bash array of arguments to SQLite to execute something like the following:

```bash
sqlite3 :memory: -cmd 'PRAGMA foreign_keys = ON' -cmd '.version' 'SELECT strftime("%s")'
```

This technique isn't specific to `sqlite3`, it was just what I was working with at the time when I figured this out, and I think it serves as a good example of it.

In case you're curious, that creates an in-memory database, runs commands to [turn on foreign key enforcement](https://www.sqlite.org/foreignkeys.html) and print the version of SQLite you're using, and then runs a query to [compute the current Unix timestamp](https://www.sqlite.org/lang_datefunc.html). Nothing too fancy, I just want to demonstrate that it works with spaces and quotation marks and all that.

Let's start by defining our command array and query:

```bash
cmds=(
    'PRAGMA foreign_keys = ON'
    '.version'
)
query='SELECT strftime("%s")'
```

Just think of the query as an extra argument you're passing if you're not working with SQLite.

Now we need to build up our argument list. We can do that by separating each argument using a newline and passing them all to GNU [xargs](https://en.wikipedia.org/wiki/Xargs),[^1] telling it we want to use those newlines as the delimiter between arguments. Thinking back to our use case, each command and the `-cmd` preceding it are their own arguments, so we need newlines in between each of those too.

It's probably not the cleanest way to do it but here's how I accomplished that:

```bash
(
    echo :memory:
    printf -- "-cmd\n%s\n" "${cmds[@]}"
    echo "$query"
) | xargs -d "\n" sqlite3
```

The newlines are being added both at the end of the `echo` invocations and in the `printf` invocation; see the `\n`s in the format string? The `--` right before that format string is telling `printf` to not parse the `-` in the format string as the beginning of an option for it (`printf`) to interpret. If you're curious what you're feeding to `xargs`, try piping to `cat` instead!

[^1]: Friends on macOS: I know you already have an `xargs` command, but this will not work as-is using it. I just downloaded GNU xargs and replaced `xargs` in that code block with `gxargs` because that's what Brew installed it as. I thought about using `\0` as a delimiter (along with `xargs`' `-0` option) but decided I didn't want to spend time figuring it out when I already had this working.

I'm not a Bash (or SQLite) expert, but I hope I helped you a little with whatever you're working on!
