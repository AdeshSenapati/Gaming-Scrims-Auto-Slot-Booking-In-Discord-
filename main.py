import requests
import datetime
import time

#https://discord.com/api/v9/channels/728567993495191594/messages

payload = {
'content': """TEAM NAMes....
"""
}

header = {
'authorization': 'key'
}

twelvethirtypmregis = 854694993166729236
onethirtypmregis = 852237476000038952
twothirtypmregis = 854694413551534121
threethirtypmregis = 854694489125158942
fourthirtypmregis = 854694548114898944
fivethirtypmregis = 854694601704734740
sixthirtypmregis = 854694661331353620
seventhirtypmregis = 854694708642316288
eightthirtypmregis = 854694756471013376
ninethirtypmregis = 854694799809445899
tenthirtypmregis = 854694851558637618
eleventhirtypmregis = 854694885700534332
while True:
    mytime = datetime.datetime.now().strftime('%I:%M %p')

    if mytime == '10:13 AM':
        r = requests.post(f'https://discord.com/api/v9/channels/{twelvethirtypmregis}/messages',
                          data=payload, headers=header)
        while mytime == '10:13 AM':
            print('waiting...')
            mytime = datetime.datetime.now().strftime('%I:%M %p')

    elif mytime == '10:14 AM':
        r = requests.post(f'https://discord.com/api/v9/channels/{onethirtypmregis}/messages',
                          data=payload, headers=header)
        while mytime == '10:14 AM':
            print('waiting...')
            mytime = datetime.datetime.now().strftime('%I:%M %p')
        # time.sleep(60)

    elif mytime == '10:15 AM':
        r = requests.post(f'https://discord.com/api/v9/channels/{twothirtypmregis}/messages',
                          data=payload, headers=header)
        while mytime == '10:15 AM':
            print('waiting...')
            mytime = datetime.datetime.now().strftime('%I:%M %p')

    elif mytime == '10:16 AM':
        r = requests.post(f'https://discord.com/api/v9/channels/{threethirtypmregis}/messages',
                          data=payload, headers=header)
        while mytime == '10:16 AM':
            print('waiting...')
            mytime = datetime.datetime.now().strftime('%I:%M %p')

    elif mytime == '10:17 AM':
        r = requests.post(f'https://discord.com/api/v9/channels/{fourthirtypmregis}/messages',
                          data=payload, headers=header)
        while mytime == '10:17 AM':
            print('waiting...')
            mytime = datetime.datetime.now().strftime('%I:%M %p')

    elif mytime == '10:18 AM':
        r = requests.post(f'https://discord.com/api/v9/channels/{fivethirtypmregis}/messages',
                          data=payload, headers=header)
        while mytime == '10:18 AM':
            print('waiting...')
            mytime = datetime.datetime.now().strftime('%I:%M %p')

    elif mytime == '10:19 AM':
        r = requests.post(f'https://discord.com/api/v9/channels/{sixthirtypmregis}/messages',
                          data=payload, headers=header)
        while mytime == '10:19 AM':
            print('waiting...')
            mytime = datetime.datetime.now().strftime('%I:%M %p')

    elif mytime == '10:20 AM':
        r = requests.post(f'https://discord.com/api/v9/channels/{seventhirtypmregis}/messages',
                          data=payload, headers=header)
        while mytime == '10:20 AM':
            print('waiting...')
            mytime = datetime.datetime.now().strftime('%I:%M %p')

    elif mytime == '10:21 AM':
        r = requests.post(f'https://discord.com/api/v9/channels/{eightthirtypmregis}/messages',
                          data=payload, headers=header)
        while mytime == '10:21 AM':
            print('waiting...')
            mytime = datetime.datetime.now().strftime('%I:%M %p')

    elif mytime == '10:22 AM':
        r = requests.post(f'https://discord.com/api/v9/channels/{ninethirtypmregis}/messages',
                          data=payload, headers=header)
        while mytime == '10:22 AM':
            print('waiting...')
            mytime = datetime.datetime.now().strftime('%I:%M %p')

    elif mytime == '10:23 AM':
        r = requests.post(f'https://discord.com/api/v9/channels/{tenthirtypmregis}/messages',
                          data=payload, headers=header)
        while mytime == '10:23 AM':
            print('waiting...')
            mytime = datetime.datetime.now().strftime('%I:%M %p')

    elif mytime == '10:24 AM':
        r = requests.post(f'https://discord.com/api/v9/channels/{eleventhirtypmregis}/messages',
                          data=payload, headers=header)
        break
    else:
        print(mytime)