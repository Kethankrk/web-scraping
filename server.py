from flask import Flask
from flask import jsonify
from requests_html import HTMLSession, AsyncHTMLSession
import threading

app = Flask(__name__)

@app.route("/")
async def scraping_function():
    amazon = await AsyncHTMLSession().get("https://www.amazon.in/s?k=pocox3")
    flipkart = await AsyncHTMLSession().get("https://www.flipkart.com/search?q=pocox3")

    await amazon.html.arender(sleep=1, keep_page=True, scrolldown=1)
    await flipkart.html.arender(sleep=1, keep_page=True, scrolldown=1)

    amazon_data = amazon.html.find(".s-card-container")
    flipkart_data = flipkart.html.find("._2kHMtA")

    await AsyncHTMLSession().close()

    total_list = []

    def amazon_function():

        # Filtering the Products
        amazon_product_filter = []
        for items in amazon_data:
            amazon_heading = items.find(".a-size-medium", first=True).text.lower()
            if "poco x3" in amazon_heading:
                amazon_product_filter.append(items)
        
        # Finding the least price from the filtered list 
        amazon_price_list = []
        for items in amazon_product_filter:
            try:
                amazon_price = items.find(".a-price-whole", first=True).text
                amazon_price_list.append(amazon_price.replace(",", ""))
            except:
                continue
    
        amazon_price_list.sort()
        amazon_least_price = amazon_price_list[0]
        # print(amazon_least_price)

        for items in amazon_product_filter:
            try:
                price_check = items.find(".a-price-whole", first=True).text.replace(",", "")
                if price_check == amazon_least_price:
                    # print(f"Product in amazon: {items.text}")
                    amazon_product = items
                    break
            except:
                continue
        from_amazon = {
            "heading": amazon_product.find(".a-size-medium", first=True).text,
            "rating": amazon_product.find(".a-size-base", first=True).text,
            "price": amazon_product.find(".a-price-whole", first=True).text,
            # "image": amazon_product.find(".")
        }
        total_list.append(from_amazon)

    def flipkart_function():
        flipkart_product_filter = []
        for items in flipkart_data:
            flipkart_heading = items.find("._4rR01T", first=True).text.lower()
            if "poco x3" in flipkart_heading:
                flipkart_product_filter.append(items)
        
        flipkart_price_list = []
        for items in flipkart_product_filter:
            flipkart_price = items.find("._30jeq3", first=True).text
            flipkart_price_list.append(flipkart_price.replace(",", ""))
        
        flipkart_price_list.sort()
        # print(f"The least amount in Flipkart: {flipkart_price_list[0]}")
        flipkart_least_price = flipkart_price_list[0]

        for items in flipkart_product_filter:
            try:
                Fprice_check = items.find("._30jeq3", first=True).text.replace(",", "")
                if Fprice_check == flipkart_least_price:
                    # print(f"Product in flipkart: {items.text}")
                    flipkart_final_product = items
                    break
            except:
                continue
        
        from_flipkart = {
            "heading": flipkart_final_product.find("._4rR01T", first=True).text,
        }
        total_list.append(from_flipkart)
    amazon_function()
    flipkart_function()
    print(total_list)
    return await total_list


if __name__ == "__main__":
    app.run(debug=True)
