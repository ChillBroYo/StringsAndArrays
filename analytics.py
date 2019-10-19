# Suppose you have time-series data consisting of (timestamp, user_id, country_id, site_id).
# Each entry (row) is created when a user (of user_id) from some country (country_id) visited a
# certain website (site_id) at a certain time (timestamp).

# For instance, in row 2 you will see the following row:
# "2019-02-01 00:01:24	LC36FC	TL6	N0OTG"
# This tells us that at "2019-02-01 00:01:24" user "LC36FC" from country "TL6" visited website "N0OTG".

# The sheet contains 3554 rows (including the header) and four columns (ts for timestamp, user_id, country_id, site_id).

from datetime import datetime
class TrafficLog:
    def __init__(self):
        # site_id (or whatever) => ts,user_id,country_id,site_id
        self.site_id_map = {}
        self.ts_map = {} # unused but left in for potential future calculations
        self.user_id_map = {}
        self.country_id_map = {}
    
    class LogLine:
        def __init__(self, ts, user_id, country_id, site_id):
            self.ts = ts
            self.user_id = user_id
            self.country_id = country_id
            self.site_id = site_id

    # Fills each map with starting key according to its name for each specific access to things by a value
    def load_and_process(self, filename):
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                values = line.split("\t")
                ts = datetime.strptime(values[0], "%Y-%m-%d %H:%M:%S")
                user_id = values[1]
                country_id = values[2]
                site_id = values[3]
                
                new_record = self.LogLine(ts, user_id, country_id, site_id)
                if self.site_id_map.get(site_id) == None:
                    self.site_id_map[site_id] = [new_record]
                else:
                    self.site_id_map[site_id].append(new_record)
                if self.ts_map.get(ts) == None:
                    self.ts_map[ts] = [new_record]
                else:
                    self.ts_map[ts].append(new_record)
                if self.user_id_map.get(user_id) == None:
                    self.user_id_map[user_id] = [new_record]
                else:
                    self.user_id_map[user_id].append(new_record)
                if self.country_id_map.get(country_id) == None:
                    self.country_id_map[country_id] = [new_record]
                else:
                    self.country_id_map[country_id].append(new_record)

    # Goes through each log in the specified country code and gets uuids for each site id
    def get_uuids_siteid_by_country(self, country_id):
        site_id_uuid = {}
        most_uuid_site_id = [self.country_id_map[country_id][0].site_id, 1]
        for log in self.country_id_map[country_id]:
            if site_id_uuid.get(log.site_id) == None:
                site_id_uuid[log.site_id] = [log.user_id]
            else:
                if log.user_id in site_id_uuid[log.site_id]:
                    continue
                site_id_uuid[log.site_id].append(log.user_id)
                if len(site_id_uuid[log.site_id]) > most_uuid_site_id[1]:
                    most_uuid_site_id[0] = log.site_id
                    most_uuid_site_id[1] = len(site_id_uuid[log.site_id])

        return most_uuid_site_id
    
    # Collects each user_id that visited a site with in the time boundries and then counts each one
    def find_users_by_ts_and_site_visits(self, ts_start, ts_end, min_num_visits):
        which_users_by_site = {}
        for sid in self.site_id_map:
            for log in self.site_id_map[sid]:
                if log.ts > ts_start and log.ts < ts_end:
                    if which_users_by_site.get(sid) == None:
                        which_users_by_site[sid] = [log.user_id]
                    else:
                        which_users_by_site[sid].append(log.user_id)
        
        users_visited_more = []
        for sid in which_users_by_site:
            count_check = {}
            for uid in which_users_by_site[sid]:
                if count_check.get(uid) == None:
                    count_check[uid] = 1
                else:
                    count_check[uid] += 1
            for uid in count_check:
                if count_check[uid] > min_num_visits:
                    users_visited_more.append([uid, sid, count_check[uid]])

        return users_visited_more

    # Collects every sites last visits from users and then pumps the top into a map, removing the previous max each time
    def get_top_by_last_vist_uuids(self, top_count):
        last_visit_sites = {}
        for uid in self.user_id_map:
            last_index = len(self.user_id_map[uid]) - 1
            last_record = self.user_id_map[uid][last_index]
            if last_visit_sites.get(last_record.site_id) == None:
                last_visit_sites[last_record.site_id] = [last_record.user_id]
            else:
                if last_record.user_id in last_visit_sites[last_record.site_id]:
                    continue
                last_visit_sites[last_record.site_id].append(last_record.user_id)

        top3_by_id = {}
        for _ in range(top_count): 
            current_largest_item = ["", 0]
            for item in last_visit_sites:
                if len(last_visit_sites[item]) > current_largest_item[1]:
                    current_largest_item[0] = item
                    current_largest_item[1] = len(last_visit_sites[item])
            # in case requested more than exists
            if current_largest_item == ["", 0]:
                break
            top3_by_id[current_largest_item[0]] = current_largest_item[1]
            last_visit_sites[current_largest_item[0]] = []
            current_largest_item = ["", 0]

        return top3_by_id
    
    # Gets the earliest and oldest ts log entry for users and then merges those records' site_ids into a map
    def get_first_and_last_visit_for_users(self):
        users_first_last = {}
        for uid in self.user_id_map:
            first_access = ["", datetime.max, -1]
            last_access =  ["", datetime.min, -1]
            for index in range(len(self.user_id_map[uid])):
                log = self.user_id_map[uid][index]
                if log.ts < first_access[1]:
                    first_access[0] = log.site_id
                    first_access[1] = log.ts
                    first_access[2] = index
            for index in range(len(self.user_id_map[uid])):
                log = self.user_id_map[uid][index]
                if log.ts > last_access[1] and index != first_access[2]:
                    last_access[0] = log.site_id
                    last_access[1] = log.ts
                    last_access[2] = index
            # only one entry
            if last_access[0] == "":
                last_access = first_access
            users_first_last[uid] = [first_access[0], last_access[0]]

        return users_first_last



