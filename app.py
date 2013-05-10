import os, urllib
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

app.config.update(
        DEBUG = True,
        )


def getBRank(name):
    url =
    'http://census.soe.com/get/ps2-beta/charater/?name.first_lower='+name+'&c:show=experience.rank'
    return urllib.urlopen(url).read()




#----
# controllerz
#----
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
    'ico/favicon.ico')

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/test")
def test():
    return "This is a test"

@app.route("/brank/<username>")
def brank(username):
    return getBRank(username)




if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=port)


