NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
NAT_GIGA = NAT.replace('Fast', 'Gigabit')
print (NAT_GIGA)
