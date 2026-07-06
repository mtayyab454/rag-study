<!-- source: lib/screens/available_machines_screen.dart, lib/widgets/available_machines_picker.dart (referenced), lib/state/app_state.dart (setAvailableMachines/availableMachineIds/isMachineAvailable), lib/engine/session_builder.dart (isAvailable), lib/models/machine.dart (idsForGym), lib/models/onboarding_profile.dart (GymKind/availableMachineIds) -->

# Your Available Machines and Gym Setup

GymStart only ever suggests machines you can actually use. The set of machines it draws from is your **available pool**, and this document explains how it's set and edited.

## Gym type vs. available pool

Two related things control what shows up:

- **Gym type** — Planet Fitness, a full gym, or a small/hotel gym. This is a shortcut: picking one pre-ticks a typical set of machines.
- **Available pool** — the actual checklist of machines you have. This is the authoritative thing; the gym type just gives you a sensible starting selection to trim or extend.

If you never set an explicit pool, the app falls back to your gym type so sessions still work.

## Setting it at onboarding

During onboarding, the "Which machines does your gym have?" screen lets you tap a gym type to tick a typical set, then add or remove any machine. You must select at least one machine to continue.

## Editing it later

Go to **Settings → Machines I have**. It's the same picker as onboarding:

- Tap a gym-type shortcut to reset the checklist to that gym's typical set, or
- Tick and untick individual machines.

When the current selection exactly matches a gym's preset, that gym is highlighted; if you've diverged from every preset, no gym is highlighted.

Saving updates your pool and **rebuilds today's session immediately**, so any machine you removed drops out at once, and anything you added becomes available to generate or swap in.

## How the pool affects sessions

- **Generated sessions** only ever pull from your available pool.
- **The swap sheet** on the Today screen only offers machines in your pool that aren't already in today's session.
- **Custom machines you added yourself are always available**, regardless of gym type.

## A machine isn't showing up

If a machine you expect isn't appearing in sessions or the swap list, check that it's ticked in **Settings → Machines I have**. If the Machine Finder identifies a machine that isn't in your gym's line-up, it shows a heads-up that the machine won't appear in your sessions until you add it to your pool.
