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
        self.ts_map = {}
        self.user_id_map = {}
        self.country_id_map = {}
    
    class LogLine:
        def __init__(self, ts, user_id, country_id, site_id):
            self.ts = ts
            self.user_id = user_id
            self.country_id = country_id
            self.site_id = site_id

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
    
    def find_users_by_ts_and_site_visits(self, ts_start, ts_end, min_num_visits):
        site_id_to_user_id_to_visits = {}
        for ts in self.ts_map:
            if ts > ts_start and ts < ts_end:
                for uid in range(len(self.ts_map[ts])):
                    if site_id_to_user_id_to_visits.get(self.ts_map[ts][uid].site_id) == None:
                        site_id_to_user_id_to_visits[self.ts_map[ts][uid].site_id] = {self.ts_map[ts][uid].user_id: 1}
                    elif site_id_to_user_id_to_visits.get(self.ts_map[ts][uid].site_id) != None and self.ts_map[ts][uid].user_id not in site_id_to_user_id_to_visits[self.ts_map[ts][uid].site_id]:
                        site_id_to_user_id_to_visits[self.ts_map[ts][uid].site_id] = {self.ts_map[ts][uid].user_id: 1}
                    else:
                        site_id_to_user_id_to_visits[self.ts_map[ts][uid].site_id][self.ts_map[ts][uid].user_id] += 1

        users_visited_more = []
        for i in site_id_to_user_id_to_visits:
            for x in site_id_to_user_id_to_visits[i]:
                if site_id_to_user_id_to_visits[i][x] > min_num_visits:
                    users_visited_more.append([i, site_id_to_user_id_to_visits[i], site_id_to_user_id_to_visits[i][x]])
        
        print(users_visited_more)


        return {}

    def get_topthree_by_last_vist_uuids(self):
        return {}
    
    def get_first_and_last_visit_for_users(self):
        return {}



if __name__ == "__main__":
    processor = TrafficLog()
    processor.load_and_process("/Users/Samson/Documents/projects/Strings_and_Arrays/sample_db.txt")

    # Consider only the rows with country_id = "BDV" (there are 844 such rows). For each site_id, we
    # can compute the number of unique user_id's found in these 844 rows. Which site_id has the largest
    # number of unique users? And what's the number?
    val = processor.get_uuids_siteid_by_country("BDV")
    print("Site_id of the site with the greatest number of uuids in country code BDV: {} \nCount of uuids from site with greatest number of uuids in country code BDV: {}".format(val[0], val[1]))

    # Between 2019-02-03 00:00:00 and 2019-02-04 23:59:59, there are four users who
    # visited a certain site more than 10 times. Find these four users & which sites
    # they (each) visited more than 10 times.
    # (Simply provides four triples in the form (user_id, site_id,
    # number of visits) in the box below.)
    val = processor.find_users_by_ts_and_site_visits(datetime.strptime("2019-02-03 00:00:00", "%Y-%m-%d %H:%M:%S"),
        datetime.strptime("2019-02-04 23:59:59", "%Y-%m-%d %H:%M:%S"), 10)
    for uid in val:
        print("user_id: {},  site_id: {}, visits: {}".format(val[uid].uid, val[uid].sid, val[uid].visits))
    exit(0)
    # For each site, compute the unique number of users whose last visit (found in the
    # original data set) was to that site. For instance, user "LC3561"'s last visit is
    # to "N0OTG" based on timestamp data. Based on this measure, what are top three sites?
    # (hint: site "3POLC" is ranked at 5th with 28 users whose last visit in the data
    # set was to 3POLC; simply provide three pairs in the form (site_id, number of users).)
    val = processor.get_topthree_by_last_vist_uuids()
    for site_id in val:
        print("site_id: {}, num_last_visited_uuids: {}".format(site_id, val[site_id]))

    # For each user, determine the first site he/she visited and the last site he/she
    # visited based on the timestamp data. Compute the number of users whose first/last
    # visits are to the same website. What is the number?
    val = processor.get_first_and_last_visit_for_users()
    count_fls = 0
    for uid in val:
        if val[uid].first_visit == val[uid].last_visit:
            count_fls += 1
    print("Number of users with the same first and last visit are: {}", count_fls)
