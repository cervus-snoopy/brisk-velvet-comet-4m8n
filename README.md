# The Robot Pickup Line Championship

[![Bounty](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/cervus-snoopy/brisk-velvet-comet-4m8n/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/cervus-snoopy/brisk-velvet-comet-4m8n/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

This program writes a single one-line robot pickup line, built around the way a machine chooses exactly one device to reconnect to on its own, into `entry.txt`.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## Verify

```sh
wc -c /output/entry.txt
cat /output/entry.txt
```

The output is one line, at most 200 characters, with no trailing newline, written with mode 0644.
