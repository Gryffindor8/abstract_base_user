import requests
from bs4 import BeautifulSoup
import json


# from urlss import urls


def get_data(soup_obj, tags):
    try:
        obj = soup_obj.find(lambda t: t.name == 'td' and tags in t.text).parent
        if tags == "Mailing Address:":
            obj = str(obj).replace("<br/>", " #N ")
            obj1 = BeautifulSoup(obj, "html.parser")
            return obj1.text
        return obj.text

    except:
        obj = ''
    return obj


urls = ["https://www2.dre.ca.gov/publicasp/pplinfo.asp?License_id=01759756",
        "https://www2.dre.ca.gov/publicasp/pplinfo.asp?License_id=02124511",
        "https://www2.dre.ca.gov/publicasp/pplinfo.asp?License_id=02186081",
        "https://www2.dre.ca.gov/publicasp/pplinfo.asp?License_id=02132541"]
# urls = urls.split()
# urls = urls[1500:2000]
all_data = []
retry = 0
failed = []

for num, url in enumerate(urls):
    if not url:
        continue
    while True:
        try:
            data_dict = {}
            html_doc = requests.get(url).content
            soup = BeautifulSoup(html_doc, 'html.parser')
            name_tag = 'Name:'
            address_tag = 'Mailing Address:'
            broker_tag = 'Former Responsible Broker:'
            license_tag = 'License ID'
            expiry_tag = 'Expiration Date:'

            data_dict["url"] = url
            data_dict["name"] = get_data(soup, name_tag)
            data_dict["address"] = get_data(soup, address_tag)
            data_dict["license"] = get_data(soup, license_tag)
            data_dict["expiry"] = get_data(soup, expiry_tag)

            tag = soup.find(lambda t: t.name == 'td' and name_tag in t.text).parent
            nexts = tag.find_all_next("td")
            brokers = []

            for k in nexts:
                if "License ID:" in k.text:
                    try:
                        brokers.append(k.find("font").text)
                    except:
                        pass
            data_dict["brokers"] = brokers
            all_data.append(data_dict)
            json_object = json.dumps(all_data)

            with open("result.json", "w") as outfile:
                outfile.write(json_object)
            print(num)
            retry = 0
            break
        except Exception as e:
            print(e)
            retry = retry + 1
            if retry == 4:
                retry = 0
                print(url)
                failed.append(url)
                fl = {"failed": failed}
                json_object1 = json.dumps(fl)
                with open("failed.json", "w") as outfile:
                    outfile.write(json_object1)
                break