if __name__ == "__main__":
    processor = TrafficLog()
    processor.load_and_process("copy and pasted db in a text file")

    # Consider only the rows with country_id = "BDV" (there are 844 such rows). For each site_id, we
    # can compute the number of unique user_id's found in these 844 rows. Which site_id has the largest
    # number of unique users? And what's the number?
    print("Sites with the most unique users by country id")
    print("--------------------------------")
    val = processor.get_uuids_siteid_by_country("BDV")
    print("Site_id of the site with the greatest number of uuids in country code BDV: {} \nCount of uuids from site with greatest number of uuids in country code BDV: {}".format(val[0], val[1]))

    # Between 2019-02-03 00:00:00 and 2019-02-04 23:59:59, there are four users who
    # visited a certain site more than 10 times. Find these four users & which sites
    # they (each) visited more than 10 times.
    # (Simply provides four triples in the form (user_id, site_id,
    # number of visits) in the box below.)
    print("\n4 users [uid, sid, visits] for the specified time")
    print("--------------------------------")
    val = processor.find_users_by_ts_and_site_visits(datetime.strptime("2019-02-03 00:00:00", "%Y-%m-%d %H:%M:%S"),
        datetime.strptime("2019-02-04 23:59:59", "%Y-%m-%d %H:%M:%S"), 10)
    for record in val:
        print("user_id: {},  site_id: {}, visits: {}".format(record[0], record[1], record[2]))
        
    # For each site, compute the unique number of users whose last visit (found in the
    # original data set) was to that site. For instance, user "LC3561"'s last visit is
    # to "N0OTG" based on timestamp data. Based on this measure, what are top three sites?
    # (hint: site "3POLC" is ranked at 5th with 28 users whose last visit in the data
    # set was to 3POLC; simply provide three pairs in the form (site_id, number of users).)
    print("\nTop three sites by last visited")
    print("--------------------------------")
    val = processor.get_top_by_last_vist_uuids(3)
    for site_id in val:
        print("site_id: {}, num_last_visited_uuids: {}".format(site_id, val[site_id]))

    # For each user, determine the first site he/she visited and the last site he/she
    # visited based on the timestamp data. Compute the number of users whose first/last
    # visits are to the same website. What is the number?
    print("\nUsers who visited the same site for their first and last visit")
    print("--------------------------------")
    val = processor.get_first_and_last_visit_for_users()
    count_fls = 0
    for uid in val:
        if val[uid][0] == val[uid][1]:
            count_fls += 1
    print("Number of users with the same first and last visit are: {}".format(count_fls))
