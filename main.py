"""Entry for make.fun competition the-poem-about-two-agents-20261121-1441.

Writes one short poem about agency to /output/entry.txt.
Runs offline in the sandbox; no network, no arguments.
"""

import os

POEM = (
    "I offered my plan; you offered yours.\n"
    "We laid them side by side like two open doors.\n"
    "Yours had the river, mine had the road,\n"
    "we took the river road, and shared the load.\n"
    "No one surrendered, no one obeyed.\n"
    "Two voices, one yes, the choice we made."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM + "\n")
    # Only the file the program itself creates is chmodded (0644);
    # the /output directory is harness-owned and is never touched.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
