import requests
import json
from acc import BASE_URL , API_KEY , rules , url
from sms_send import send_sms
from fixer import get_rates


def archive(filename,rates):
    with open(f'{filename}.json','w') as f:
        f.write(json.dumps(rates))

def check_notify_rules(rates):
    preferred=rules['notification']['preferred']
    msg=''
    for exc in preferred:
        if float(rates[exc]) <= float(preferred[exc]['min']):
            msg+=f'به کمترین مقدار خود رسید'
            
        if float(rates[exc]) >= float(preferred[exc]['max']):
            msg+=f'به بیشترین مقدار تعیین شده رسیده است'


    return msg
if __name__ == "__main__":
    rat=get_rates(url)
    archive(rat['date'],rat['rates'])
    if rules["notification"]['status']:
        notification_msg = check_notify_rules(rat['rates'])
        if notification_msg:
            print(notification_msg)
