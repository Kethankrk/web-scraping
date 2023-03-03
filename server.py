from flask import Flask
from flask import jsonify
from requests_html import HTMLSession

app = Flask(__name__)


def lol():
    session = HTMLSession()


    url = "http://results.uoc.ac.in/"
    r = session.get(url)

    r.html.render(sleep=1, keep_page=True, scrolldown=1)

    data = r.html.find(".sorting_2")
    data2 = r.html.find(".sorting_1")
    wow = []
    for i in data:
        wow.append({
            "heading": i.text
        })
    data2List = []
    for i in data2:
        data2List.append({
            "date": i.text
        })
    totalData = []


    for i in range(len(wow)):
        totalData.append({
            "heading": wow[i]["heading"],
            "date": data2List[i]["date"]
        })

    return totalData

myData = lol()


@app.route("/")
def fun():

    return jsonify(myData)


if __name__ == "__main__":
    app.run(debug=True)
