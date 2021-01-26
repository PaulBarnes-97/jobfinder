import json
import os

fp = os.getcwd()+"/json dump/"+"2021-01-24.json"
json = json.loads(open(fp).read())
val = json["job"]
print(len(val[3]["Link"]))