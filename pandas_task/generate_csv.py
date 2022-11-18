import csv
from faker import Faker

fake = Faker()

n_rows = 200000
max_customer_id = 10
min_value = 1
start_date = '-20m'


def main():
    with open('test_data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['customer_id', 'product_id', 'timestamp'])
        for _ in range(n_rows):
            writer.writerow(
                [
                    fake.pyint(min_value=min_value, max_value=max_customer_id),
                    fake.pyint(min_value=min_value),
                    fake.date_time_between(start_date=start_date)
                ]
            )


if __name__ == "__main__":
    main()
