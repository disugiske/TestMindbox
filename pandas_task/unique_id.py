import pandas as pd
from datetime import datetime

filename = 'frame_result.csv'
chunksize = 15000


def format_frame():
    date_parse_func = lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
    frame = pd.read_csv('test_data.csv',
                        dtype={'customer_id': pd.Int32Dtype(),
                               'product_id': pd.Int32Dtype(),
                               },
                        chunksize=chunksize,
                        parse_dates=['timestamp'],
                        date_parser=date_parse_func,
                        )
    return frame


def main():
    for frame in format_frame():
        delta = lambda t: t.diff().gt(pd.Timedelta('3min')).cumsum()
        frame['session_id'] = frame.groupby(['customer_id'], group_keys=False)['timestamp'].apply(delta).astype(
            'uint32')
        frame['session_id'] = frame.groupby(['customer_id', 'session_id']).ngroup().astype('uint32') + 1

    frame.to_csv(filename, encoding='utf-8')


if __name__ == "__main__":
    main()
