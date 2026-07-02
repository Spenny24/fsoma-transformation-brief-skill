"""
Generates a 2x2 impact vs effort chart as a PNG, for embedding into the
FSOMA Transformation Brief Kit docx.

Usage:
    python generate_2x2.py --output impact_effort.png

Edit the WORKFLOWS list below (or wire it up to read from a JSON file
produced by Stage 2 of the pipeline) before running.

Each workflow needs:
    name: short label (keep under ~28 chars, it gets printed on the chart
          or in the legend, depending on collision density)
    impact: 1-10 (y-axis, higher = more impact)
    effort: 1-10 (x-axis, higher = more effort/cost to implement)

Quadrants (standard prioritization matrix):
    high impact, low effort   -> Quick Wins
    high impact, high effort  -> Major Projects
    low impact, low effort    -> Fill-Ins
    low impact, high effort   -> Deprioritize

Chart-safe formatting (Mandatory Analytical Behaviour 6):
    Inline text labels next to every point break down once several
    workflows cluster in the same quadrant, or once there are simply
    a lot of points on the chart. This script switches from inline
    labels to numbered markers with a legend whenever any of the
    following is true:
      - more than 8 items are plotted
      - two or more points sit within COLLISION_DISTANCE of each other
      - any single label is longer than MAX_INLINE_LABEL_LENGTH characters
    It is all-or-nothing per chart, a mix of inline labels and numbers
    on the same chart is harder to read than either approach alone.
"""

import argparse
import itertools
import matplotlib.pyplot as plt

WORKFLOWS = [
    # Replace with real Stage 2 output before running.
    {"name": "Brief intake & routing", "impact": 8, "effort": 3},
    {"name": "Planning synthesis", "impact": 9, "effort": 5},
    {"name": "Content prep & metadata", "impact": 7, "effort": 4},
    {"name": "Measurement reporting", "impact": 6, "effort": 3},
    {"name": "Creative concepting support", "impact": 7, "effort": 7},
    {"name": "Workflow orchestration", "impact": 8, "effort": 8},
]

# Points closer than this (in chart units, axes run 0-10) are treated as
# colliding. 1.4 is roughly the space a short label needs before it starts
# overlapping its neighbour's marker or text at this chart size.
COLLISION_DISTANCE = 1.4

# Labels longer than this look cramped directly on a data point regardless
# of collision, switch to the legend once any label crosses this length.
MAX_INLINE_LABEL_LENGTH = 18

# More than this many points makes even non-colliding inline labels feel
# busy, switch to the legend regardless of spacing.
MAX_INLINE_ITEM_COUNT = 8


def needs_legend(workflows):
    if len(workflows) > MAX_INLINE_ITEM_COUNT:
        return True
    if any(len(wf["name"]) > MAX_INLINE_LABEL_LENGTH for wf in workflows):
        return True
    for a, b in itertools.combinations(workflows, 2):
        dist = ((a["impact"] - b["impact"]) ** 2 + (a["effort"] - b["effort"]) ** 2) ** 0.5
        if dist < COLLISION_DISTANCE:
            return True
    return False


def generate_chart(workflows, output_path):
    use_legend = needs_legend(workflows)

    fig, ax = plt.subplots(figsize=(8, 6), dpi=150)

    ax.axvspan(0, 5, ymin=0.5, ymax=1, color="#E8F3E8", zorder=0)   # quick wins
    ax.axvspan(5, 10, ymin=0.5, ymax=1, color="#E8ECF3", zorder=0)  # major projects
    ax.axvspan(0, 5, ymin=0, ymax=0.5, color="#F5F5F0", zorder=0)   # fill-ins
    ax.axvspan(5, 10, ymin=0, ymax=0.5, color="#F3E8E8", zorder=0)  # deprioritize

    legend_lines = []
    for i, wf in enumerate(workflows, start=1):
        ax.scatter(wf["effort"], wf["impact"], s=110, color="#1F2937", zorder=3)
        if use_legend:
            ax.annotate(
                str(i),
                (wf["effort"], wf["impact"]),
                ha="center", va="center",
                color="white", fontsize=8, fontweight="bold",
                zorder=4,
            )
            legend_lines.append(f"{i}. {wf['name']}")
        else:
            ax.annotate(
                wf["name"],
                (wf["effort"], wf["impact"]),
                textcoords="offset points",
                xytext=(6, 6),
                fontsize=8,
                zorder=4,
            )

    ax.axhline(5, color="#999999", linewidth=0.8, zorder=1)
    ax.axvline(5, color="#999999", linewidth=0.8, zorder=1)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xlabel("Effort to implement", fontsize=10)
    ax.set_ylabel("Business impact", fontsize=10)
    ax.set_title("Impact vs Effort: Priority Workflows", fontsize=12, fontweight="bold")

    ax.text(1.2, 9.3, "Quick Wins", fontsize=9, color="#4A7A4A", fontweight="bold")
    ax.text(6.8, 9.3, "Major Projects", fontsize=9, color="#4A5A7A", fontweight="bold")
    ax.text(1.2, 0.5, "Fill-Ins", fontsize=9, color="#888880", fontweight="bold")
    ax.text(6.8, 0.5, "Deprioritize", fontsize=9, color="#7A4A4A", fontweight="bold")

    if use_legend:
        legend_text = "\n".join(legend_lines)
        fig.text(
            1.02, 0.5, legend_text,
            transform=ax.transAxes, fontsize=8, va="center", ha="left",
        )
        plt.subplots_adjust(right=0.62)
    else:
        plt.tight_layout()

    plt.savefig(output_path, facecolor="white", bbox_inches="tight" if use_legend else None)
    mode = "numbered markers + legend (>8 items, collision, or long label)" if use_legend else "inline labels (no trigger met)"
    print(f"Chart written to {output_path}, mode: {mode}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="impact_effort.png")
    args = parser.parse_args()
    generate_chart(WORKFLOWS, args.output)
