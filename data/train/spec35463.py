import numpy as np 

def function(x):

	b8 = x
	x4 = 2
	paths = []
	try:
		if b8 > 2:
			x4 = x4+2
			x4 = 4/2
			b8 = x4-x
			paths.append(1)
		else:
			x = 7-b8
			paths.append(2)
		if x4 <= 1:
			x4 = x4*x4
			x4 = x4/x
			paths.append(3)
		else:
			x = x-5
			b8 = x+b8
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x4 = b8**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))