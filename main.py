import requests
import json
from acc import BASE_URL , API_KEY , rules , url
from sms_send import send_sms
from fixer import get_request


def archive(filename,rates):
    with open(f'archive/{filename}.json','w') as f:
        f.write(json.dumps(rates))

def check_notify_rules(rates):
    preferred=rules['notification']['preferred']
    msg=''
    for exc in preferred:
        print(preferred[exc]['min'])
        if float(rates[exc]) <= float(preferred[exc]['min']):
            msg+=f'{exc} reached min{rates[exc]}'
            print(msg)
            
        if float(rates[exc]) >= float(preferred[exc]['min']):
            msg+=f'{exc} reached max{rates[exc]}'


    return msg

def send_notification(msg):
    send_sms(msg)



def send_mail(timestamp,rates):
    subject = f'{timestamp} rates'
    if rules['preferred'] is not None:
        tmp = dict()
        for exc in rules['preferred']:
            tmp[exc]=rates[exc]
        rates = tmp
    text = json.dumps(rates)



if __name__ == "__main__":
    rat=get_request(url)
    archive(rat['date'],rat['rates'])
    if rules["notification"]['status']:
        notification_msg = check_notify_rules(rat['rates'])
        if notification_msg:
            send_notification(notification_msg)
