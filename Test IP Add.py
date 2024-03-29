ip_address = input("Enter ip address: ")
octets = ip_address.split(".")
print(octets)
correct_ip = True

if len(octets) != 4:
    correct_ip = False
else:
    for octet in octets:
        if not (octet.isdigit() and int(octet) in range(256)):
            correct_ip = False
            break

if not correct_ip:
    print("Нis not correct")
else:
    octets_num = [int(i) for i in octets]

    if octets_num[0] in range(1, 224):
        print("unicast")
    elif octets_num[0] in range(224, 240):
        print("multicast")
    elif ip_address == "255.255.255.255":
        print("local broadcast")
    elif ip_address == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")