# anotation

数据科学基础大作业

## 项目介绍

简介：我们对裁判文书网上刑事案件文书中的重要信息进行标注，并对标注进行数据分析与数据可视化，以便于对历史司法案件的数据与数据特性进行挖掘，从而提高刑事案件的处理效率。

本项目总共分为两个部分：
1. 案例标注：获取文书并对文书进行标注；
2. 标注分析：对标注进行统计分析，最后可视化数据。

## 案例标注

### step 1 获取原始数据

为了能够做最基本的分析，我们要先从裁判文书网上下载大量的刑事案件的文书案例，但是由于下载效率过慢，所以最终只获取了100分案例。
案例模板如下：
```txt
孟生辉故意杀人死刑复核刑事裁定书
 中华人民共和国最高人民法院
 刑 事 裁 定 书
 被告人孟生辉，男，汉族，1983年5月21日出生于甘肃省文县，初中文化，无业，户籍地文县××乡××村××号，住址地文县××镇出租房。2016年12月2日被逮捕。现在押。
 四川省广元市中级人民法院审理广元市人民检察院指控被告人孟生辉犯故意杀人罪一案，于2017年12月26日以（2017）川08刑初49号刑事判决，认定被告人孟生辉犯故意杀人罪，判处死刑，剥夺政治权利终身。宣判后，孟生辉提出上诉。四川省高级人民法院经依法开庭审理，于2019年5月21日以（2018）川刑终129号刑事裁定，驳回上诉，维持原判，并依法报请本院核准。本院依法组成合议庭，对本案进行了复核，依法讯问了被告人。现已复核终结。
 经复核确认：2016年7月，被告人孟生辉在中国太平洋财产保险股份有限公司为其所有的川××××××轻型普通货车购买了赔偿限额为50万元的第三者责任险。2016年10月，孟生辉因欠有银行贷款及他人借款无法归还，致使家庭经济困难，产生通过制造交通事故撞死妻子张春红（同案被告人，已判刑）的外曾祖母张某甲（被害人，殁年84岁）从而骗取保险金的想法，张春红得知后反对，但经孟生辉反复劝说，张春红遂同意。2016年10月23日，孟生辉、张春红以接张某甲外出看病为由，由孟生辉驾驶川××××××轻型普通货车从甘肃省文县××镇张春红母亲家中将张某甲接走，后孟生辉驾车拉载张某甲前往陕西省宁强县燕子砭镇、大安镇等地寻找作案机会未果。10月27日10时许，孟生辉驾驶川××××××轻型普通货车拉载张某甲行驶至国道212线761千米＋900米附近时，孟生辉以上厕所为由将车停靠路边，张某甲下车独自沿路步行，孟生辉驾车撞击张某甲，致张某甲因机动车撞击、碾压致脊髓离断、多脏器破裂死亡。
 上述事实，有第一审、第二审开庭审理中经质证确认的扣押的川××××××轻型普通货车，机动车保险单、借款借据、通话记录及事故调查报告书等书证，证人张某乙、孟某甲、孟某乙、王某甲、王某乙等的证言，机动车司法鉴定意见、尸体鉴定意见，现场勘验检查笔录，侦查实验笔录，电子证据检验笔录和同案被告人张春红的供述等证据证实。被告人孟生辉虽不供认，但足以认定。
 本院认为，被告人孟生辉为骗取保险金，故意驾车撞死他人，其行为已构成故意杀人罪。孟生辉与妻子合谋，为骗取保险金将被害人骗出，并在陕、甘、川三省交界处寻找作案机会，后驾车将被害人撞死，在共同犯罪中系犯意提出者和行为实施者，系主犯，且动机卑劣，手段残忍，情节特别恶劣，实属罪行极其严重，应依法惩处。第一审判决、第二审裁定认定的事实清楚，证据确实、充分，定罪准确，量刑适当。审判程序合法。依照《中华人民共和国刑事诉讼法》第二百四十六条、第二百五十条和《最高人民法院关于适用〈中华人民共和国刑事诉讼法〉的解释》第三百五十条第（一）项的规定，裁定如下：
 核准四川省高级人民法院（2018）川刑终129号维持第一审以故意杀人罪判处被告人孟生辉死刑，剥夺政治权利终身的刑事裁定。
 本裁定自宣告之日起发生法律效力。
 审判长　罗　敏
 审判员　魏海欢
 审判员　苏　敏
 二〇一九年十二月二十七日
 书记员　张名嘉
```

同时我们也支持用户访问“裁判文书分析器”页面来输入用户的感兴趣的刑事案件文书，并对文书实时生成标注信息，持久化后返回页面供用户使用。

### step 2 对数据进行标注

由于文书具有固定的格式，所以并没有使用NLP对文书进行分析，经过尝试使用NLP反而无法下手，所以采用基本的控制结构实现对案例的标注，并对标注使用json格式进行存储。
标注示例如下：
```txt
    "孟生辉": {
        "出生地": "甘肃省文县",
        "姓名": "孟生辉",
        "性别": "男",
        "民族": "汉族",
        "罪行": "故意杀人罪",
        "法院": {
            "1": " 四川省广元市中级人民法院",
            "2": "四川省高级人民法院",
            "3": "中华人民共和国最高人民法院"
        }
    }
```

## 标注分析

### 数据分析

对案件的发生地、性别、罪行、民族进行了分析

### 数据可视化

使用echarts、wordcloud为分析结果作图，并利用CSS模板展示到页面上
