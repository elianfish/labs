#/usr/bin/env python
#_*_coding:utf-8_*_

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}


current_menu = menu
parents = []

while True:
    for key in current_menu:
        print(key)

    item = input(">>请输入选项进入或输入back返回或输入quit退出:").strip()
    if item in current_menu:
        if current_menu[item]:
            parents.append(current_menu)
            current_menu = current_menu[item]
        else:
            print('这是最后选项')
    elif item == '':
        continue
    elif item == 'back':
        if parents:
            current_menu = parents.pop()
    elif item == 'quit':
        break
    else:
        print('输入有误!')

