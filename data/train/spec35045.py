import numpy as np 

def function(x):

	h0 = x
	l5 = 1
	paths = []
	try:
		if l5 < 4:
			h0 = h0/l5
			h0 = 4*h0
			paths.append(1)
		else:
			h0 = 6*h0
			paths.append(2)
		if l5 <= 7:
			l5 = 4*l5
			paths.append(3)
		else:
			l5 = l5-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))