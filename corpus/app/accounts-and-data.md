<!-- source: lib/data/local_store.dart, lib/screens/settings_screen.dart, lib/state/app_state.dart (exportBackup/importBackup/startOver), lib/screens/onboarding_screen.dart (welcome copy) -->

# Accounts, Privacy & Your Data

GymStart has no accounts and no cloud. This document explains where your data lives, how it moves (only when you move it), and what the app never does.

## There is no account

You never create a username, email, or password. The welcome screen states it directly: "No accounts. Everything stays on your phone." There is no login screen anywhere in the app, and there is no "signed-in" state tied to a server — the only thing the app checks is whether you have completed onboarding on this device.

## Where your data lives

Everything the app knows is stored locally on your device as small JSON blobs (via the device's shared-preferences store). That includes:

- Your onboarding profile (age, activity level, aches, goal, gym type).
- Your available-machines pool and any per-day picks.
- Per-machine progression (current working weight, your sets/rep-range choices, your last "how did it feel" answer, and the internal counters that drive weight changes).
- Your session history.
- Any machines you added yourself and any machine photos you set.
- Small counters like total completed sessions and where you are in the deload cycle.

Because it's all local, the app is fully offline-first. Nothing is transmitted anywhere.

## Nothing is sent anywhere

The Settings screen repeats the promise: "Everything is stored only on this phone. There are no accounts and nothing is sent anywhere." Your data is never uploaded, synced, or shared unless *you* copy it out yourself using the backup feature below.

## Moving to a new phone: backup and restore

Since there's no cloud sync, GymStart lets you carry your data across devices manually with a copy-and-paste backup.

- **Copy my data** exports everything the app knows as a single block of text and puts it on your clipboard. Paste it somewhere safe — a notes app, or an email to yourself.
- **Restore from a backup** takes that pasted text on a new phone and rebuilds your profile, progression, custom machines, history, and counters. Restoring **replaces everything** currently on that phone.

Two details worth knowing:

- **Simulated (what-if) sessions are never included in a backup.** Only your real history travels.
- **Machine photos are stored as file paths, not the image bytes.** A custom machine restored on a new phone shows the placeholder illustration until you set a photo again.

If you paste something that isn't a valid GymStart backup, nothing changes and the app tells you so.

## Erasing everything

**Start over** in Settings wipes your answers, machine progress, and history from the device. It cannot be undone, and it returns you to onboarding. There is no separate "delete my account" action because there is no account to delete — erasing the local data is the whole story.

## What GymStart collects about you

Only what you tell it during setup and use: your age, activity level, any aches, your optional goal, your gym type, which machines you have, and what you did in each session. It does not ask for your body weight, your name, or contact details, and it has no analytics account tied to you.
