<!-- source: lib/state/app_state.dart (simulationMode/setSimulationMode/hasSimulatedData/deleteSimulatedData/finishSession), lib/screens/home_screen.dart (_startSession/_SimulationBanner), lib/screens/settings_screen.dart (simulation section), lib/data/local_store.dart (simulationMode/exportBackup) -->

# Simulation Mode

Simulation mode is a preview toggle for filling your calendar and progress charts with "what-if" data, so you can see how they'll look as you use the app. It's off by default and lives in **Settings → Simulation**.

## What it changes

When simulation mode is **on**:

- An orange banner appears on the Today screen so it's always obvious what will happen.
- When you tap **Start** on the Today screen, GymStart first asks you to **pick a date** (anywhere from two years back to two years ahead). The session is then logged against that date.
- The resulting session record is tagged as **simulated** — a what-if entry.

## What it does and doesn't affect

- Simulated sessions **do** show up on the calendar and in your progress charts, so you can preview how they fill in.
- Simulated sessions **do** move your real progression weights, just like normal sessions — the weight changes are real.
- Simulated sessions are **never** included in a backup — they don't travel to a new phone.

## Cleaning up

When you have simulated data, a **Delete simulated data** button appears in Settings. It removes every what-if session, leaving your real sessions untouched. One caveat: the weight changes those simulated sessions caused are **not** rewound — only the dated calendar/chart entries are cleared.

## When to use it

It's primarily a developer/preview convenience. If you just want to try the app normally, leave simulation mode off; a normal session is logged against the current date without asking.
