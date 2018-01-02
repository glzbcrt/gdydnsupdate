#
# This Python script will update a DNS record at GoDaddy with your external IP address.
# Change it to reflect your needs.
#
# Created by glzbcrt (george@georgeluiz.com) @ 08/05/2017.
#
import requests
import json
import time
import sys

#
# Put here your key and secret to access GoDaddy APIs.
# Get them at https://developer.godaddy.com/keys/
#
GODADDY_KEY    = "MY_KEY"
GODADDY_SECRET = "MY_KEY_SECRET"

#
# Configure here the DNS zone and resource record you want to update with your external IP address.
#
GODADDY_ZONE = "myzone.com"
GODADDY_HOST = "home"

def getExternalAddress():
    return requests.get("https://api.ipify.org?format=json").json()["ip"]

def updateDnsRecord(zone, record, type, value):
    headers = {
        "Authorization": "sso-key " + GODADDY_KEY + ":" + GODADDY_SECRET,
        "Content-Type": "application/json"
    }

    #
    # Docs for the APIs can be found at https://developer.godaddy.com/doc
    #
    url = "https://api.godaddy.com/v1/domains/%s/records/%s/%s" % (zone, type, record)
    body = [ { "data": value } ]

    rc = requests.put(url, json.dumps(body), headers = headers).status_code

    if (rc == 200):
        print("DNS record updated successfully.")
    else:
        print("Error %s while updating DNS record.")

previousAddress = ""

while 1 == 1:
    try:
        currentAddress = getExternalAddress()

        if (currentAddress != previousAddress):
            updateDnsRecord(
                GODADDY_ZONE,
                GODADDY_HOST,
                "A",
                currentAddress
            )

            previousAddress = currentAddress
        else:
            print("Address did not change.")

    except:
        print(sys.exc_info()[2])

    # Iterate forever sleeping half hour between each one.
    time.sleep(1800)
