ip = input('Enter IP address in format 10.1.1.1/24 ')

print('\n' + '-' * 30)

split_main = ip.split('/')

split_ip = split_main[0]
split_mask = '/' + split_main[1]

ip_bin = '.'.join([bin(int(x)+256)[3:] for x in split_ip.split('.')])
split_bin = ip_bin.split('.')

split_ip_general = split_ip.split('.')

print(split_mask)

for i in split_ip_general:
 print('{0:10}'.format(i), end='')
print('')

for i in split_bin:
 print('{0:10}'.format(i), end='')
print('')
