import numpy as np 

def function(x):

	b9 = x
	x2 = 3
	paths = []
	try:
		if b9 >= 6:
			x2 = x2+4
			x = 5+9
			paths.append(1)
		else:
			x = x/x
			x2 = 4*x2
			x = 8-3
			paths.append(2)
		if b9 >= 3:
			x = x+8
			paths.append(3)
		else:
			x2 = 3*2
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))