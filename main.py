import requests
import pyperclip
# ver 0.02
def 获取释义(成语):

    a=requests.get(f'https://hanyu.sogou.com/result?query={成语}').text
    # print('a',a)
    b=a.find('基础释义\n')
    # print('b', b)
    if '详细释义\n  </h3>' in a:
        c=a.index('详细释义\n  </h3>')
    elif '出处\n  </h3>' in a:
        c=a.index('出处\n  </h3>')
    elif '例句\n  </h3>' in a:
        c=a.index('例句\n  </h3>')
    elif '近义词\n    </h3>' in a:
        c=a.index('近义词\n    </h3>')
    else:
        c=a.find('成语接龙\n    </h3>')
    if b!=-1 and c!=-1:
        return ''.join([i for i in a[b+4:c] if ord(i)>=12246])
print('===批量成语释义v0.01@真爱===')
while True:
    result_list =''
    cy=input('输入批量成语，用中文逗号隔开：').split('，')
    for i in cy:
        if 获取释义(i):
            result = i +'—'+获取释义(i)
            print(result)
            result_list = result_list + '\n' +result
        else:
            result = i + '—' +'查不到该词语'
            print(result)
    pyperclip.copy(result_list)
    nothing = input('已经复制结果，请按回车继续下一批查询...')