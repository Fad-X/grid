def head():

	print("+", end=" ")	print("-", end=" ")

	print("-", end=" ")

	print("-", end=" ")

	

def body():

	print("|", end=" ")

	print(" ", end=" ")

	print(" ", end=" ")

	print(" ", end=" ")

def end_head():

	print("+")

	

def end_body():

	print("|")

def do1(x):

	x()

	

def do2(x):

	do1(x)

	do1(x)

def do3(x):

	do2(x)

	do1(x)

def do4(x):

	do2(x)

	do2(x)

	

def do6(x):

	do3(x)

	do3(x)	

	

def do7(x):

	do6(x)

	do1(x)

	

def length():

	do7(body)

	end_body()

	do7(body)

	end_body()

	do7(head)

	end_head()

	

def draw_top():

	do6(head)

	do1(head)

	end_head()

	

def do12(x):

	do6(x)

	do6(x)

	

def do24(x):

	do12(x)

	do12(x)

	

def draw_body():

	do12(length)

	do4(length)

	

	

def draw():

	draw_top()

	draw_body()

	

draw()

	

	

	

	

	

	
