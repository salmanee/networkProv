import os


num_nodes = [200, 250, 300, 350 , 400, 450, 500]

for n in num_nodes:
	with open('ts' + str(n), 'w') as f:
		f.write('ts 1 22\n')
		#generates 1 graph, 22 is initial seed
		f.write('3 0 0\n')
		f.write('1 20 3 0.5\n')
		# f.write(str(n) + ' ' + str(n) + ' 3 .2\n')
		f.write(str(n) + ' ' + '25 3 0.6\n')
		f.write('4 10 3 0.42\n')
	f.closed
	os.system('./itm ts' + str(n))
	os.system('./sgb2alt ts' + str(n) + '-0.gb ts' + str(n) + '.alt')
	os.system('rm ts' + str(n))
	os.system('rm ts' + str(n) + '-0.gb')
