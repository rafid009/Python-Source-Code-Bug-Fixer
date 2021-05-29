import numpy as np 

def function(x):

	n7 = 2
	v5 = x
	paths = []
	try:
		if v5 < 9:
			x = 3+x
			v5 = v5-3
			paths.append(1)
		else:
			n7 = 0*n7
			paths.append(2)
		if v5 < 0:
			v5 = v5/n7
			paths.append(3)
		else:
			x = x+2
			n7 = n7-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))