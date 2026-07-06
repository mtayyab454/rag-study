<!-- source: lib/screens/home_screen.dart, lib/state/app_state.dart (setMachinesToday/showAllMachinesToday/swapMachine/removeMachineFromToday/regenerateToday), lib/engine/session_builder.dart, lib/models/machine.dart (MachineLibrary, TrainingDay) -->

# The Today Screen: Shaping and Starting a Session

The **Today** tab is the heart of GymStart. It's where a session is shaped and then started. It's designed to feel fluid rather than like a form — the list of machines *is* the editor.

## What you see up top

At the top is a calm hero card showing today's weekday and a one-line summary. That summary reads either **"Picked for you"** (the app chose today's machines) or **"The machines you chose"** (you hand-picked them). If you're in a recovery week it adds "· easy week."

Below the hero, when today has machines, a short **coverage summary** shows which muscles today's session works, rolled up across all the machines and de-duplicated.

## Choosing how many machines: the Suggest chips

Above the machine list is a row labelled **Suggest** with chips for **2**, **3**, and **4**, plus a **Show all** chip.

- Tapping **2**, **3**, or **4** builds a fresh suggested session of that size for today. Importantly, the count is a *suggestion, not a lock*. A chip is only highlighted when today's session actually has that many machines — so if you add or remove a machine afterward, the chips simply reflect the real count.
- Tapping a count chip clears any hand-picked machines for today first, then generates a fresh set. This is intentional: otherwise an earlier explicit pick would override the suggestion and the chip would appear to do nothing.
- **Show all** puts every machine in your available pool (across both groups) into today's session at once.

## The machine list is the editor

Each machine appears as a light, tappable row showing its photo, name, group chip (A or B), today's target (sets × rep range · weight), and a small forward-looking forecast line ("+5 lb in ~3 easy sessions"). Two gestures shape the session:

- **Tap a machine** to open its slot sheet, where you can **swap it** for any other available machine — including one from the *other* group. Swapping keeps the machine's position so the rest of the session is undisturbed. It's a completely free choice; muscles and group are shown so you can keep the day balanced if you want.
- **Swipe a machine left or right** to remove it from today. If you remove the last machine, the app leaves the session empty rather than silently refilling it.

At the foot of the list is a dashed **"Add or choose machines"** tile that opens a flat picker of every machine you have available, so you can tick exactly what you want to do.

## How the app picks machines for you

When you're not hand-picking, GymStart generates the session automatically:

- A session is a **mix of both groups**, alternating A/B/A… The "day" that leads flips after each finished session, so consecutive sessions aren't identical.
- Within each group, machines you've trained recently are pushed toward the back, so a generated session rotates through your machines over time instead of repeating the same few.
- Only machines in your **available pool** are ever offered. If your pool is empty (not set yet), the app falls back to your gym type.
- The A/B groups are both **balanced, full-body** sessions (a leg movement, a push, a pull, core, etc.). The A/B label no longer means "push day vs pull day" — it just keeps sessions from repeating.

## Hand-picking exactly what you want

The **"Add or choose machines"** picker is a single flat list of everything available to you, each row tagged with its group and muscles. Tick the ones you want; on save, today's session is set to exactly those machines. Behind the scenes each pick is also filed under its A/B group, so your rhythm keeps working on future days.

## Regenerating

If you want a completely fresh suggestion, tapping a count chip (2/3/4) regenerates today's session from your rhythm and history. The generated session is remembered until you finish it or the day flips — so your swaps, removals, and count tweaks all stick in the meantime.

## Starting

The confident button at the bottom starts the session. It reads "Start — 3 machines" (or "1 machine", etc.), or "Pick machines to start" if the list is empty. Tapping it takes you into the session flow, beginning with a warm-up card. (In simulation mode, it first asks you to pick a date — see the Simulation Mode doc.)

## Your edits stick until the session is spent

When the app generates a session, it remembers it. Everything you do to shape today's list — swapping a machine, removing one, tapping a count chip, using Show all, or hand-picking from the picker — is saved into that remembered session. So if you back out of the Today screen and come back, your list is exactly as you left it. The remembered session is cleared only when you **finish** the session or when the **day flips** to the next A/B group after a completed session. At that point the next day generates fresh.

If a machine in your saved session becomes invalid — for example a custom machine you deleted, or a machine you removed from your available pool — it's quietly dropped from today's list the next time the list is read, so you never end up with a broken slot.

## The forecast line under each machine

Each machine row shows a small "+X lb in ~N easy sessions" line. This is a best-case forecast: it's what would happen if every upcoming session on that machine felt Easy or Just right. It's there to motivate, not to promise — the weight only ever moves up when you're ready. (The full rules behind it are in the How Progression Works document.)

## What the group chips (A / B) mean

Every machine shows a small **Group A** or **Group B** chip. These refer to the two halves of the rotation the app uses to keep consecutive sessions from being identical. Both groups are balanced full-body sessions, so the chip is informational — it doesn't restrict what you can do. You're free to mix machines from both groups in a single session, and the swap sheet deliberately offers machines from either group.

## Adding a brand-new machine mid-flow

The **"Add or choose machines"** picker lists machines you already have. If your gym has something GymStart doesn't list at all, you add it as a custom machine in Settings → My machines (covered in its own document). A custom machine assigned to today's group is appended to today's session the moment you add it, so it appears right away.

## Empty session

If you remove every machine, the app leaves the list empty rather than refilling it — a deliberate choice so it never overrides you. The start button then reads "Pick machines to start" and is disabled until you add at least one machine (via a count chip, Show all, the swap sheet, or the picker).

## Banners you might see

Depending on your recent activity, the Today screen may show a gentle banner at the top: a **recovery-week** note, a **rest-day** note if you trained very recently, a **friendly reminder** after a few quiet days (if reminders are on), or an orange **simulation-mode** banner. None of these ever block you from training.

## Quick recap

- The machine **list is the editor** — tap to swap, swipe to remove.
- **Suggest chips (2/3/4)** build a fresh set of that size; they're suggestions, not locks.
- **Show all** loads your whole available pool.
- Sessions are a **free mix of both groups**, favouring machines you haven't done recently.
- Your edits are **remembered** until you finish the session or the day flips.
- One button **starts** the session, beginning with a warm-up.
