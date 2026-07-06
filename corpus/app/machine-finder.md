<!-- source: lib/screens/machine_finder_screen.dart, lib/screens/home_screen.dart (search action) -->

# The Machine Finder: "What's This Machine?"

Standing in front of a machine on the gym floor and not sure what it is? GymStart has a guided identifier that names it in two or three taps — no camera or signal required.

## Where to find it

On the **Today** screen, tap the **search icon** (🔍) in the top bar, labelled "What's this machine?".

## How it works

The finder asks a couple of plain-language questions and narrows down to the exact machine. It's a small decision tree, not a photo scanner.

1. The first question is **"What does it look like you'd do on it?"** with four options:
   - *Push something away with my feet* → identifies the Leg Press directly.
   - *Push handles with my arms* → asks which way the handles move (out in front → Chest Press; up overhead → Shoulder Press; sweeping together → Pec Fly; straight down → Triceps Press).
   - *Pull handles toward me* → asks where you're pulling from (down from above → Lat Pulldown; back toward your stomach → Seated Row; sweeping out and back → Rear Delt Fly; curling toward your shoulders → Biceps Curl).
   - *Move my legs against a pad* → asks how your legs move (kicking a pad up → Leg Extension; curling a pad down → Seated Leg Curl; pressing knees outward → Hip Abduction).

2. Once it lands on a machine, you get a **photo-first result**: the machine's picture, its name and group, a one-liner, the muscles it works, a "How to do it safely" block, and a "Why this works" block.

3. If the identified machine isn't in your gym's usual line-up, a heads-up note tells you it won't appear in your sessions.

You can tap **Back** to change an answer, or **Identify another machine** to start the tree over.

## Why it's a guided flow and not a camera

A point-the-camera version would need a trained vision model. The guided question flow ships today, works with no signal, and gets you the same answer.
