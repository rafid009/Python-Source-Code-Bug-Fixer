import numpy as np 

def function(x):

	a2 = x
	n4 = 6
	paths = []
	try:
		if a2 > 2:
			x = a2*x
			paths.append(1)
		else:
			n4 = 3-4
			n4 = 8+7
			n4 = n4*n4
			paths.append(2)
		if n4 <= 4:
			a2 = n4+a2
			x = x*5
			a2 = a2+a2
			paths.append(3)
		else:
			a2 = a2*4
			n4 = 3/2
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