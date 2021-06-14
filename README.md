# piASM : Custom assembly-like language
Why? Because boredom.

## Description
piASM works with a stack and a memory buffer (refered to as MEM), which are both arraylists that instructions can modify. Both contain only integers - strings/chars are converted to their ascii codes, and decimals are not supported.

Instructions can pop from / push to the top of the stack, and can read from / write to MEM.

The first line of a piASM file specifies the initial memory buffer contents as a list of comma-separated values.
All other lines contain instructions, which are run sequentially from left to right. Instructions are single characters, and integer arguments are given by appending `<argument>` after the instruction letter (see the Instructions section and examples for more details). Once the end of the instruction list is reached, the program terminates.

Whitespace is not part of syntax and a hashtag anywhere in a line marks the whole line as a comment.

# piASM Instructions

format:
```
<instruction + usage>
<mnemonic>
<description>
```

## General

```
P <pointer>
pointer
specify a unique reference number ("pointer") to this point in execution
```

```
j <pointer>
jump
pop two values (a then b) from stack. If a is 1, jump to pointer b and continue execution
```

```
J <pointer>
jump
pop two values (a then b) from stack. If b is 1, jump to pointer a and continue execution
```

```
p <integer>
push
push integer to stack
```

```
g
get
pop a value from stack, push MEM[value] to stack
```

```
s
set
pop two values (a then b) from stack, set MEM[a] to b
```

## I/O

```
i
input
push stdin to stack as an int
```

```
o
output
pop a value from stack, send to stdout as an int
```

```
I
string input
for each char in stdin: convert to ascii code, then push to stack. Finally, push the length of the input to stack
```

```
O
string output
pop a value from stack, convert from ascii code, send to stdout as a character
```



## Logic

```
E
equals zero
pop a value from stack, push (value==0) to stack as a 1 or 0
```

```
L
less than
pop two values (a then b) from stack, push (a<b) to stack as a 1 or 0
```

```
A
and
pop two values from stack, perform bitwise and, push result to stack
```

```
X
xor
pop two values from stack, perform bitwise xor, push result to stack
```



## Maths

```
a
add
pop two values from stack, add them, push result to stack
```

```
s
subtract
pop two values (a then b) from stack, push (a-b) to stack
```

```
m
multiply
pop two values (a then b) from stack, push (a*b) to stack
```

```
d
divide
pop two values (a then b) from stack, push (a//b) to stack ( // = integer division)
```

# Tips

A == B : `(A XOR B) == 0`  
A != B : `( (A XOR B) == 0) XOR 1`  
A OR B : `( (A XOR 1) AND (B XOR 1) ) XOR 1`