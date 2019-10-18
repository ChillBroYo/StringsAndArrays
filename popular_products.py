# You are given a text file where each line contains a JSON message as string, containing three fields:
# user_id (string), product_id (string), and quantity (integer). You can assume that each line is a valid JSON message. 

# For instance, a text file may contain the following three lines:
# {"user_id" : "uid_1", "product_id" : "pid_1", "quantity" : 45}
# {"user_id" : "uid_1", "product_id" : "pid_2", "quantity" : 1}
# {"user_id" : "uid_2", "product_id" : "pid_2", "quantity" : 5}

# Given this as input (assume that it is a text file stored in your local machine),
# write a program that reads the file, and computes the most popular products based on two ranking methods.

# (1) Based on the unique number of users who purchased each product, and
# (2) Based on the total quantity of each product sold.

# For instance, using the above example with 3 data points, the most popular product based on ranking method #1 is "pid_2"
# because it was purchased by two different users (where as "pid_1" was purchased only by one user).
# On the other hand, using ranking method #2, "pid_1" is the winner as 45 units of "pid_1" was sold
# whereas only 1+5=6 units of "pid_2" was sold.

# In case of ties, your program must output the product ids that are tied.
# The output can be simply printed to the console in a human-readable manner. 
# Refer to the sample output message below.

# Sample Output:
# Most popular product(s) based on the number of purchasers: [ "pid_2" ]
# Most popular product(s) based on the quantity of goods sold: [ "pid_1" ]

# Constraints:
# You can assume that the input file is fairly small in size (less than 1M lines).
# user_id and product_id are both strings of length at most 10.
# quantity is a positive integer between 1 and 100.
# Each line is a valid JSON message and always contains three elements (user_id, product_id, and quantity).
import json
class Popular_Products_Processor:
    def __init__(self):
        self.product_listing = dict()
        self.highest_uuid_count = -1
        self.highest_quantity = -1

    class Product:
        def __init__(self, pid):
            self.pid = pid
            self.quantity = 0
            self.uuids = []
        
        def flatten_check(self):
            return "pid: {}, quantity: {}, uuid_count: {}".format(self.pid, self.quantity, len(self.uuids))

    def load_and_process(self, filename):
        with open(filename) as f:
            content = f.readlines()
            for line in content:
                json_line = json.loads(line)
                pid    = json_line["product_id"]
                uid    = json_line["user_id"]
                amount = json_line["quantity"]
                if self.product_listing.get(pid) != None:
                    self.product_listing[pid].quantity += amount
                    if self.highest_quantity < self.product_listing[pid].quantity:
                        self.highest_quantity = self.product_listing[pid].quantity
                    if uid in self.product_listing[pid].uuids:
                        continue
                    self.product_listing[pid].uuids.append(uid)
                    if self.highest_uuid_count < len(self.product_listing[pid].uuids):
                        self.highest_uuid_count = len(self.product_listing[pid].uuids)
                else:
                    new_product = self.Product(pid)
                    new_product.quantity = amount
                    new_product.uuids = [uid]
                    self.product_listing[pid] = new_product
                    if self.highest_quantity < amount:
                        self.highest_quantity = amount
                    if self.highest_uuid_count < 1:
                        self.highest_uuid_count = 1

    # O(n) traversal for get
    def get_popular_products(self):
        popular_by_quantity = []
        popular_by_uuid = []

        for pid in self.product_listing:
            if len(self.product_listing[pid].uuids) == self.highest_uuid_count:
                popular_by_uuid.append(pid)
            if self.product_listing[pid].quantity == self.highest_quantity:
                popular_by_quantity.append(pid)
        
        return [popular_by_uuid, popular_by_quantity]


# Most popular product(s) based on the number of purchasers: [ "pid_2" ]
# Most popular product(s) based on the quantity of goods sold: [ "pid_1" ]
if __name__ == "__main__":
    processor = Popular_Products_Processor()
    processor.load_and_process("/Users/Samson/Documents/projects/Strings_and_Arrays/sample_json_large.txt")
    val = processor.get_popular_products()
    for key in processor.product_listing:
        print(processor.product_listing[key].flatten_check())
    print(processor.highest_uuid_count)
    print(processor.highest_quantity)
    print("Most popular product(s) based on the number of purchasers: {}".format(val[0]))
    print("Most popular product(s) based on the quantity of goods sold: {}".format(val[1]))
