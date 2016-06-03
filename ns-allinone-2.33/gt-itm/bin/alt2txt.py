#!/usr/bin/env python
import networkx as nx
import random
import sys
import math




def main(alt_file, txt_file):
	topology = {'nodes': [], 'edges': []}
	with open(alt_file, 'r') as fin:
		for line in fin:
			if line.strip() == 'VERTICES (index name u v w x y z):':
				break
		for line in fin:
			if line.strip() == '':
				break
			topology['nodes'].append(line.strip().split()[0])

		for line in fin:
			if line.strip() == 'EDGES (from-node to-node length a b):':
				break
		for line in fin:
			edge = line.strip().split()
			topology['edges'].append((edge[0], edge[1], edge[2]))
	
	with open(txt_file, 'w') as fout:
		fout.write('Nodes:\n')
		for node in topology['nodes']:
			fout.write(node)
			fout.write('\n')
		fout.write('Edges:\n')
		for edge in topology['edges']:
			fout.write(edge[0] + ' ' + edge[1] + ' ' + edge[2])
			fout.write('\n')

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print('Usage: python alt2txt.py .alt_file .txt_file')
		print('sample: python alt2txt ts100.alt ts100.txt')
	else:
		main(sys.argv[1], sys.argv[2])
