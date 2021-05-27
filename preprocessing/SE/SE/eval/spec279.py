import numpy as np 

def function(x):

	b3 = x
	b4 = x
	paths = []
	try:
		if x >= 8:
			b3 = 8-b3
			paths.append(1)
		else:
			x = b4*7
			b3 = b3+1
			b3 = b3+3
			paths.append(2)
		if b4 >= 0:
			b3 = b3*8
			paths.append(3)
		else:
			x = 4/b4
			b4 = 4*b4
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b3 = b4**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))