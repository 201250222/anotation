from flask import Flask, render_template
import json
import _locale
_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf-8'])
jsonurl = r"Annotation.json"


app = Flask(__name__)


@app.route('/')
def hello():
    genderlist = getjson(jsonurl)[0]
    accusationlist = getjson(jsonurl)[1]
    ethnicitylist = getjson(jsonurl)[2]
    return render_template('analyse.html', genderlist=genderlist, accusationlist=accusationlist, ethnicitylist=ethnicitylist)


def getjson(purl):
    url = purl
    datalist = []
    genderlist = []
    accusationlist = [0,0,0,0]
    # 故意杀人罪 抢劫罪 强奸 其他
    ethnicitylist = [0, 0]
    with open(url, 'r') as f:
        jsonObj = json.load(f)
        count = 0
        for i in range(1, 101):
            if jsonObj[str(i)]["Gender"] == "男":
                count = count + 1
            if jsonObj[str(i)]["Accusation"] == "故意杀人罪":
                accusationlist[0] = accusationlist[0] + 1
            else:
                if "抢劫" in jsonObj[str(i)]["Accusation"]:
                    accusationlist[1] = accusationlist[1] + 1
                else:
                    if "毒" in jsonObj[str(i)]["Accusation"]:
                        accusationlist[2] = accusationlist[2] + 1
                    else:
                        accusationlist[3] = accusationlist[3] + 1
            if jsonObj[str(i)]["Ethnicity"] == "汉族":
                ethnicitylist[0] = ethnicitylist[0] + 1
            else:
                ethnicitylist[1] = ethnicitylist[1] + 1
        genderlist.append(count/100)
        genderlist.append((100-count)/100)
    f.close()
    datalist.append(genderlist)
    datalist.append(accusationlist)
    datalist.append(ethnicitylist)
    return datalist


if __name__ == '__main__':
    app.run()