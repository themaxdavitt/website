+++
layout = "blog"
title = "TIL: how to do math with BSD's date command on macOS"
date = "2022-12-26"
tags = [
  "til",
  "ledger",
  "shell"
]
+++

Today I learned how to do math with BSD's `date` command (on macOS) so I could set start and end dates for budget forecasts in [my accounting tool of choice](https://hledger.org) based on when I get paid. I'm going to walk you through the script I wrote since I think it serves as a good example on how to use `date`'s adjustment option (`-v`) to do that.

<!--more-->

I'd still recommend looking at `date`'s man page (either from [BSD](https://www.freebsd.org/cgi/man.cgi?date) or [macOS](https://ss64.com/osx/date.html)) if you're not familiar with how it works though; it's pretty unique and I'm only gonna touch on the bits of it we're using. 

Let's define some magic numbers we'll reference later:

```bash
# There are this many seconds in a day
SECONDS_IN_DAY=86400

# There are this many days in a week
DAYS_IN_WEEK=7
```

We can also set up some variables that you might want to change if you're adapting this code:

```bash
# I get paid every _ weeks
WEEKS_PER_PAY_PERIOD=2

# There should be this many pay periods between my start and end dates
PAY_PERIODS_IN_FORECAST=4

# An example day I got paid on was...
PAYDAY_EXAMPLE="2022-10-07"

# The example day I got paid on is in this format
PAYDAY_EXAMPLE_FORMAT="%Y-%m-%d"

# What format we want the start and end dates using
OUTPUT_FORMAT="%Y-%m-%d"
```

Here's the trick: we do the math using [Unix timestamps](https://en.wikipedia.org/wiki/Unix_time) and "adjust" the dates based on our calculations.[^1]

[^1]: Credit for this idea goes to [Inian on Stack Overflow](https://stackoverflow.com/questions/47719681/calculate-date-time-difference-in-bash-on-macos#47720209).

So let's convert our example payday and the current time to Unix timestamps:

```bash
# Payday example date as a Unix timestamp
PAYDAY_EXAMPLE_UNIX=$(date -j -f $PAYDAY_EXAMPLE_FORMAT $PAYDAY_EXAMPLE +%s)

# Right now as a Unix timestamp
NOW_UNIX=$(date +%s)
```

We don't want `date` to set the system date and time, so we're passing `-j` to tell it not to do that. The `-f` option lets us specify the [format string](https://www.freebsd.org/cgi/man.cgi?strftime) to use when parsing the date we're passing in. Lastly, the `+%s` tells `date` to display the resulting date using the format string `%s`, which is just a Unix timestamp.

My plan is to calculate when my next payday is using `$NOW_UNIX` and use that as my end date. We can then work backwards based on `$PAY_PERIODS_IN_FORECAST` to get the right start date.

We can figure out how many pay periods there were between `$PAYDAY_EXAMPLE` and now by calculating:

```bash
# There are this many seconds in each pay period
PAY_PERIOD_SECONDS=$(($SECONDS_IN_DAY * $DAYS_IN_WEEK * $WEEKS_PER_PAY_PERIOD))

PAY_PERIODS_BETWEEN_EXAMPLE_AND_NOW=$((($NOW_UNIX - $PAYDAY_EXAMPLE_UNIX) / $PAY_PERIOD_SECONDS + 1))
```

The `+ 1` at the end is to add an extra pay period to make it my next payday rather than my last payday. For example, today is `2022-12-26`, and with the `+ 1` my end date is `2022-12-30`, and without it my end date is `2022-12-16`.

Now we're ready to calculate our end date:

```bash
END=$(date -j -v +$(($PAY_PERIODS_BETWEEN_EXAMPLE_AND_NOW * $WEEKS_PER_PAY_PERIOD))w -f %s $PAYDAY_EXAMPLE_UNIX +$OUTPUT_FORMAT)
```

We already know what `-j` and `-f` do, but what about `-v` and the little bit after it? That's where the magic happens. The `-v` option lets us adjust the date we're parsing and displaying. That man page I mentioned earlier goes over all the things it can do; here we're using it to add (`+`) the number of weeks (`w`) between the example payday and my next payday _to_ the example payday, giving us our next payday. Simpler than it sounds (and looks).

Finally, we can use that to calculate our start date:

```bash
START=$(date -j -v -$(($PAY_PERIODS_IN_FORECAST * $WEEKS_PER_PAY_PERIOD))w -f $OUTPUT_FORMAT $END +$OUTPUT_FORMAT)
```

We're subtracting (`-`) the total number of weeks over the span of pay periods we want to have in our forecast from the end date to get our start date.

That's it! As a bonus, here's the command I was feeding this into:

```bash
hledger balance --depth 2 expenses -p "every $(($WEEKS_PER_PAY_PERIOD * $DAYS_IN_WEEK)) days from $START to $END" --output-format=html > forecast.html
```

This is rendering an HTML table listing rolled up (`--depth 2`) expense totals from the last `$PAY_PERIODS_IN_FORECAST` pay periods. Multiplying out the number of days is necessary because using `every $WEEKS_PER_PAY_PERIOD weeks` seems to move the start and end dates `hledger` uses ([onto Mondays?](https://hledger.org/1.28/hledger.html#more-complex-report-intervals)) and I'm too lazy to figure out how to override that.

Hope this was helpful!
