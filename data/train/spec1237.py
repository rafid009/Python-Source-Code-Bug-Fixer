import numpy as np 

def function(x):

	n4 = 7
	e2 = x
	paths = []
	try:
		if e2 >= 9:
			n4 = 4*n4
			x = 3*n4
			paths.append(1)
		else:
			x = x-8
			x = n4+x
			x = e2+e2
			paths.append(2)
		if e2 > 3:
			x = 9/x
			paths.append(3)
		else:
			x = x-9
			n4 = n4/x
			x = e2-5
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