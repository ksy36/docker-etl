import argparse
import pandas as pd

from datetime import date, timedelta
from collections import namedtuple

from data_validation import retrieve_data_validation_metrics, record_validation_results

parser = argparse.ArgumentParser(
    description="Validate Recent Search Input Against Historical Norms",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "--data_validation_origin", help="Origin table for data validation metrics"
)
parser.add_argument(
    "--data_validation_reporting_destination",
    help="Table to store data validation metric test results",
)
args = parser.parse_args()

validation_df = retrieve_data_validation_metrics(args.data_validation_origin)

record_validation_results(validation_df, args.data_validation_reporting_destination)