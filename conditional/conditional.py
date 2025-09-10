device = "acti"
tempreture  = 20
if device=="active":
    if tempreture > 35:
        print("high teperature alert")
    else:
        print("temperature is normal")
if not device=="active":
    print("device is offline")