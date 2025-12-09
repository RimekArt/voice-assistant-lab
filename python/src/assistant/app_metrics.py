# app_metrics.py
from prometheus_client import start_http_server, Summary, Counter
import time, random

recognize_time = Summary('va_recognize_seconds', 'Time spent in recognize()')
recognize_total = Counter('va_recognize_total', 'Total recognize calls')

@recognize_time.time()
def recognize():
    time.sleep(random.uniform(0.05, 0.20))  # емулюємо роботу
    recognize_total.inc()

if __name__ == '__main__':
    start_http_server(8000)  # <-- /metrics на 8000
    while True:
        recognize()
