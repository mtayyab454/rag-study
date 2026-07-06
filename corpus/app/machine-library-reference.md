<!-- source: lib/models/machine.dart (MachineLibrary, all machine definitions, MuscleGroup, TrainingDay, GymKind gyms sets) -->

# Machine Library Reference

GymStart ships with a library of beginner-safe, supported/selectorized machines, split across two rotation groups (A and B). Both groups are balanced full-body sessions — the A/B label just keeps consecutive sessions from being identical, it doesn't mean "push day vs pull day." This is a reference to the bundled machines.

## Bundled machines

| Machine | Group | Primary area | Default sets × reps | In basic/hotel gym? |
|---|---|---|---|---|
| Leg Press | A | Legs (quads, glutes) | 3 × 10–15 | Yes |
| Chest Press | A | Chest | 3 × 8–12 | Yes |
| Shoulder Press | A | Shoulders | 3 × 8–12 | No |
| Lat Pulldown *(anchor)* | A | Back | 3 × 5–8 | Yes |
| Seated Leg Curl | A | Legs (hamstrings) | 3 × 10–15 | Yes |
| Back Extension *(anchor)* | A | Lower back | 3 × 5–8 | Yes |
| Abdominal Crunch | A | Core | 3 × 12–20 | Yes |
| Biceps Curl | A | Arms | 3 × 10–15 | No |
| Leg Extension | B | Legs (quads) | 3 × 10–15 | Yes |
| Pec Fly | B | Chest | 3 × 10–15 | No |
| Seated Row | B | Back | 3 × 8–12 | Yes |
| Assisted Pull-up | B | Back | 3 × 6–10 | No |
| Hip Abduction | B | Hips (outer) | 3 × 10–15 | No |
| Hip Adduction | B | Hips (inner) | 3 × 10–15 | No |
| Rear Delt Fly | B | Shoulders | 3 × 10–15 | No |
| Triceps Press | B | Arms | 3 × 10–15 | No |
| Rotary Torso | B | Core | 3 × 12–20 | No |

## Anchor machines

Two machines are marked as **anchors** — heavier, lower-rep movements you can do for quality reps if you enjoy that style: the **Lat Pulldown** and the **Back Extension**, both defaulting to about 5–8 reps.

## Gym types

Each machine declares which gym types stock it. The three gym types are **Planet Fitness**, **A full gym**, and **A small / hotel gym**. Picking a gym type at onboarding (or in Settings) pre-ticks a typical set of machines as a shortcut — but the checklist you end up with is what's authoritative. The "In basic/hotel gym?" column above reflects the small/hotel-gym set, which is the most limited.

## Substitution groups

Machines that train the same movement share a substitution group, so one can stand in for another when a machine is busy or when a flagged ache makes it uncomfortable. For example, the Chest Press and Pec Fly are both "horizontal push"; the Lat Pulldown and Assisted Pull-up are both "vertical pull."

## What each machine shows

For every machine, the app can show a plain-language one-liner ("Works your legs while you sit — easy on the back"), a "How to do it safely" tip, a "Why this works" explainer, the specific muscles it works (primary and secondary), and — if you flagged a relevant ache — a short form cue like "Use a partial range — don't bring your knees up too far."
