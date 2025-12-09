from __future__ import annotations
from pathlib import Path
from time import perf_counter
import sys, csv
from filelock import FileLock
import pytest
from assistant.speech import recognize

# щоб "from assistant.speech import recognize" працювало
ROOT = Path(__file__).resolve().parents[1] / "src"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

CSV_PATH = Path("reports/times.csv")
CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
LOCK = FileLock(str(CSV_PATH) + ".lock")

@pytest.fixture(scope="session", autouse=True)
def _init_csv():
    with LOCK:
        fresh = not CSV_PATH.exists()
        with CSV_PATH.open("a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if fresh:
                w.writerow(["worker", "file", "elapsed_ms", "result"])

@pytest.fixture
def timer():
    t0 = perf_counter()
    yield lambda: (perf_counter() - t0) * 1000.0  # ms
