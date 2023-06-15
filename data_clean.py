import json

f = open("result2.json", 'r')
datas = json.load(f)

for count1, data in enumerate(datas):
    address = data.get("address", '')
    if address.strip():
        address_split = address.split("#N")
        address_split = [k for k in address_split if k.strip()]
        # data["address"] = address_split
        for count2, addr in enumerate(address_split):
            key = "address_" + str(count2 + 1)
            data[key] = addr
        # main_address = address_split[0]
        # ad = (address_split[1].strip().split())
        # state = (ad[0])
        # postal = (ad[1])
        # data["postal"] = postal
        # data["state"] = state

    for count, brok in enumerate(data.get("brokers", [])):
        if not brok.strip():
            continue
        key = "Responsible_broker" + str(count)
        broker = brok.strip().split(' ', 1)
        broker_license = broker[0]
        addresses = broker[1].split(",")
        broker_address = addresses[0]
        # b_state, b_postal = addresses[-1].strip().split()
        # data[key + "address"] = broker_address
        data[key + "_address"] = broker[1]
        data[key + "_license"] = broker_license
        # data[key + "state"] = b_state
        # data[key + "postal"] = b_postal
    del datas[count1]["brokers"]

# print(datas)
json_object1 = json.dumps(datas)
with open("final.json", "w") as outfile:
    outfile.write(json_object1)
