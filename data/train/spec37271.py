import numpy as np 

def function(x):

	f2 = 7
	h3 = 7
	paths = []
	try:
		if h3 > 0:
			f2 = 3/8
			h3 = 0/h3
			h3 = h3*9
			paths.append(1)
		else:
			x = x+3
			h3 = 5/x
			h3 = h3+4
			paths.append(2)
		if h3 < 5:
			f2 = 6*f2
			x = 8+x
			paths.append(3)
		else:
			h3 = 5*h3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))