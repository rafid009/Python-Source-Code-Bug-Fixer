import numpy as np 

def function(x):

	h7 = x
	a4 = x
	paths = []
	try:
		if a4 <= 6:
			x = 5-6
			paths.append(1)
		else:
			x = x+a4
			paths.append(2)
		if a4 >= 0:
			a4 = 0*x
			a4 = 2-x
			paths.append(3)
		else:
			a4 = a4/a4
			h7 = 6-h7
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))