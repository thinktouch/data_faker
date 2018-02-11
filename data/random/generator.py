from faker import Faker

fake = Faker("zh_CN")


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
