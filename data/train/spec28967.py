import numpy as np 

def function(x):

	e6 = 0
	h0 = x
	paths = []
	try:
		if e6 < 9:
			e6 = e6-2
			e6 = e6/e6
			paths.append(1)
		else:
			x = 0-e6
			paths.append(2)
		if x >= 3:
			e6 = 0/e6
			paths.append(3)
		else:
			x = 6+5
			e6 = h0-e6
			e6 = e6/e6
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		x = h0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))