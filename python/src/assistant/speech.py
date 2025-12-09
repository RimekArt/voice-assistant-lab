from __future__ import annotations
from pathlib import Path
import time

def recognize(wav_path: str | Path) -> str:
    """sound."""
    _ = Path(wav_path).read_bytes()  # імітація роботи з файлом
    time.sleep(0.01)                  # ~10 мс “навантаження”
    return "OK"

