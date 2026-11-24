import os
import sys

SENTENCE = "It is a road of wires joining town to town across the earth, where letters, pictures, and voices fly faster than any horse, so a man in London may speak with a friend in Canton while his tea cools."


def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
