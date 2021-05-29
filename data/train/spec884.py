import numpy as np 

def function(x):

	h0 = x
	a2 = 7
	paths = []
	try:
		if x >= 0:
			x = h0-x
			a2 = 6+a2
			h0 = x+h0
			paths.append(1)
		else:
			h0 = 9+h0
			h0 = 6*9
			h0 = h0+2
			paths.append(2)
		if a2 >= 5:
			h0 = x*8
			a2 = 1-a2
			x = x*8
			paths.append(3)
		else:
			x = 5-x
			a2 = a2+x
			h0 = 3+h0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))