from pathlib import Path

import pandas as pd
from model.predict import make_prediction

sample_input_path = Path(__file__).resolve().with_name("bankchurn_test.csv")
sample_input_data = pd.read_csv(sample_input_path)
result = make_prediction(input_data=sample_input_data)
print(result)
