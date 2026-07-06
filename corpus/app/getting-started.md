<!-- source: lib/main.dart, lib/screens/onboarding_screen.dart, lib/models/onboarding_profile.dart, lib/state/app_state.dart (completeOnboarding) -->

# Getting Started with GymStart

GymStart is a gym app built for people who are easing into strength training. The whole idea is to remove friction: a few taps to set up, one short session picked for you, and no accounts to create. This guide walks through what happens the first time you open the app.

## The first thing you see

When you launch GymStart for the very first time, it opens straight into onboarding. There is no sign-up screen, no email field, and no password to remember. The welcome screen says it plainly: "No accounts. Everything stays on your phone." The app decides whether to show onboarding or your home screen based only on whether you have finished onboarding before — nothing is checked against a server.

## The onboarding questions

Onboarding is deliberately short — around six screens, each with big tappable buttons and almost no typing. You move forward one screen at a time, and a row of progress dots at the top shows where you are.

1. **Welcome.** A short hello and a "Let's go" button.
2. **How old are you?** A scrolling wheel from 35 to 60, defaulting to 42. Your age gently affects pacing — the app keeps things a little gentler toward the upper end.
3. **How active have you been lately?** One of three choices: *Mostly sitting*, *Somewhat active*, or *Pretty active*. There's no wrong answer; it just sets a comfortable starting point for your weights.
4. **Any aches we should respect?** A multi-select list — *Lower back*, *Knees*, *Hips*, *Shoulders* — or tap *None*. The app goes a little lighter on machines that load an ache you flagged, and may show a short form cue for those machines.
5. **Which machines does your gym have?** Tap a gym type (*Planet Fitness*, *A full gym*, or *A small / hotel gym*) to tick a typical set of machines, then add or remove any. You must pick at least one machine before continuing. This becomes your "available pool" — GymStart only ever suggests machines you can actually use.
6. **Any particular hope?** An optional goal: *Get stronger*, *Feel better day-to-day*, or *Build some muscle*. This is entirely optional — the button reads "Skip — build my session" if you don't choose one. Your goal nudges your rep ranges slightly and can be changed any time.

## What happens when you finish

When you tap the final button, GymStart saves your answers, seeds a conservative starting weight for every machine you might be assigned, and builds your first session. From then on the app opens to the **Today** screen instead of onboarding.

Your `machinesToday` count defaults to 3 after onboarding, meaning a typical suggested session has three machines — but you can change that on the Today screen at any time.

## Do I need an internet connection?

No. GymStart is offline-first. Everything is stored locally on your device, and no part of setup requires a signal. You can complete onboarding and run sessions on a plane.

## Redoing onboarding

You can re-run the whole onboarding flow later by choosing **Start over** in Settings. That erases your answers, machine progress, and history and returns you to the welcome screen. See the Settings and FAQ documents for details on what "Start over" removes.
