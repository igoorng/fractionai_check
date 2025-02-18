import requests
import time
from datetime import datetime

USERID_LIST = [218512,218752,219065,219105,219221,219246,219342,219363,219480,219509,219578,219743,220010,220055,220076,220095,220121,220184,220706,220768,220796,220808,220833,220856,220878,222943,222965,223141,223154,223178,223214,224015,224024,230258,230306,230343,230370,230377,230374,230414]

for USERID in USERID_LIST:

    # 设置请求的URL
    url = 'https://dapp-backend-4x.fractionai.xyz/api3/rewards/fractal/user/{}'.format(USERID)

    # 设置请求头
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Allowed-State': 'na',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Origin': 'https://dapp.fractionai.xyz',
        'Pragma': 'no-cache',
        'Referer': 'https://dapp.fractionai.xyz/',
    }

    # 发送GET请求
    response = requests.get(url, headers=headers)

    # 检查响应状态码
    if response.status_code == 200:
        # 解析JSON响应
        data = response.json()
        
        # 获取userFractals字段的值
        user_fractals = data.get('userFractals')     
        # 获取userFractals字段的值（注意：可能是userFractals的拼写错误，实际字段名可能不同）
        # 这里假设你想获取的是另一个字段，具体要根据实际情况调整
        dailyFractals = data.get('dailyFractals')  # 假设字段名为userFractals2

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open('log.txt', 'a', encoding='utf-8') as log_file:  # 'a' 模式表示追加写入
            log_file.write(f'[{current_time}] 钱包账户{USERID_LIST.index(USERID) + 1}: 账号总积分: {user_fractals} 今日获取积分: {dailyFractals}\n')

        time.sleep(2)
    else:
        print('请求失败，状态码:', response.status_code)

print('所有请求已查询完成，请查看当前目录下的log.txt文件')
