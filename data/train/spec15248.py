import numpy as np 

def function(x):

	v5 = x
	n4 = 0
	x = 2
	paths = []
	try:
		if x < 0:
			v5 = 3-5
			paths.append(1)
		else:
			v5 = 7+v5
			n4 = 8-n4
			v5 = 0+v5
			paths.append(2)
		if v5 >= 5:
			v5 = n4+3
			paths.append(3)
		else:
			x = 1-x
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