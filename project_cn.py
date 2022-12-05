import ipaddress

def findClass(ip4):
    ip = int(ip4[0])
    if (ip >= 0 and ip <= 127):

        return ["255.0.0.0", 'Class A']

    elif (ip >= 128 and ip <= 191):

        return ["255.255.0.0", 'Class B']

    elif (ip >= 192 and ip <= 223):

        return ["255.255.255.0", 'Class C']

    elif (ip >= 224 and ip <= 239):
        return ['','Class D']

    else:
        return ['', 'Class E']


def sub_binary(subnet):
    subnet = subnet.split(".")
    return format(int(subnet[0]), '08b') + '.' + format(int(subnet[1]), '08b') + '.' + format(int(subnet[2]),
                                                                                              '08b') + '.' + format(
        int(subnet[3]), '08b')


def net_mask(netmask):
    subnet = netmask.split(".")
    return format(int(subnet[0]), '08b') + '.' + format(int(subnet[1]), '08b') + '.' + format(int(subnet[2]),
                                                                                              '08b') + '.' + format(
        int(subnet[3]), '08b')


def subnet_ipaddr(ip_4):
    return ip_4.network_address


# ip = input("Enter IP: ")
# ip4 = ip.split(".")
# sub = findClass(ip4)
# print("Default Subnet:", sub, end="  ")
# print("(", sub_binary(sub), ")\n")
#
# bit = int(input("Enter no of subnet bits: "))
# if sub == "255.0.0.0":
#     bit = bit + 8
# elif sub == "255.255.0.0":
#     bit = bit + 16
# else:
#     bit = bit + 24
# ip_4 = ipaddress.ip_network(f'{ip}/{bit}', strict=False)
# print("Subnet Mask:", ip_4.netmask, end="  ")
#
# print("(", net_mask((ip_4.netmask).__str__()), ")")
# print("Network address:", subnet_ipaddr(ip_4))
# lis_hosts = list(ip_4.hosts())
# print(f'Number of hosts:  {lis_hosts[0]} - {lis_hosts[-1]} ')
# print(f'Broadcast Address: {ip_4.broadcast_address}')
# print(f'Total number of hosts: {len(lis_hosts)}')
# print(f'Usable Hosts: {len(lis_hosts)+2}')
# if ip_4.is_private == True:
#     print("Private Network")
# else:
#     print("Public Network")
#
# print(ip_4)
