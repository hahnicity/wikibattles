# Point of this file is to create a csv file that we can input into the page rank algorithm
#
import csv

from wikibattles.main import perform_parsing, retrive_data


def main():
    args, password = perform_parsing()
    cursor = retrive_data(args.host, password, args.user, args.port, args.db)
    with open('battlelinks.csv', 'w') as file_:
        writer = csv.writer(file_)
        results = cursor.fetchmany(args.page_len)
        while results:
            results = cursor.fetchmany(args.page_len)
            for result in results:
                writer.writerow([result[0], 0, result[1], 1])


if __name__ == "__main__":
    main()
