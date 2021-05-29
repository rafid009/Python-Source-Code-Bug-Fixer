import numpy as np 

def function(x):

	e0 = x
	n4 = 6
	paths = []
	try:
		if e0 >= 9:
			e0 = e0-3
			x = e0/x
			paths.append(1)
		else:
			x = x*n4
			n4 = n4+9
			paths.append(2)
		if x >= 7:
			n4 = n4-e0
			e0 = x/x
			e0 = 3-e0
			paths.append(3)
		else:
			e0 = e0+5
			e0 = e0+x
			x = 3/6
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		n4 = e0**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))