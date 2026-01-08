def correlate(accounts):
    matches = []

    for a in accounts:
        for b in accounts:
            if a != b and a.get("username") == b.get("username"):
                matches.append({
                    "username": a.get("username"),
                    "platforms": [a.get("platform"), b.get("platform")]
                })

    return matches
