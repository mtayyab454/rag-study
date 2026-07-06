<!-- source: lib/screens/settings_screen.dart, lib/state/app_state.dart, lib/data/local_store.dart, lib/screens/home_screen.dart, lib/screens/session_screen.dart, lib/screens/machine_finder_screen.dart, lib/models/onboarding_profile.dart -->

# FAQ & Troubleshooting

Short answers to common questions about GymStart.

## Accounts and data

**Do I need to create an account?**
No. GymStart has no accounts, no email, and no password. You go straight from the welcome screen into onboarding.

**How do I delete my account?**
There's no account to delete. To erase everything on the device, use **Settings → Start over**. It removes your answers, machine progress, and history and can't be undone. That's the closest thing to "delete my account."

**Does the app work offline?**
Yes, fully. Everything is stored locally on your device and nothing is sent anywhere, so setup and sessions work with no signal.

**How do I move my data to a new phone?**
Use **Settings → Backup → Copy my data** to export a block of text, save it somewhere (a note or an email to yourself), then **Restore from a backup** on the new phone. Restoring replaces whatever is on the new phone. Machine photos and simulated sessions don't travel.

**Is my data uploaded or synced to the cloud?**
No. There is no cloud and no sync. The only way data leaves the device is if you copy out a backup yourself.

## Sessions

**Why did the app pick these machines?**
When you don't hand-pick, GymStart builds a balanced mix from both groups, favouring machines you haven't trained recently and only using machines in your available pool.

**Can I do more or fewer machines?**
Yes. Use the **2 / 3 / 4** Suggest chips, tap **Show all**, or add/remove machines directly on the Today screen. The count is a suggestion, not a lock.

**How do I swap a machine?**
Tap it on the Today screen and pick a replacement from the sheet — any available machine, from either group.

**How do I remove a machine from today?**
Swipe it left or right on the Today screen.

**I ended a session early — did I lose my progress?**
No. Machines you already answered "How did that feel?" for keep their progress. Only the unfinished session isn't written to your history.

**Why is there a rest timer?**
A 60-second rest timer runs automatically between sets. You can tap **Skip rest** whenever you like.

## Weights and reps

**Why won't my weight go up?**
Weight increases after four "Easy" or "Just right" sessions accumulate on a machine. "Hard" sessions don't count toward that. Check the forecast line on the machine for how many easy sessions remain.

**The app suggested I go lighter — will it change my weight for me?**
No. The app never lowers weight automatically. After two Hard sessions in a row it *suggests* going lighter; you make the change with the − stepper.

**Can I set my own reps?**
Yes, in **Settings → Sets & reps**, per machine. Reps are a range you aim within and never change on their own.

## Machines

**How do I figure out what a machine on the floor is?**
Tap the search icon on the Today screen for the **"What's this machine?"** finder — a couple of plain questions identify it. It's a guided flow, not a camera scanner.

**Can I point my camera at a machine to identify it?**
Not currently. Identification is a guided question flow; a camera version would need a vision model. The guided flow works offline today.

**My gym has a machine you don't list — what do I do?**
Add it in **Settings → My machines → Add a machine**. Custom machines are always available to you.

## Simulation

**What is simulation mode?**
An off-by-default preview toggle that logs "what-if" sessions against a date you pick, so you can see how your calendar and charts fill in. Turn it off (and wipe the data) in Settings.
