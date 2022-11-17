import pandas as pd
from pandas import DataFrame as df

times = [
    "2022-11-14 00:13:25",
    "2022-11-14 00:14:24",
    "2022-11-14 00:15:23",
    "2022-11-14 00:19:25",
    "2022-11-14 00:20:25",
    "2022-11-14 00:21:25",
    "2022-11-14 00:22:23",
    "2022-11-14 00:22:26",
    "2022-11-14 00:27:26",
    "2022-11-14 00:23:1",
    "2022-11-14 00:23:4",
    "2022-11-14 00:25:30",
    "2022-11-14 00:27:1",
]
userid = [1, 1, 1, 2, 2, 3, 2, 3, 2, 5, 6, 1, 1]
product_id = [1, 1, 1, 12, 2, 3, 45, 6, 8, 3, 56, 7, 3]
data = {"customer_id": userid, "product_id": product_id, "timestamp": times, }
frame = df(data)


def main():
    frame["timestamp"] = pd.to_datetime(frame["timestamp"])
    format = lambda t: t.diff().gt(pd.Timedelta('3min')).cumsum()
    frame['session_id'] = frame.groupby(['customer_id'], group_keys=False)['timestamp'].apply(format)
    frame['session_id'] = frame.groupby(['customer_id', 'session_id']).ngroup() + 1
    print(frame)


if __name__ == "__main__":
    main()
