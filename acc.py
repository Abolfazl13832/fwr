BASE_URL= "http://data.fixer.io/api/latest?access_key="
API_KEY = "417315d1a83ba5efac35080cf1725ffe"

url = BASE_URL + API_KEY


EMAIL_RECEIVER = "alypwr573@gmail.com"


rules = {
    'archive':True,
    'send_mail':True,
    'notification':{
        'status':True,
        'receiver':'09929399646',
        'preferred':{
            'BTN':{'min':'92.318437','max':'93'},
            'IRR':{'min':'45000','max':'50000'},
        }
    }    
}