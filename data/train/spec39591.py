import numpy as np 

def function(x):

	t0 = x
	h2 = 6
	paths = []
	try:
		if t0 >= 0:
			t0 = t0*7
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if x >= 6:
			h2 = 0*5
			paths.append(3)
		else:
			h2 = h2/5
			t0 = 0+t0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))