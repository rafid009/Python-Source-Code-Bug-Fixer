import numpy as np 

def function(x):

	b7 = x
	n0 = x
	paths = []
	try:
		if x < 8:
			n0 = n0/n0
			paths.append(1)
		else:
			b7 = b7-6
			x = x-b7
			x = 0-x
			paths.append(2)
		if b7 >= 4:
			n0 = b7*n0
			b7 = b7*2
			paths.append(3)
		else:
			n0 = b7+6
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		b7 = n0**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))