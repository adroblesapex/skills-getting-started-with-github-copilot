---
name: add-participants-section
applyTo:
  - src/static/index.html
  - src/static/app.js
  - src/static/styles.css
description: |
  Update the activity cards in the web UI to show a participants section for each activity.
  The participants list should be rendered as a bulleted list beneath the activity details and styled to match the existing card design.
  Use the existing API response fields, preserve current activity card content, and keep the page visually clean and pretty.
---

When editing `src/static/app.js`, add participant rendering logic inside the activity card creation block. When editing `src/static/styles.css`, add styling for the participants list and card section so it looks polished and matches the current blue/white theme. Keep `src/static/index.html` unchanged unless structure changes are required for the new participant section.
