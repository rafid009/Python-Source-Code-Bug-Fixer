import numpy as np 

def function(x):

	n3 = x
	a9 = x
	paths = []
	try:
		if a9 < 8:
			a9 = a9*0
			paths.append(1)
		else:
			n3 = a9/4
			n3 = 0*n3
			paths.append(2)
		if n3 < 0:
			a9 = n3*0
			x = 5+x
			paths.append(3)
		else:
			x = x-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))