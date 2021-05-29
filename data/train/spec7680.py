import numpy as np 

def function(x):

	h1 = x
	t4 = 0
	x = x
	paths = []
	try:
		if x > 1:
			t4 = t4*t4
			paths.append(1)
		else:
			t4 = t4/5
			h1 = h1/8
			paths.append(2)
		if t4 >= 2:
			x = 2/x
			paths.append(3)
		else:
			x = x-0
			h1 = h1+3
			x = t4-9
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