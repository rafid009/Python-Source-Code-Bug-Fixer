import numpy as np 

def function(x):

	e2 = x
	n4 = 5
	paths = []
	try:
		if x > 5:
			e2 = n4+3
			paths.append(1)
		else:
			n4 = e2+n4
			n4 = n4-x
			paths.append(2)
		if x < 0:
			n4 = n4*n4
			x = 3*1
			x = e2*x
			paths.append(3)
		else:
			n4 = n4+n4
			e2 = 1/e2
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		n4 = e2**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))