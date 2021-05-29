import numpy as np 

def function(x):

	b4 = x
	n0 = x
	paths = []
	try:
		if x >= 7:
			n0 = 1-n0
			paths.append(1)
		else:
			x = 0/4
			paths.append(2)
		if x > 5:
			n0 = n0/3
			b4 = b4/9
			paths.append(3)
		else:
			x = x+n0
			n0 = n0/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n0 = x**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))