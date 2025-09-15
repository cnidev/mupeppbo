import time

import requests
from celery import shared_task

@shared_task
def send_mass_sms_task(phone_number_list, content_list, access_token):
    
    url = "https://api.orange.com/smsmessaging/v1/outbound/tel%3A%2B2250707830932/requests"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    for phone_number in phone_number_list:
        payload = {
            "outboundSMSMessageRequest": {
		        "address": f"tel:+225{phone_number}",
		        "senderAddress":"tel:+2250707830932",
                "senderName": "MUPEPPBO",
		        "outboundSMSTextMessage": {
			        "message": f"{content_list}"
                }
            }

        }
        rq = requests.post(url=url, json=payload, headers=headers)
        print(f"REQUEST: {rq.text}")
        time.sleep(0.2)