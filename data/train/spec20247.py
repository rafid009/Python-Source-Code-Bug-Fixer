import numpy as np 

def function(x):

	e9 = x
	n2 = x
	paths = []
	try:
		if n2 >= 4:
			e9 = 2/n2
			e9 = e9*2
			n2 = 3*e9
			paths.append(1)
		else:
			x = 4*x
			x = x-6
			paths.append(2)
		if e9 > 4:
			e9 = e9+n2
			e9 = e9-5
			n2 = 6/4
			paths.append(3)
		else:
			n2 = e9*6
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x = e9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))