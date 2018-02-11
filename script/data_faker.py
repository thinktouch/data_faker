import sys

import pymongo
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from faker import Faker
from pymongo import MongoClient

es = Elasticsearch(hosts=["10.10.13.51"], http_auth=('elastic', 'S2Lylw_072nyLQxH@c3C'), port=9200)
fake = Faker("zh_CN")

db_name = "es_mongodb_pk"
collection_name = "pk_pk"

connect = MongoClient("10.10.13.51", 27017)
db = connect[db_name]
collection = db[collection_name]
collection.create_index([("paragraph", pymongo.TEXT), ("mac_address", pymongo.TEXT)])
collection.create_index("name", unique=False)
collection.create_index("phone_number", unique=False)
collection.create_index("ip", unique=False)


def write_mongodb(data):
    collection.insert(data)


def write_es(data):
    actions = [
        {
            "_index": db_name,
            "_type": collection_name,
            "_source": source
        }
        for source in data
    ]
    helpers.bulk(es, actions=actions)


def data_generate():
    name = fake.name()
    job = fake.job()
    phone_number = fake.phone_number()
    internet_explorer = fake.internet_explorer()
    url = fake.url()
    address = fake.address()
    mac_address = fake.mac_address()
    ip = fake.ipv4(network=False)
    paragraph = fake.paragraph(nb_sentences=5, variable_nb_sentences=True, ext_word_list=None)
    date = fake.iso8601(tzinfo=None, end_datetime=None)

    data = {"name": name, "job": job, "phone_number": phone_number, "internet_explorer": internet_explorer,
            "url": url, "address": address, "mac_address": mac_address, "ip": ip, "paragraph": paragraph, "date": date}

    return data


def writer():
    print("====== generate start ======")
    loop_start = 1
    loop_end = 10001
    batch_size = 100
    loop_total = loop_end - loop_start
    base_num = loop_total / batch_size
    for j in range(loop_start, loop_end):
        json = []
        for i in range(batch_size):
            json.append(data_generate())
        write_es(json)
        write_mongodb(json)
        sys.stdout.write("\r")
        sys.stdout.write("%s%% |%s| %s/%s" % (int(j / base_num % 101), int(j / base_num % 101) * '#', loop_total * batch_size, j * batch_size))
        sys.stdout.flush()
    print("\n====== generate end ======")


if __name__ == "__main__":
    writer()
