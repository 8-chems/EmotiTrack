import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("emotitrack.performance")


def log_performance(metrics: dict, path: str = "metrics/performance.log.csv"):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame([metrics])
    if Path(path).exists():
        df.to_csv(path, mode="a", header=False, index=False)
    else:
        df.to_csv(path, index=False)
    logger.info("Logged performance metrics: %s", metrics)
