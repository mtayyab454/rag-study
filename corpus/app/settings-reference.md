<!-- source: lib/screens/settings_screen.dart, lib/models/onboarding_profile.dart (Goal/GymKind/MuscleColorMode), lib/state/app_state.dart (setGoal/setGym/setRemindersOn/setMuscleColorMode/setSimulationMode/deleteSimulatedData/startOver/exportBackup/importBackup) -->

# Settings Reference

Everything on the Settings screen, top to bottom. Reach it from the gear icon on the Today screen. Settings still has no accounts, and nothing leaves your device unless you copy it out yourself.

## Your profile at a glance

The top of Settings shows read-only info from onboarding: your **Age**, **Activity** level, the **Aches respected**, and your total **Sessions done**. These come straight from your onboarding answers (changing them means starting over).

## Adjustable settings

| Setting | What it does | Options / values | Notes |
|---|---|---|---|
| **Goal** | Nudges your rep ranges | Get stronger · Feel better day-to-day · Build some muscle · No goal | Optional; changeable any time. Strength = heavier/fewer reps, Feel better = lighter/more reps. |
| **Machines I have** | Your available pool — the machines every session draws from | Checklist of machines, with a gym-type shortcut | Same picker as onboarding. Saving rebuilds today's session so removed machines drop out at once. |
| **Sets & reps** | Per-machine sets and rep range | Sets 1–6, reps 5–30 (per machine) | A one-time setup choice, not a per-session tweak. Values are clamped to safe bounds; weight is never touched here. |
| **My machines** | Add, photo, or remove your own machines | Add / remove | Custom machines are always available. Removing one clears its progress but keeps past history. |
| **Muscle tag colours** | How muscle tags are coloured | Colour by body area · One colour | Purely visual. Defaults to one colour. |
| **Gentle reminders** | Home-screen nudge after quiet days | On / Off | On by default. Never pushy; shows only after ~3 quiet days. |
| **Simulation mode** | Log what-if sessions against a chosen date | On / Off | Off by default. See the Simulation Mode doc. |

## Backup

Two buttons:

- **Copy my data** — exports everything as text to your clipboard to paste somewhere safe.
- **Restore from a backup** — pastes that text back in (replaces everything currently on the device).

No account is needed; this is how your data survives a new phone. Simulated sessions are never included in a backup, and machine photos (stored as paths) don't travel.

## Simulation controls

When simulation mode is on and you've logged what-if sessions, a **Delete simulated data** button appears. It removes every what-if session (your real sessions stay). Note: weight changes those simulated sessions caused are *not* rewound.

## Start over

At the very bottom, **Start over** erases your answers, machine progress, and history and returns you to onboarding. It asks for confirmation and **cannot be undone**. There's no "delete account" because there's no account — this is the erase-everything action.

## Bounds worth knowing

- Sets per machine: **1–6**.
- Reps per machine: **5–30** (the low end never below 5, for joint-friendliness).
- Machines suggested per session: **2–4** (via the Suggest chips) or "Show all".
