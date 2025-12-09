def route_command(text: str) -> str:
    t = (text or "").strip().lower()
    if not t:
        return "empty"
    if any(k in t for k in ("call", "dial", "зател", "пов")):
        return "phone"
    if any(k in t for k in ("music", "play", "муз")):
        return "audio"
    if any(k in t for k in ("navigate", "марш", "route", "nav")):
        return "nav"
    return "unknown"
