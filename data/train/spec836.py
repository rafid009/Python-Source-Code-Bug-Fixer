import numpy as np 

def function(x):

	n4 = 9
	b5 = 5
	paths = []
	try:
		if n4 >= 2:
			n4 = n4/5
			n4 = 9*8
			paths.append(1)
		else:
			n4 = 4*7
			paths.append(2)
		if n4 <= 9:
			n4 = n4*3
			b5 = 9*4
			x = x+b5
			paths.append(3)
		else:
			b5 = 8-3
			n4 = n4+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))