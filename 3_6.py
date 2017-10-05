ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf_keys = ['Protocol', 'Prefix', 'AD/Metric', 'Next Hop', 'Last Update', 'Outbound Interface']

ospf_route = ospf_route.replace('O', 'OSPF')
ospf_route = ospf_route.replace('[110/41]', '110/41')

ospf_route = ospf_route.split()
ospf_route.remove('via')

ospf_dict = dict(zip(ospf_keys, ospf_route))

for i in ospf_dict:
 print('{0:25} {1}'.format(i + ':', ospf_dict[i]))
