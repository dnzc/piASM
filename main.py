# this file runs a .piASM program

def run(program, memory_string):
	stack = []

	# find pointers
	pointers = {}
	for i,ins in enumerate(program):
		if ins[0] == 'P':
			pointers[int(ins[1:])] = i

	MEM = [int(i) for i in memory_string.split(',')]
	
	curins = 0
	while curins < len(program):
		# print(stack, MEM)
		ins = program[curins]
		char = ins[0]
		# general
		if char == 'P':
			pass
		elif char == 'j':
			a = stack.pop(0)
			b = stack.pop(0)
			if a == 1:
				curins = pointers[b]
		elif char == 'J':
			a = stack.pop(0)
			b = stack.pop(0)
			if b == 1:
				curins = pointers[a]
		elif char == 'p':
			stack.insert(0, int(ins[1:]))
		elif char == 'g':
			val = stack.pop(0)
			stack.insert(0, MEM[val])
		elif char == 's':
			val = stack.pop(0)
			MEM[val] = stack.pop(0)
		# I/O
		elif char == 'i':
			stack.insert(0, int(input()))
		elif char == 'o':
			print(stack.pop(0))
		elif char == 'I':
			inp = input()
			for i in inp:
				stack.insert(0, ord(i))
			stack.insert(0, len(inp))
		elif char == 'O':
			print(chr(stack.pop(0)))
		# logic
		elif char == 'E':
			a = stack.pop(0)
			stack.insert(0, int(a==0))
		elif char == 'L':
			a = stack.pop(0)
			b = stack.pop(0)
			stack.insert(0, a<b)
		elif char == 'A':
			a = stack.pop(0)
			b = stack.pop(0)
			stack.insert(0, a&b)
		elif char == 'X':
			a = stack.pop(0)
			b = stack.pop(0)
			stack.insert(0, a^b)
		# maths
		elif char == 'a':
			a = stack.pop(0)
			b = stack.pop(0)
			stack.insert(0, a+b)
		elif char == 's':
			a = stack.pop(0)
			b = stack.pop(0)
			stack.insert(0, a-b)
		elif char == 'm':
			a = stack.pop(0)
			b = stack.pop(0)
			stack.insert(0, a*b)
		elif char == 'd':
			a = stack.pop(0)
			b = stack.pop(0)
			stack.insert(0, a//b)
		else:
			print(f'invalid syntax at instruction {curins}: {ins}')
			return

		curins += 1
	
	print('Program executed successfully')

#################################

import re

##### get file to run

filenames = ['examples/0_add.piASM', 'examples/1_exponentiation.piASM']

print('Input a number to choose which file to run:')
for i,val in enumerate(filenames):
	print(f'    {i}) {val}')
filename = filenames[int(input())]

##### parse file

raw = open(filename, 'r').read().split('\n')
# remove comments + blank lines
parsed = [i for i in raw if '#' not in i and i != '']
# extract memory string
memory_string = parsed.pop(0)
# remove whitespace
parsed = re.sub('\s+', '', ''.join(parsed))
# separate instructions
program = re.findall(r'[a-zA-Z]\d*', parsed)
print("Loaded program:", parsed)

##### run

print(f'Starting execution of {filename}')
run(program, memory_string)