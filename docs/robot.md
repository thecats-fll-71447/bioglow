---
layout: page
title: Cat-Bot
permalink: /robot/
---

<p class="todo">📷 Add a photo: save it as <code>docs/assets/images/cat-bot.jpg</code>, then replace this box with<br><code>![Cat-Bot]({{ "/assets/images/cat-bot.jpg" | relative_url }})</code></p>

## The robot

- **Drive:** two motors drive the wheels.
- **Attachments:** **one** motor powers *every* attachment through a shared
  mounting spot (our *attachment template*), so swapping attachments is fast.
- **Brains:** a SPIKE Prime hub running **Pybricks** — we switched from the
  SPIKE app to Pybricks so we could code in **Python**.
- **The clever part:** a forward-facing **color sensor**. Each attachment has a
  colored brick on it, and Cat-Bot reads that color to decide which code to
  run. Put on the RED attachment → it runs the rock mission. BLUE or YELLOW →
  it runs a different part of the leaves mission. Fewer wrong-program mistakes
  at the table!

## How we designed it

We followed the engineering design process from the Engineering Notebook:
**Identify → Design → Create → Iterate → Communicate.**

### Identify: Points vs. Effort
As a team we went through every mission, rated how hard it was, and compared
that to how many points it was worth. We skipped missions that were too hard
for too few points.

### Design & Create
- Everyone had their own **practice robot**, so nobody had to wait in line.
- We used an **Xbox controller** to test attachments quickly before writing code.
- Our coaches documented builds in **Studio** so we could rebuild and share them.
- We learned about **passive attachments**: a rubber band can replace a motor —
  load, push, release, *snap*.

### Iterate: The Solved Rule
A mission is only **solved** when it works **3–5 times in a row**. Before we
had that rule we'd sometimes work on one idea for days. Now we know when to
keep going, when to rebuild, and when to **keep it simple**.

### What we learned
- Robots need to be **stable and compact** to work well.
- **Settle on a robot design early**, so you can spend your time solving missions.
- Attachments that all mount the **same way** save time in every match.
