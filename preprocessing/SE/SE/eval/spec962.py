import numpy as np 

def function(x):

	r9 = 7
	h2 = x
	paths = []
	try:
		if r9 >= 7:
			r9 = 9/r9
			r9 = r9-h2
			r9 = 6+9
			paths.append(1)
		else:
			h2 = h2*8
			x = 9/6
			r9 = r9-3
			paths.append(2)
		if x > 2:
			r9 = 9+r9
			x = x-9
			x = x+7
			paths.append(3)
		else:
			x = x*2
			h2 = r9+h2
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