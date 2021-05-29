import numpy as np 

def function(x):

	b1 = x
	k4 = x
	paths = []
	try:
		if k4 > 8:
			k4 = k4-4
			paths.append(1)
		else:
			b1 = 9*b1
			paths.append(2)
		if x > 8:
			b1 = b1-1
			b1 = x-2
			paths.append(3)
		else:
			x = x+8
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		b1 = b1**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))