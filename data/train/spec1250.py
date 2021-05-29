import numpy as np 

def function(x):

	e8 = 7
	n7 = 4
	paths = []
	try:
		if e8 > 2:
			n7 = n7/e8
			n7 = 9-2
			x = 5/x
			paths.append(1)
		else:
			n7 = 7+x
			e8 = 8-5
			e8 = 7*6
			paths.append(2)
		if n7 < 9:
			x = x/7
			n7 = 4*n7
			paths.append(3)
		else:
			x = 0*x
			e8 = e8/1
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