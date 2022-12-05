from tkinter import *
import time
from project_cn import *
root = Tk()



#frame
frame = Frame(master=root, width=350, height=150, bg='white')
frame.pack()
#ipaddr
lbl_ipaddr =  Label(master= frame, text = "IPaddress", bg='white').place(x=45,y=10)
ent_ipaddr = Entry(master= frame,)
ent_ipaddr.place(x=155.5, y=10)
#subnet bits
lbl_bits = Label(master= frame, text = "Subnet Bits", bg='white').place(x=45,y=50.5)
ent_bits = Entry(master= frame)
ent_bits.place(x=155.5,y=50.5)

#output function
def show_fn():

    ip_1 = str(ent_ipaddr.get())
    ip4_1 = ip_1.split(".")
    sub, INT_CLASS = findClass(ip4_1)
    #bits part
    bit_1 = int(ent_bits.get())
    if sub == "255.0.0.0":
        bit_1 = bit_1 + 8
    elif sub == "255.255.0.0":
        bit_1 = bit_1 + 16
    else:
        bit_1 = bit_1 + 24
    ip_4 = ipaddress.ip_network(f'{ip_1}/{bit_1}', strict=False)
    lis_hosts = list(ip_4.hosts())


    label_addr = Label(root, text =f'IP Address:  {ip_1}' ).pack()
    label_netaddr = Label(root, text=f'"Network address:", {subnet_ipaddr(ip_4)}').pack()
    label_hosts = Label(root, text = f'Host Range:  {lis_hosts[0]} - {lis_hosts[-1]} ').pack()
    label_brodaddr =Label(root, text = f'Broadcast Address: {ip_4.broadcast_address}').pack()
    label_numhosts = Label(root, text = f'Total number of hosts: {len(lis_hosts)}').pack()
    label_usehosts = Label(root, text = f'Usable Hosts: {len(lis_hosts)+2}').pack()


    label_fn = Label(root, text = f'Default Subnet: {sub}').pack()
    label_in = Label(root, text=f' Binary Default Subnet: {sub_binary(sub)}').pack()
    label_class = Label(root, text = f'IP Class: {INT_CLASS}').pack()
    label_sub = Label(root, text = f'Subnet Mask: {ip_4.netmask}').pack()
    label_subbin = Label(root, text = f'Binary Subnet Mask: {net_mask((ip_4.netmask).__str__())}').pack()
    if ip_4.is_private == True:
        label_type = Label(root, text = f'IP Type: Private Network').pack()
    else:
        label_type = Label(root, text=f'IP Type: Public Network').pack()

    label_cidr = Label(root, text = f'CIDR Notation: {ip_4}').pack()

button_1 = Button(root, text = "Show", command = show_fn).place(x = 150, y = 97)


root.mainloop()
