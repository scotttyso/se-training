import requests
import json

"""
Modify these please
"""
url='http://vpn.advtechracks.com:8188/ins'
switchuser='admin'
switchpassword='C1sc0123'

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "config t ;vlan 900 ;name db",
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()