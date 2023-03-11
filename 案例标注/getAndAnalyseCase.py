from flask import Flask, request, render_template, jsonify

global caseContent
global contentList
global jsondata
global userSelect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('前端页面.html')

@app.route('/get_test')
def get_test():
    num=request.args['get1']
    print(num)
    return str(num)

@app.route('/posttest',methods=['POST'])
def post_test():
    global caseContent
    global contentList
    caseContent=request.values['post1']
    print(caseContent)
    f=open('./用户输入的裁判文书.txt','a',encoding='utf-8')
    f.write(caseContent)
    f.write('\n\n')
    contentList=caseContent.split("\n")
    createAnnotation()
    return jsonify(jsondata)

@app.route('/saveData',methods=['POST'])
def getUserSelect():
    global userSelect
    userSelect=request.values['hide']
    print(userSelect)
    store(userSelect)
    return userSelect



@app.route('/posttest1/<number>',methods=['POST'])
def posttest1(number):

    return jsonify({"result":int(number)+1})


def createAnnotation():
    Annotation = {
        # 标注的标准格式
        # 注意：每次在createAnnotation方法中必须对所有字典项进行修改
        "姓名": "",
        # 姓名
        "性别": "",
        # 性别
        "民族": "",
        # 民族
        "出生地": "",
        # 出生地
        "罪行": "",
        # 罪行
        "法院": {}
        # 判决法院
    }
    # ##############################处理代码的位置############################## #
    lineNo = 0
    num = 0
    count = 1 # changed
    global contentList
    for line in contentList:
        lineNo = lineNo + 1
        if lineNo == 4:
            # 提取第四行中有的信息，参考该行文本内容，先用逗号分割
            fifthline = line.split('，')
            i = 0
            for str in fifthline:
                i = i+1
                if '被告人' in str:
                    Annotation['姓名'] = str.split('被告人')[1]
                if '男' in str:
                        Annotation['性别'] = '男'
                if '女' in str:
                        Annotation['性别'] = '女'
                if '出生' in str:
                    if '出生于' in str:
                        Annotation['出生地'] = str.split('出生于')[1]
                    else:
                        sentence = fifthline[i]
                        if '人' in sentence:
                            Annotation['出生地'] = sentence.split('人')[0]
                        else:
                            Annotation['出生地'] = '不详'
                if '族' in str:
                    if len(str) < 5:
                        Annotation['民族'] = str
        if lineNo == 5:
            # 提取第五行中有的信息，参考该行文本内容
            sixthline = line.split('，')
            for str in sixthline:
                if '罪一案' in str:
                    index = str.rfind('犯')
                    Annotation['罪行'] = str[index+1:].split('一案')[0]
                if '法院' in str:  # changed
                    index = str.find('法院')
                    Annotation["法院"][count] = str[:index+2]
                    count = count + 1
                    break
            sixline = line.split('。')[2]
            index = sixline.find('法院')  # changed
            if index < 10:
                Annotation["法院"][count] = sixline[:index+2]
                count = count + 1
        # 提取其他法院信息，标志为该行以核准开始########################################## changed ###################
        if line.startswith(' 核准'):
            indexstart = line.find(' 核准') + 3
            indexend = line.find('法院') + 2
            stemp = line[indexstart:indexend]
            # if stemp not in Annotation["Courts"]:
            #    Annotation["Courts"][count] = stemp
            #    count = count + 1
            test = 0
            for item in Annotation["法院"]:
                if stemp == Annotation["法院"][item]:
                    test = 1
            if test == 0:
                Annotation["法院"][count] = stemp
                count = count + 1
        else:
            if line.startswith('核准'):
                indexstart = line.find('核准') + 2
                indexend = line.find('法院') + 2
                stemp = line[indexstart:indexend]
                # if stemp not in Annotation["Courts"]:
                #    Annotation["Courts"][count] = stemp
                #    count = count + 1
                test = 0
                for item in Annotation["法院"]:
                    if stemp == Annotation["法院"][item]:
                        test = 1
                if test == 0:
                    Annotation["法院"][count] = stemp
                    count = count + 1
    Annotation["法院"][count]="中华人民共和国最高人民法院"
    # ##############################处理代码结束############################## #
    global jsondata
    jsondata=Annotation


import json
def store(jsonstr):
    res = json.loads(jsonstr)[0]
    url = "用户标注.json"
    with open(url, 'r') as f:
        jsonObj = json.load(f)
    f.close()
    with open(url, 'w') as fp:
        jsonObj[res["姓名"]] = res
        fp.truncate()
        fp.write(json.dumps(jsonObj, indent=4, ensure_ascii=False))
    fp.close()


if __name__ == '__main__':
    app.run(debug=True)


