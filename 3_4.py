command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

command1_split = command1.split()
command1_list = command1_split[-1].split(',')

command2_split = command2.split()
command2_list = command2_split[-1].split(',')

command1_set = set(command1_list)
command2_set = set(command2_list)

command_set = command1_set.intersection(command2_set)

command_main_list = list(command_set)

print (command_main_list)
