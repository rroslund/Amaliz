import os, urllib, json, sys
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

app.config.update(
        DEBUG = True,
        )

baseurl = 'http://census.soe.com/get/ps2-beta/'
def getCharId(name):
    url='http://census.soe.com/get/ps2-beta/character/?name.first_lower='+name+'&c:show=name.first'
    return int(json.loads(urllib.urlopen(url).read())['character_list'][0]['id'])

def getBRank(name):
    url = 'http://census.soe.com/get/ps2-beta/character/?name.first_lower='+name+'&c:show=experience.rank&c:show=name.first'
    return urllib.urlopen(url).read()

def ggetCharId(name):
    return 9001

def getItemTESTJson(url):
    f = file('/Users/rich/Documents/items.json','r')
    res =  json.loads(f.read())
    f.close()
    return res
def ggetJson(url):
    f = file('/Users/rich/Documents/amalizDeaths.json','r')
    res =  json.loads(f.read())
    f.close()
    return res


def getJson(url):
    return json.loads(urllib.urlopen(url).read())

def getDeathsByWeapon(name,numToCheck):
    charId = getCharId(name);
    url = baseurl+'/characters_event/'+str(charId)+'?type=DEATH&c:limit='+str(numToCheck)
    res = getJson(url)
    weaponInfo = [x['attacker_weapon_id'] for x in res['characters_event_list'] if int(x['attacker_weapon_id'])!=0]
    uniqueWeps = set(weaponInfo)
    wepDeathCount = {x:weaponInfo.count(x) for x in uniqueWeps}
    wepRank = list(set(wepDeathCount.values()))
    wepRank.sort()
    wepRes = [x for x in wepDeathCount.items() if x[1] > wepRank[len(wepRank)-10]]
    return json.dumps([(getItemName(x[0]),x[1]) for x in wepRes])

def getItemName(itemId):
    url = baseurl+'/item/'+str(itemId)+'?c:show=name'
    jsonres = getJson(url)
    res = [x['name']['en'] for x in jsonres['item_list'] if int(x['id'])==int(itemId)]
    if res != None and len(res)>0:
        return res[0]
    else:
        return 'UNKNOWN'
            




#----
# controllerz
#----
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
    'ico/favicon.ico')

@app.route("/comparison/")
def comparison():
    return render_template('comparison.html')
@app.route("/home/")
def home():
    return render_template('index.html')
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/test")
def test():
    return "This is a test"

@app.route("/brank/<username>")
def brank(username):
    return getBRank(username)
@app.route("/weapon_deaths/<userOne>&<amount>")
def deathsByWep(userOne,amount):
    return getDeathsByWeapon(userOne,amount)





if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=port)

