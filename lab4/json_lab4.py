import json




with open("sample-data.json", "r") as file:
    data = json.load(file)


print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU'}")
print("-" * 80)


for interface in data["imdata"]:
    attributes = interface["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes.get("speed", "inherit")  
    mtu = attributes["mtu"]
    

    print(f"{dn:<50} {'':<20} {speed:<7} {mtu}")
