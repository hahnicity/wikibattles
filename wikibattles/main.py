# Point of this file is to create a csv file that we can input into the page rank algorithm
#
import argparse
from getpass import getpass

import MySQLdb


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", type=int, default=3306)
    parser.add_argument("--user", default="root")
    parser.add_argument("--db", required=True)
    parser.add_argument("--page-len", type=int, default=1000)
    return parser


def perform_parsing():
    parser = build_parser()
    args = parser.parse_args()
    password = getpass("Enter your mysql password, just hit enter if there is none: ")
    return args, password


def retrive_data(host, password, user, port, db):
    db = MySQLdb.connect(host=host, passwd=password, user=user, port=port, db=db)
    cursor = db.cursor()
    # eh... I've made things configurable except for the database schema... so it's not really
    # configurable. Oh well unless someone else wants to follow my steps.
    cursor.execute("select page_title,page_to_title from page as t1 inner join battle_links as t2 on t2.pl_from=t1.page_id;")
    return cursor
