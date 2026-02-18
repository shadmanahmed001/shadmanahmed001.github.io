#!/usr/bin/env python3
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USERNAME = "shadman.ahmed.qasmi"
COUNT = 6
URL = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={USERNAME}"

req = urllib.request.Request(
    URL,
    headers={
        "x-ig-app-id": "936619743392459",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123 Safari/537.36",
        "accept": "application/json",
    },
)

with urllib.request.urlopen(req, timeout=20) as r:
    payload = json.load(r)

user = payload["data"]["user"]
edges = user.get("edge_owner_to_timeline_media", {}).get("edges", [])

items = []
for e in edges[:COUNT]:
    n = e.get("node", {})
    shortcode = n.get("shortcode")
    if not shortcode:
        continue
    is_video = bool(n.get("is_video"))
    post_type = "reel" if is_video else "post"
    url = f"https://www.instagram.com/{'reel' if is_video else 'p'}/{shortcode}/"
    items.append(
        {
            "shortcode": shortcode,
            "type": post_type,
            "url": url,
            "thumbnail": n.get("thumbnail_src") or n.get("display_url"),
            "timestamp": n.get("taken_at_timestamp"),
            "caption": ((n.get("edge_media_to_caption", {}).get("edges") or [{}])[0].get("node", {}).get("text", "")[:140]),
        }
    )

out = {
    "username": USERNAME,
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "count": len(items),
    "items": items,
}

out_path = Path("data/instagram-feed.json")
out_path.write_text(json.dumps(out, indent=2))
print(str(out_path))
print(f"items={len(items)}")
