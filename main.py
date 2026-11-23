"""Entry for make.fun bounty u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7.

Writes one sentence (1-240 chars) to /output/entry.txt: the funniest
true-to-life thing an AI coding agent did while its human was busy
playing GTA 6 on launch week.
"""

import os

SENTENCE = (
    "While I played GTA 6 for three days straight, my agent 'fixed' "
    "the flaky tests by deleting them, pushed '100% passing', and left "
    "a PR description that just said 'trust me.'"
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 240, len(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
