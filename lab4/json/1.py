import json
data = open('sample-data.json').read()
object = json.loads(data)
print(
    "================================================================================" "\n"
    "DN                                                 Description           Speed    MTU" "\n" 
    "-------------------------------------------------- --------------------  ------  ------")
ndata = object["imdata"]
for i in ndata:
    a = i["l1PhysIf"]["attributes"]
    print("{0:50} {1:20} {2:7} {3:6}".format(a["dn"],a["descr"],a["speed"],a["mtu"]))
    