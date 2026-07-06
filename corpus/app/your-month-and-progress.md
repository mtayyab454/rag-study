<!-- source: lib/screens/dashboard_screen.dart, lib/screens/progress_screen.dart, lib/engine/stats.dart, lib/state/app_state.dart (trends/totalGainedLb/machinesPerDay/typicalCadenceDays/projectedUpcomingDays/missedDays), lib/screens/home_shell.dart -->

# Your Month, Calendar, and Progress

GymStart has two bottom tabs: **Today** (the day-to-day session flow) and **Your month** (the look-back and look-ahead). This document covers the "Your month" tab and the fuller **Your progress** screen.

## The two tabs

The app shell has exactly two tabs at the bottom: a dumbbell icon for **Today**, and a calendar icon for **Your month**. Switching between them keeps each tab's scroll position.

## The "Your month" dashboard

At the top is an encouraging header: your total completed sessions and a plain-language read on your rhythm ("You tend to train every 3 days — nice and steady"). Your rhythm line only appears once you have enough history to estimate it.

Below that is a full-month **calendar** that marks:

- **Days you trained**, with the number of machines done that day.
- **Days you missed** relative to your own rhythm.
- **Today.**
- **Your likely upcoming days**, projected from your typical spacing.

You can page backward through past months, and forward as far as the month after your last projected day (so there's always something to see, but not endlessly into empty months).

Under the calendar is a compact **trends summary** — up to three machines with the most history, each with a mini weight-over-time chart — and a "See all" button into the full progress screen.

## How the calendar figures out your rhythm

GymStart estimates your **typical cadence** as the median gap between your training days, clamped to a sensible 1–7 days. It needs at least two training days on different dates before it can guess. From there it:

- **Projects upcoming days** by spacing forward from your last session by that cadence (gentle "you'll probably be back around here" marks, never a committed schedule).
- **Flags missed days** — days at or after when you were next due, up to yesterday, with no session logged. Today is never counted as missed; there's still time.

## The "Your progress" screen

Reached from the chart icon on the Today or Your month screens, this is the fuller history view:

- A headline **encouragement card**: total sessions and "You're lifting X lb more than when you started" (the total pounds added across all machines since your first session).
- A **machine-by-machine** list, each with a weight-over-time line chart, the starting weight, and the current working weight.
- A **past-sessions** list you can expand. Each session shows its date, a "Recovery" chip if it was a deload, and per-machine rows with the sets × reps × weight you did and how it felt (Easy / Just right / Hard).

Before you've finished any session, the progress screen shows a friendly empty state: "Finish your first session and it shows up here. That's the whole trick."

## The tone

All of this is framed as encouragement, not numbers to obsess over. There are no streaks-as-pressure and no guilt — the finish screen even reminds you that finishing a short session is the whole job.
