import numpy as np 

def function(x):

	l5 = 5
	h0 = 9
	paths = []
	try:
		if x <= 4:
			l5 = l5*x
			h0 = l5/h0
			paths.append(1)
		else:
			x = h0*x
			paths.append(2)
		if l5 <= 3:
			l5 = h0-x
			paths.append(3)
		else:
			l5 = l5*7
			h0 = l5-h0
			l5 = 5-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h0 = x**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))