# this file runs a .piASM program

def run(program, memory_string):
	stack = []

	# find pointers
	pointers = {}
	for i,ins in enumerate(program):
		if ins[0] == "P":
			pointers[int(ins[1:])] = i

	MEM = []
	for i in memory_string.split(","):
		if i != "":
			MEM.append(int(i))
	
	curins = 0
	while curins < len(program):
		# print(stack, MEM)
		ins = program[curins]
		char = ins[0]
		# general
		if char == "P":
			pass
		elif char == "j":
			a = stack.pop(0)
			b = stack.pop(0)
			if a == 1:
				curins = pointers[b]
		elif char == "p":
			stack.insert(0, int(ins[1:]))
		elif char == "g":
			val = stack.pop(0)
			stack.insert(0, MEM[val])
		elif char == "s":
			val = stack.pop(0)
			MEM[val] = stack.pop(0)
		# I/O
		elif char == "i":
			while True:
				try:
					stack.insert(0, int(input()))
					break
				except:
					print("input failed, try again")
		elif char == "o":
			print(stack.pop(0), end="")
		elif char == "I":
			while True:
				a=input()
				if len(a)>0:break
			inp = a[0]
			stack.insert(0, ord(inp))
		elif char == "O":
			print(chr(stack.pop(0)), end="")
		elif char == "R":
			inp = input().replace("\n", "")
			for i in inp:
				stack.insert(0, ord(i))
			stack.insert(0, len(inp))
		# logic
		elif char == "e":
			a = stack.pop(0)
			stack.insert(0, int(a==0))
		elif char == "l":
			a = stack.pop(0)
			b = stack.pop(0)
			stack.insert(0, a<b)
		elif char == "a":
			a = stack.pop(0)
			b = stack.pop(0)
			stack.insert(0, a&b)
		elif char == "x":
			a = stack.pop(0)
			b = stack.pop(0)
			stack.insert(0, a^b)
		# maths
		elif char == "A":
			a = stack.pop(0)
			b = stack.pop(0)
			stack.insert(0, a+b)
		elif char == "S":
			a = stack.pop(0)
			b = stack.pop(0)
			stack.insert(0, a-b)
		elif char == "M":
			a = stack.pop(0)
			b = stack.pop(0)
			stack.insert(0, a*b)
		elif char == "D":
			a = stack.pop(0)
			b = stack.pop(0)
			stack.insert(0, a//b)
		else:
			print(f"unrecognized instruction around #{curins}: {ins}")
			return

		curins += 1
	
	print("\nProgram executed successfully")

#################################

import re

##### get file to run

filenames = [
	"examples/0_add",
	"examples/1_helloworld",
	"examples/2_exponentiation",
	"examples/3_choose",
	"examples/4_mazegame",
]

print("Input a number to choose which file to run:")
for i,val in enumerate(filenames):
	print(f"    {i}) {val}")
filename = filenames[int(input())]

##### parse file

raw = open(filename + ".piASM", "r").read().split("\n")
# remove comments + blank lines
parsed = [i.split("#")[0] for i in raw]
parsed = [i for i in parsed if i != ""]
# remove whitespace
parsed = re.sub("\s+", "", "".join(parsed))
# extract memory string
parsed = parsed.split("]")
memory_string = parsed[0][5:]
# separate instructions
program = re.findall(r"[a-zA-Z][-\d]*", parsed[1])
print("Loaded program:", parsed[1])
print(parsed[0]+"]")

##### run

print(f"Starting execution of {filename}")
run(program, memory_string)