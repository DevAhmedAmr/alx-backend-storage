#!/usr/bin/python3
from pymongo import MongoClient

"""Python script that provides some stats
                about Nginx logs stored in MongoDB:"""
if "__main__" == __name__:

    client = MongoClient('mongodb://127.0.0.1:27017')
    # client.get_database("logs").get_collection("nginx")
    client.get_database().get_collection()

    nginx_collection = client.logs.nginx

    all = nginx_collection.find().count()

    get = nginx_collection.count_documents({"method": "GET"})
    post = nginx_collection.count_documents({"method": "POST"})
    put = nginx_collection.count_documents({"method": "PUT"})
    patch = nginx_collection.count_documents({"method": "PATCH"})
    delete = nginx_collection.count_documents({"method": "DELETE"})
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{all} logs")
    print(f"Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{status_check} status check")
