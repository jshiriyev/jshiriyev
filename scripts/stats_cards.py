"""Render the profile README's GitHub stats cards as static SVGs.

Run by .github/workflows/stats-cards.yml. Reads public data from the GitHub
GraphQL API and writes profile/stats.svg and profile/top-langs.svg, so the
README does not depend on a third-party image service being up.

Environment:
    GITHUB_TOKEN   token for the GraphQL API (the workflow's token is enough)
    GH_USER        account to report on (default: jshiriyev)
    EXCLUDE_LANGS  comma-separated languages to leave out of the language card
"""

import json
import os
import urllib.request
from html import escape
from pathlib import Path

USER = os.environ.get("GH_USER", "jshiriyev")
EXCLUDE = {s.strip() for s in os.environ.get("EXCLUDE_LANGS", "Jupyter Notebook").split(",") if s.strip()}
OUT = Path(__file__).resolve().parent.parent / "profile"

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
    }
    repositoriesContributedTo(first: 1, contributionTypes: [COMMIT, ISSUE, PULL_REQUEST, REPOSITORY]) { totalCount }
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC) {
      totalCount
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
  }
}
"""

STYLE = """
  <style>
    .bg { fill: #ffffff; stroke: #d0d7de; }
    .title { font: 600 16px 'Segoe UI', Ubuntu, Helvetica, Arial, sans-serif; fill: #1f6feb; }
    .label { font: 400 13px 'Segoe UI', Ubuntu, Helvetica, Arial, sans-serif; fill: #424a53; }
    .value { font: 600 13px 'Segoe UI', Ubuntu, Helvetica, Arial, sans-serif; fill: #1f2328; }
    .track { fill: #eaeef2; }
    @media (prefers-color-scheme: dark) {
      .bg { fill: #0d1117; stroke: #30363d; }
      .title { fill: #58a6ff; }
      .label { fill: #9198a1; }
      .value { fill: #e6edf3; }
      .track { fill: #21262d; }
    }
  </style>
"""


def fetch(token):
    body = json.dumps({"query": QUERY, "variables": {"login": USER}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    if "errors" in payload:
        raise RuntimeError(payload["errors"])
    return payload["data"]["user"]


def card(width, height, title, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">\n'
        f"{STYLE}"
        f'  <rect class="bg" x="0.5" y="0.5" rx="6" width="{width - 1}" height="{height - 1}"/>\n'
        f'  <text class="title" x="20" y="32">{escape(title)}</text>\n'
        f"{body}</svg>\n"
    )


def stats_svg(user):
    contrib = user["contributionsCollection"]
    repos = user["repositories"]
    rows = [
        ("Public repositories", repos["totalCount"]),
        ("Stars earned", sum(r["stargazerCount"] for r in repos["nodes"])),
        ("Commits (last year)", contrib["totalCommitContributions"]),
        ("Pull requests (last year)", contrib["totalPullRequestContributions"]),
        ("Issues (last year)", contrib["totalIssueContributions"]),
        ("Contributed to (last year)", user["repositoriesContributedTo"]["totalCount"]),
    ]
    body = ""
    for i, (label, value) in enumerate(rows):
        y = 62 + i * 25
        body += f'  <text class="label" x="20" y="{y}">{label}</text>\n'
        body += f'  <text class="value" x="330" y="{y}" text-anchor="end">{value:,}</text>\n'
    return card(350, 62 + len(rows) * 25, "GitHub Stats", body)


def langs_svg(user, top=6):
    totals, colors = {}, {}
    for repo in user["repositories"]["nodes"]:
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            if name in EXCLUDE:
                continue
            totals[name] = totals.get(name, 0) + edge["size"]
            colors[name] = edge["node"]["color"] or "#8b949e"
    ranked = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)[:top]
    grand = sum(size for _, size in ranked) or 1

    body, x = "", 20.0
    bar_width = 310
    body += f'  <rect class="track" x="20" y="48" rx="4" width="{bar_width}" height="8"/>\n'
    for name, size in ranked:
        w = bar_width * size / grand
        body += f'  <rect x="{x:.2f}" y="48" width="{w:.2f}" height="8" fill="{colors[name]}"/>\n'
        x += w
    for i, (name, size) in enumerate(ranked):
        col, row = i % 2, i // 2
        cx, cy = 20 + col * 160, 82 + row * 24
        body += f'  <circle cx="{cx + 5}" cy="{cy - 4}" r="5" fill="{colors[name]}"/>\n'
        body += (
            f'  <text class="label" x="{cx + 16}" y="{cy}">{escape(name)} '
            f'<tspan class="value">{100 * size / grand:.1f}%</tspan></text>\n'
        )
    rows = (len(ranked) + 1) // 2
    return card(350, 82 + rows * 24, "Most Used Languages", body)


def main():
    user = fetch(os.environ["GITHUB_TOKEN"])
    OUT.mkdir(exist_ok=True)
    (OUT / "stats.svg").write_text(stats_svg(user), encoding="utf-8")
    (OUT / "top-langs.svg").write_text(langs_svg(user), encoding="utf-8")


if __name__ == "__main__":
    main()
