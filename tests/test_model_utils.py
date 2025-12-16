import sys
from pathlib import Path

# 프로젝트 루트(final-group20)를 Python 경로에 추가
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.model_utils import rmse

import numpy as np

def test_rmse_zero_error():
    y = np.array([1, 2, 3])
    assert rmse(y, y) == 0.0
