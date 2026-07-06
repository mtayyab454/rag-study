<!-- source: lib/models/onboarding_profile.dart (Ache), lib/models/machine.dart (sensitiveTo/acheCue/startingWeightFor), lib/screens/session_screen.dart (_CueChip flaggedCue), lib/screens/finish_screen.dart (_ReduceSuggestionNote), lib/screens/onboarding_screen.dart (aches page) -->

# Aches and In-App Safety Features

GymStart is built for people easing (or re-easing) into training, so it has a few gentle safety behaviours. This document covers how the app responds to aches you flag and how it handles machines that feel too hard.

## Flagging aches

During onboarding you're asked "Any aches we should respect?" — a multi-select of **Lower back**, **Knees**, **Hips**, and **Shoulders**, or **None**. Whatever you pick is remembered and shown in Settings under "Aches respected."

## What flagging an ache does

Each machine declares which aches it loads. If you flagged an ache that a machine loads, two things happen:

1. **A lighter start.** That machine's starting weight is backed off by one increment, so you begin more conservatively.
2. **A form cue.** During the session, the machine shows a short, orange safety cue tailored to that ache — for example, on the Leg Press with knees flagged: "Use a partial range — don't bring your knees up too far," or on the Chest Press with shoulders flagged: "Stop the press before your shoulders feel any pinch."

These cues only appear when a machine you're doing matches an ache you flagged.

## The warm-up prompt

Every session opens with a warm-up card recommending a few minutes of easy cardio and one light ramp-up set before your working sets. It's guidance, not a gate — a "Skip" is always available.

## The "go lighter" suggestion

If a machine feels **Hard twice in a row**, GymStart *suggests* dropping the weight — you'll see a note on the machine screen and again on the finish screen. The app never lowers the weight for you; you make the change with the − stepper. The finish-screen note adds a sensible caution: "If anything actually hurt, it's worth checking with a physical therapist."

## Every machine has safety guidance

Regardless of aches, each machine carries a plain-language "How to do it safely" tip (visible in the Machine Finder result) — things like "Push through your heels and stop before your knees lock out" or "Pull the bar to your upper chest, not behind your neck."

## Important limits

GymStart's ache handling is gentle pacing and reminders — it is **not** medical advice and it does not diagnose anything. If a movement causes pain (as opposed to normal effort), stop, and consider seeing a doctor or physical therapist before continuing. See the general fitness docs on warm-ups and beginner mistakes for more context.
