import numpy as np 

def function(x):

	n2 = x
	e9 = 9
	paths = []
	try:
		if e9 > 6:
			n2 = n2/8
			x = 6+e9
			paths.append(1)
		else:
			e9 = 8/e9
			n2 = 7*x
			n2 = n2*6
			paths.append(2)
		if n2 < 9:
			x = 3*x
			paths.append(3)
		else:
			x = 9/x
			x = x+e9
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		n2 = n2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))