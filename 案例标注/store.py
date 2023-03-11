import json

def store(jsonstr):
    res = json.loads(jsonstr)
    url = r"用户标注.json"
    with open(url, 'r') as f:
        jsonObj = json.load(f)
    f.close()
    with open(url, 'w') as fp:
        jsonObj[res["Criminals"]] = res
        fp.truncate()
        fp.write(json.dumps(jsonObj, indent=4, ensure_ascii=False))
    fp.close()
    # jsonObj=json.dumps(jsonstr,ensure_ascii=False)
    # f=open("用户标注.json",'a')
    # f.write(jsonObj)
    # f.write("\n")


if __name__=='__main__':
    store("{\"Criminals\":\"李大卫\",\"Gender\":\"男\",\"Courts\": {\"1\": \"北京市第二中级人民法院\",\"2\": \"北京市高级人民法院\",\"3\": \"中华人民共和国最高人民法院\"}}")