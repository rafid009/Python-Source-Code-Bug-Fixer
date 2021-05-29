import numpy as np 

def function(x):

	b0 = 1
	n6 = x
	paths = []
	try:
		if n6 > 0:
			b0 = 0-x
			x = 2*3
			paths.append(1)
		else:
			n6 = 7/n6
			b0 = b0-b0
			x = x*8
			paths.append(2)
		if x >= 4:
			x = 2+x
			paths.append(3)
		else:
			b0 = 9*b0
			n6 = n6-2
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		n6 = b0**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))