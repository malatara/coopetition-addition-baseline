#!/usr/bin/env python
""" demo of a simple coopetition solution """
import os
import sys
import pandas as pd

def predict(data):
    """ get two colums from `df` and returns the predicted ouput as a column (pd.Series)
    TODO: modify it
    """
    result = data['col1'] + data['col2']
    return result


def main(input_dir, output_dir):
    """ main procedure """
    df = pd.read_csv(os.path.join(input_dir, 'data.tsv'), sep='\t')

    predicted_result = predict(df)
    assert isinstance(predicted_result, pd.core.series.Series), \
        f"Invalid predicted output type {type(predicted_result)}"

    predicted_result.to_csv(
        os.path.join(output_dir, 'data.predict'),
        index=False,
        header=False)


if __name__ == "__main__":
    assert len(sys.argv) >= 3, f"Invalid number of arguments: {len(sys.argv)}"
    main(sys.argv[1], sys.argv[2])
