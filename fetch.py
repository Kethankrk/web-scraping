
from requests_html import HTMLSession
import re

amazon = HTMLSession().get("https://www.amazon.in/s?k=pocox3")
# # flipkart = HTMLSession().get("http://results.uoc.ac.in/")
# # alibaba = HTMLSession().get("http://results.uoc.ac.in/")
# # snapdeal = HTMLSession().get("http://results.uoc.ac.in/")
# # indiamart = HTMLSession().get("http://results.uoc.ac.in/")

amazon.html.render(sleep=1, keep_page=True, scrolldown=1)
# # flipkart.html.render(sleep=1, keep_page=True, scrolldown=1)
# # alibaba.html.render(sleep=1, keep_page=True, scrolldown=1)
# # snapdeal.html.render(sleep=1, keep_page=True, scrolldown=1)
# # indiamart.html.render(sleep=1, keep_page=True, scrolldown=1)

amazon_data = amazon.html.find(".s-card-container")
# # flipkart_data = flipkart.html.find("")
# # alibaba_data = alibaba.html.find("")
# # snapdeal_data = snapdeal.html.find("")
# # indiamart_data = indiamart.html.find("")

# az_list = []

# for item in amazon_data:
#     az_list.append(item.text)

# print(az_list)

# inp = input("Enter a product name: ")

def checking(word):
    inp = "poco x3"
    final = re.findall(r"[\w']+", word[2].text)
    lowerd = ""

    for i in final:
        lowerd += f"{i.lower()} "

    if inp in lowerd:
        p="true"
    else:
        p="false"

    if p == "true":
        print("ture")
    else:
        print("false")

# checking(amazon_data)


# checking the lest amount


def element_with_least_amount():

    LS_data = amazon.html.find(".a-price-whole")

    LS_list = []
    for items in LS_data:
        LS_list.append(items.text)

    LS_list.sort()
    LS_amount = LS_list[0]

    print(f"The least amount: {LS_amount}")

    for i in amazon_data:
        lol = i.find(".a-price-whole")
        for y in lol:
            if y.text == LS_amount:
                print(f"The least amount element: {i.text}")


element_with_least_amount()

