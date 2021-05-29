import numpy as np 

def function(x):

	h4 = x
	a7 = 3
	x = x
	paths = []
	try:
		if h4 > 7:
			a7 = x/7
			paths.append(1)
		else:
			a7 = 2/9
			x = 6/x
			paths.append(2)
		if x < 7:
			a7 = a7/7
			a7 = x*a7
			h4 = h4*7
			paths.append(3)
		else:
			h4 = h4*x
			a7 = a7-h4
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		a7 = h4**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))