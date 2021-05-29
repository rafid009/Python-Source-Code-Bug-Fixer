import numpy as np 

def function(x):

	a7 = 2
	h0 = x
	paths = []
	try:
		if x <= 4:
			a7 = h0*5
			paths.append(1)
		else:
			a7 = a7*7
			x = a7-x
			paths.append(2)
		if h0 < 8:
			h0 = h0*7
			x = x+x
			paths.append(3)
		else:
			x = h0+x
			x = 1*x
			x = x*6
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		a7 = h0**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))