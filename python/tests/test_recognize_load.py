import csv, os, time
from pathlib import Path
from filelock import FileLock
import pytest

# імпорт твоєї функції
from assistant.speech import recognize

AUDIO_DIR = Path(__file__).parent / "assets" / "audio"
CSV_PATH  = Path(__file__).parent / "recognize_timings.csv"
REPEATS   = 100   # навантаження: 100 запусків (помножиться на кількість файлів)

# зберемо набір шляхів до аудіо-файлів і повторимо
AUDIO_FILES = sorted([p for p in AUDIO_DIR.glob("*.*") if p.is_file()])
PARAMS = [str(p) for p in AUDIO_FILES] * REPEATS

@pytest.mark.parametrize("audio_path", PARAMS)
def test_recognize_perf(audio_path):
    t0 = time.perf_counter()
    _ = recognize(audio_path)   # тут викликається твоя логіка розпізнавання
    dt = (time.perf_counter() - t0) * 1000.0  # мс

    # потокобезпечно дописуємо результат
    lock = FileLock(str(CSV_PATH) + ".lock")
    with lock:
        new_file = not CSV_PATH.exists()
        with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if new_file:
                w.writerow(["ts", "file", "elapsed_ms"])
            w.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), os.path.basename(audio_path), f"{dt:.2f}"])
