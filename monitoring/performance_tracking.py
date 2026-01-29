import pandas as pd
import logging

def log_performance(metrics: dict):
    logging.basicConfig(filename='performance.log', level=logging.INFO)
    logging.info(f"Performance metrics: {metrics}")

if __name__ == "__main__":
    # Example metrics
    metrics = {
        'accuracy': 0.95,
        'f1_score': 0.92,
        'precision': 0.93,
        'recall': 0.91
    }
    log_performance(metrics)
