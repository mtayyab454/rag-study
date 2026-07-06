<!-- source: lib/screens/add_machine_screen.dart, lib/screens/settings_screen.dart (_manageMachines/_CustomMachineRow), lib/state/app_state.dart (addCustomMachine/deleteCustomMachine/setMachinePhoto/clearMachinePhoto), lib/models/machine.dart (Machine.custom) -->

# Adding Your Own Machines and Photos

GymStart ships with a library of common machines, but your gym might have something it doesn't list. You can add your own, and you can put your own photo on any machine — bundled or custom.

## Adding a machine

Go to **Settings → My machines → Add a machine**. The form is deliberately short:

- **A photo** (optional) — take one or pick from your gallery, then crop.
- **What's it called?** — a free-text name, e.g. "Cable Crossover".
- **What does it work?** — one broad area: Legs, Chest, Back, Shoulders, Arms, or Hips.
- **Which muscles does it work?** (optional) — pick the main muscles, then any it also assists. A muscle can't be both primary and secondary; primaries win. These tags are what show on the machine and roll into your day's coverage summary.
- **Which day does it belong to?** — Day A or Day B.
- **Where should you start?** — a light starting weight, adjustable in 5 lb steps.

Sets and reps default to **3 × 8–12** and can be fine-tuned later in Settings → Sets & reps, which keeps this form short.

## What happens after you add one

A machine you add is:

- **Always part of your available pool** regardless of gym type, so it can be generated into sessions and picked in the swap list straight away.
- **Seeded with progression** immediately, using the starting weight you entered.
- **Added to today's session** right away if it belongs to today's group (appended, so nothing already shown is lost). If it's for the other day, it shows up when that day comes around, or you can add it via the picker or swap list.

The name is turned into a stable id and de-duplicated, so adding two "Cable Crossover"s won't collide.

## Replacing or removing a photo

You can set a photo on **any** machine, not just custom ones — tap its thumbnail (in Settings → My machines, or on the Sets & reps screen) to open the camera/gallery → crop flow.

- A photo you set is stored as an override keyed to the machine, so a built-in machine's shipped definition is never altered.
- Clearing the photo reverts a bundled machine to its original shipped photo, and a custom machine to whatever photo it was added with (or the placeholder if it had none).

Note: photos are stored as file paths, not image data, so they don't travel in a text backup — a machine restored on a new phone shows the placeholder until you set a photo again.

## Removing a custom machine

In Settings → My machines, tap the trash icon on a machine and confirm. Removing it takes it off your machine lists and clears its progress. **Past sessions that used it stay in your history** — they still read back correctly. Only machines you added yourself can be removed this way; bundled machines can't be deleted, only excluded from your available pool.
