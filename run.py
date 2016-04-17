import argparse
import random
from datetime import datetime, timedelta
from math import log
import os
from time import sleep

from sqlalchemy import create_engine
from sqlalchemy.sql import text


DSN = None

parser = argparse.ArgumentParser(
    description='AlarStudios test task 2. Test data generates for current date as start point')
parser.add_argument('min_date')
parser.add_argument('max_date')
args = parser.parse_args()

min_date, max_date = args.min_date, args.max_date

engine = create_engine(DSN, convert_unicode=True)
connection = engine.connect()

connection.execute(open(os.path.dirname(os.path.dirname(__file__)) + 'init.sql', 'r').read())

min_id, max_id = list(connection.execute("SELECT MIN(id), MAX(id) FROM task"))[0]
max_date = (datetime.strptime(max_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")


def get_id_with_bt(ts, min_id, max_id, direction="min"):
    max_iteration_number = int(log(max_id - min_id + 1, 2)) + 1

    for _ in xrange(max_iteration_number):
        middle = (max_id - min_id) / 2 + min_id

        sql = """SELECT "timestamp" FROM task WHERE id = :middle AND "timestamp" >= :ts"""
        is_grater = len(list(connection.execute(text(sql), middle=middle, ts=ts))) == 1

        if is_grater:
            max_id = middle
        else:
            min_id = middle

    return max_id if direction == "min" else min_id


min_id = get_id_with_bt(min_date, min_id, max_id, direction="min")
max_id = get_id_with_bt(max_date, min_id, max_id, direction="max")

for i in xrange(min_id, max_id + 1, 100):
    connection.execute(text("""DELETE FROM task WHERE id BETWEEN :min AND :max AND
                               "timestamp" >= :min_date AND "timestamp" < :max_date"""),
                       min=i, max=(i + 99), min_date=min_date, max_date=max_date)
    sleep(0.1 + random.random() * 0.2)

connection.close()
