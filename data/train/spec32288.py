import numpy as np 

def function(x):

	b2 = x
	v7 = 1
	x = x
	paths = []
	try:
		if x <= 7:
			v7 = v7*v7
			paths.append(1)
		else:
			x = 7/x
			paths.append(2)
		if b2 > 2:
			v7 = v7-0
			paths.append(3)
		else:
			v7 = 5/v7
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))