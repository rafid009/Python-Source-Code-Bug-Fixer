import numpy as np 

def function(x):

	e2 = 0
	n5 = 1
	paths = []
	try:
		if e2 > 3:
			x = 9*x
			paths.append(1)
		else:
			n5 = n5+x
			e2 = 8*e2
			paths.append(2)
		if x < 1:
			n5 = 3+0
			x = 5/x
			n5 = x*n5
			paths.append(3)
		else:
			e2 = e2+1
			n5 = n5+n5
			n5 = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))