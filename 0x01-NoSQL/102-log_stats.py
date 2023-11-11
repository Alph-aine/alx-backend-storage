#!/usr/bin/env python3
''' print stats about nginx from mongodb and also top ips'''


from pymongo import MongoClient


def print_logs_stats(collection):
    '''prints the logs'''
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents(
            {"method": "GET", "path": "/status"}
            )
    print(f"{status_check} status check")

    top_ips = collection.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    print("IPs:")
    for top_ip in top_ips:
        ip = top_ip.get("ip")
        count = top_ip.get("count")
        print(f'\t{ip}: {count}')


def main():
    '''runs the fucntion'''
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    print_logs_stats(collection)


if __name__ == "__main__":
    main()
