
from requests_html import HTMLSession

amazon = HTMLSession().get("https://www.amazon.in/s?k=pocox3")
# flipkart = HTMLSession().get("http://results.uoc.ac.in/")
# alibaba = HTMLSession().get("http://results.uoc.ac.in/")
# snapdeal = HTMLSession().get("http://results.uoc.ac.in/")
# indiamart = HTMLSession().get("http://results.uoc.ac.in/")

amazon.html.render(sleep=1, keep_page=True, scrolldown=1)
# flipkart.html.render(sleep=1, keep_page=True, scrolldown=1)
# alibaba.html.render(sleep=1, keep_page=True, scrolldown=1)
# snapdeal.html.render(sleep=1, keep_page=True, scrolldown=1)
# indiamart.html.render(sleep=1, keep_page=True, scrolldown=1)

amazon_data = amazon.html.find(".s-card-container")
# flipkart_data = flipkart.html.find("")
# alibaba_data = alibaba.html.find("")
# snapdeal_data = snapdeal.html.find("")
# indiamart_data = indiamart.html.find("")

print(amazon_data[0])

# for i in amazon_data:
#     print(i)


