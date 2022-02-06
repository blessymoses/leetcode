"""
Given a list of timestamps in sequential order, 
return a list of lists grouped by week (7 days) using the first timestamp as the starting point.

[
    ['2019-01-01', '2019-01-02'], 
    ['2019-01-08'], 
    ['2019-02-01', '2019-02-02'],
    ['2019-02-05'],
]
"""
from datetime import datetime, timedelta
from typing import List


def weekly_aggregation(timestamps: List[str]) -> List[List[str]]:
    result = []

    # convert to datetime
    timestamps_date = [datetime.strptime(d, "%Y-%m-%d") for d in timestamps]

    start_date = timestamps_date[0]
    end_date = start_date + timedelta(days=7)

    r_week = [timestamps_date.pop(0).strftime("%Y-%m-%d")]

    # check if the date falls in the week
    while timestamps_date:
        if start_date <= timestamps_date[0] < end_date:
            r_week.append(timestamps_date.pop(0).strftime("%Y-%m-%d"))
            continue
        start_date, end_date = end_date, end_date + timedelta(days=7)
        if r_week:
            result.append(r_week)
            r_week = []

    if r_week:
        result.append(r_week)

    return result


ts = [
    "2019-01-01",
    "2019-01-02",
    "2019-01-08",
    "2019-02-01",
    "2019-02-02",
    "2019-02-05",
]

print(*weekly_aggregation(ts), sep="\n")
