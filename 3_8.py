ip = '192.168.3.1'

ip_bin = '.'.join([bin(int(x)+256)[3:] for x in ip.split('.')])

split_bin = ip_bin.split('.')
split_ip = ip.split('.')

for i in split_ip:
 print('{0:10}'.format(i), end='')
print('')

for i in split_bin:
 print('{0:10}'.format(i), end='')
print('')
