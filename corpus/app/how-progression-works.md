<!-- source: lib/engine/progression_engine.dart, lib/models/progression_state.dart, lib/models/onboarding_profile.dart (weightIncrementLb/needsTwoEasies/startsLight), lib/state/app_state.dart (adjustWeight/deloadDue/displayWeightFor), lib/models/machine.dart (startingWeightFor/repRangeFor) -->

# How GymStart Decides Your Weights and Reps

GymStart handles the "how much should I lift?" question for you, gently. This document explains the rules the app follows so nothing feels like a black box.

## Weight is the thing that climbs

In GymStart, **weight is what progresses automatically; reps are a range you train within and only you change.** The engine never moves your rep range on its own.

## Your starting weight

When you first get a machine, the app sets a conservative starting weight based on your onboarding answers. There are two starting tiers — a lighter one and a moderate one. You start on the lighter tier if you said you're "mostly sitting" or you're 50 or older. If you flagged an ache that a particular machine loads, the app backs its starting weight off by one increment as well.

## How weight goes up

After each session you answer "How did that feel?" for each machine. The engine tallies your **Easy** and **Just right** answers (they don't have to be consecutive). Once **four** such qualifying sessions have accumulated on a machine, the working weight goes up by one increment and the tally resets.

A **Hard** answer doesn't add to the tally, but it doesn't reset it either — you simply repeat the same weight next time.

## How big is one increment?

The weight jump depends on your profile:

- If you said you're "pretty active" and you're under 45, an increment is **10 lb**.
- Otherwise (including "mostly sitting" or age 50+), an increment is **5 lb**.

The in-session weight steppers move in 5 lb steps to match the gentlest auto-increment.

## The app never lowers weight for you

Weight only ever goes up automatically. When a machine has felt **Hard twice in a row**, the app *recommends* going a little lighter — you'll see a note on the machine and on the finish screen — but it leaves the actual change to you. You lower it yourself with the − stepper.

## Manually nudging the weight

You can tap − or + on any machine's target card during a session. When you do, that new value becomes the baseline: the auto-increment tally and the consecutive-Hard streak both reset, so progression starts fresh from there.

## Reps are a range, and they're yours

Each machine has a default rep range (for example 8–12, or 10–15 for many leg machines). Your optional goal shifts that range a little: "Get stronger" trims it toward heavier/fewer reps, "Feel better" nudges it lighter/more reps, and "Build some muscle" leaves it as designed. The low end never drops below 5 so it stays joint-friendly. You can also set your own sets and rep range per machine in Settings → Sets & reps; once you do, your choice is used and the app never changes it.

## Anchor machines

A few machines are "anchors" — heavier, lower-rep movements (like the Lat Pulldown and Back Extension) that default to roughly a 5–8 rep range. They're there for quality reps if you enjoy that heavier style.

## The forecast line

Everywhere a machine is shown, GymStart displays a best-case forecast: how many more easy sessions until the weight goes up, and by how much (for example, "+5 lb in ~3 easy sessions"). It's framed as best-case — "if it keeps feeling easy" — so it motivates without over-promising. Under the hood it simulates the real engine, so it can never drift from the actual rules.

## Recovery weeks (deload)

Roughly every seven sessions, GymStart nudges a lighter recovery week: today's weights are shown about 20% lighter (rounded to the nearest 5 lb) for that session only. Your stored progression isn't changed — it's just an easier week, because easy weeks are how you keep going. See the Recovery, Rest & Reminders doc for more.
