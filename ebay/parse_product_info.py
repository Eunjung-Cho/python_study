from bs4 import BeautifulSoup



fileName = "./phone_case_others.html"
def getFileString(file_path):
    with open(file_path, 'rt', encoding='utf-8') as f:
        line = f.read()
        return line

def get_order_info(page_string):
    bsObj = BeautifulSoup(page_string, "html.parser")
    tbody = bsObj.find("tr", {"class":"shreskin-edit-sales-record-buyer-details"}).find("table").find("tbody").find("table").find("tbody")
    trs = tbody.findAll("tr")

    id = trs[0].findAll("td")[1].find("b").text
    email = trs[1].findAll("td")[1].find("b").text
    buyer_full_name = trs[3].findAll("td")[1].find("input")['value']
    street1 = trs[4].findAll("td")[1].find("input")['value']
    street2 = trs[5].findAll("td")[1].find("input")['value']
    city = trs[6].findAll("td")[1].find("input")['value']
    state = trs[7].findAll("td")[1].find("input")['value']
    zip = trs[8].findAll("td")[1].find("input")['value']
    country = trs[9].find("select").find("option", selected=True).text
    phone_number = ""
    if country in ['Canada', 'United States']:
        phone_number_td = trs[10].findAll("td")[1]
        p1 = phone_number_td.find("input", {"name":"dayphone1"})['value']
        p2 = phone_number_td.find("input", {"name":"dayphone2"})['value']
        p3 = phone_number_td.find("input", {"name":"dayphone3"})['value']
        phone_number = "({}){}-{}".format(p1, p2, p3)
    elif country in ['United Kingdom']:
        phone_number_td = trs[10].findAll("td")[1]
        p1 = phone_number_td.find("input", {"name": "dayphone1"})['value']
        p2 = phone_number_td.find("input", {"name": "dayphone2"})['value']
        phone_number = "({}){}".format(p1, p2)
    else:
        phone_number_td = trs[10].findAll("td")[1]
        p1 = phone_number_td.find("input", {"name": "dayphone1"})['value']
        phone_number = p1


    # print(phone_number)

    result = "{},{},{},{},{},{},{},{},{},{}"\
        .format(id, email, buyer_full_name, street1
                , street2, city, state, zip, country,
                phone_number)
    return result



# result = get_order_info(getFileString(fileName))
# print(result)
