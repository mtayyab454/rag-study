<!-- source: lib/screens/session_screen.dart, lib/screens/finish_screen.dart, lib/state/app_state.dart (recordFeedback/finishSession/discardPendingSession) -->

# How to Run a Session, Step by Step

Once you tap **Start** on the Today screen, GymStart walks you through one machine at a time. Here's exactly what happens, in order.

## Steps

1. **Warm up first.** The session opens on a short warm-up card. It suggests 5–8 minutes of easy cardio (a treadmill walk, the bike, or the cross-trainer) and one light ramp-up set on your first machine. Tap **"I'm warmed up — let's go"** or **"Skip — already warmed up"** to continue. The warm-up never blocks you.

2. **See the first machine.** Each machine takes the full screen: a photo you can tap to enlarge, its name, a plain-language one-liner, its group chip, the muscles it works, and a large **"Today's target"** card showing sets × rep range and the working weight.

3. **Adjust the weight if you want.** The target card has **−** and **+** steppers that move the weight in 5 lb steps. Tapping either sets a new baseline — the automatic-progression tally resets from there. Weight never goes below 0.

4. **Do your sets and check them off.** Tap **"I finished set 1"**, then set 2, and so on. A row of dots fills in as you go, and a **60-second rest timer** starts automatically between sets (never after the last one). You can tap **Skip rest** at any time.

5. **Answer "How did that feel?"** When you're done, tap **"Done with this machine"**. A sheet asks the single question that tunes your next session, with three big buttons: **Easy**, **Just right**, or **Hard**. This is the only feedback the app ever asks for.

6. **Move to the next machine.** Your answer is recorded and the app advances. Repeat steps 2–5 for each machine.

7. **Finish.** After the last machine, you reach the finish screen: a checkmark, "You finished," your running session count, and — if any machine felt Hard twice in a row — a gentle suggestion to go lighter on it next time. Tap **Done** to return home.

## What "How did that feel?" does

- **Easy** or **Just right** counts toward a weight increase. After four such sessions on a machine (not necessarily consecutive), the working weight goes up by one increment on its own.
- **Hard** repeats everything unchanged — it neither adds to nor resets the tally. Two Hards in a row makes the app *suggest* (never force) dropping the weight a little.

The app never lowers a weight for you. Increases happen automatically; decreases are always your call via the − stepper.

## Ending a session early

Tap the **✕** in the top-left to end early. The app confirms, then keeps your progress on machines you already answered for — those are saved as they happen. The unfinished session simply isn't written into your history log.

## What gets saved

When you reach the finish screen, GymStart commits the session to your history (what you did on each machine, at what weight, and how it felt), advances the A/B rotation for next time, and bumps the deload counter. Your completed-session count goes up by one.
