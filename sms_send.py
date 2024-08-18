from kavenegar import *
from acc import rules
def send_sms(text):
    try:
        api = KavenegarAPI('76546C52473948666F383650466D5442422B794E486459456B61724879613531714D544A62663537772B383D')
        params = {
            'sender': '1000689696',#optional
            'receptor': rules['notification']['receiver'],
            'message': text,
        } 
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)