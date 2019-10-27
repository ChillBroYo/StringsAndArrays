import csv
import json
import datetime
import sys


class InvestInfo:
    def __init__(self):
        self.user_records = {}

    class UserTransaction:
        def __init__(self, date, shares, cash, i_name):
            self.date = datetime.datetime.strptime(date, "%Y-%m-%d")
            self.shares_bought = int(shares)
            self.cash_paid = float(cash)
            self.investor_name = i_name

        def print(self):
            print("Date: {}, Shares: {}, Cash Paid: {}, Name: {}".format(
                self.date, self.shares_bought, self.cash_paid, self.investor_name))

    # Add item to each users index sorted by increasing date
    def add_investment(self, date, shares, cash, i_name):
        new_transact = self.UserTransaction(date, shares, cash, i_name)
        if self.user_records.get(i_name) == None:
            self.user_records[i_name] = [new_transact]
        else:
            added_item = False
            for index in range(len(self.user_records[i_name])):
                if len(self.user_records[i_name]) == 1 and self.user_records[i_name][0].date > new_transact.date:
                    self.user_records[i_name].insert(0, new_transact)
                    added_item = True
                    break
                elif self.user_records[i_name][index].date > new_transact.date and index > 0:
                    self.user_records[i_name].insert(index, new_transact)
                    added_item = True
                    break
            if added_item == False:
                self.user_records[i_name].append(new_transact)

    def load_file(self, csv_filename):
        with open(csv_filename) as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                self.add_investment(row[0], row[1], row[2], row[3])

    def get_investments_by_date(self, date):
        user_date_info = {}
        ownership_list = []
        total_shares = 0
        total_cash = 0.00
        if date == None:
            date = datetime.datetime.now()
        else:
            date = datetime.datetime.strptime(date, "%Y-%m-%d")

        # Get cash and shares
        for user in self.user_records:
            user_shares = 0
            user_cash = 0.00
            for index in range(len(self.user_records[user])):
                if self.user_records[user][index].date <= date:
                    user_shares += self.user_records[user][index].shares_bought
                    user_cash += self.user_records[user][index].cash_paid
                else:
                    # Since its in order, if theres a greater date, escape
                    break

            user_date_info[user] = [user_shares, user_cash]
            total_shares += user_shares
            total_cash += user_cash

        # Get ownership
        for user in user_date_info:
            # If the user has at least one share add it to the return set
            if user_date_info[user][0] > 0:
                user_date_info[user].append("{:.2f}".format(round(user_date_info[user][0]/total_shares * 100, 2)))
                ownership_list.append({"investor": user, "shares": user_date_info[user][0], "cash_paid": "{:.2f}".format(user_date_info[user][1]), "ownership": user_date_info[user][2]})

        return_json = {}
        return_json["date"] = date.strftime("%m/%d/%Y")
        return_json["cash_raised"] = "{:.2f}".format(total_cash)
        return_json["total_number_of_shares"] = total_shares
        return_json["ownership"] = ownership_list
        return return_json


if __name__ == "__main__":
    if len(sys.argv) == 2 or len(sys.argv) == 3:
        cap_table = InvestInfo()
        cap_table.load_file(sys.argv[1])
        date = None
        if len(sys.argv) == 3:
            date = sys.argv[2]
        date_cap_table = cap_table.get_investments_by_date(date)
        print(json.dumps(date_cap_table))
    else:
        print("usage: csv_to_captable.py input_file [date]")
