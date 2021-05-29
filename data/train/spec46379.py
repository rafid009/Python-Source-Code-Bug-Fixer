import numpy as np 

def function(x):

	h7 = x
	e6 = x
	paths = []
	try:
		if h7 >= 7:
			x = x-7
			e6 = e6*8
			paths.append(1)
		else:
			e6 = e6+4
			e6 = e6-4
			h7 = e6/e6
			paths.append(2)
		if h7 < 0:
			x = e6-0
			e6 = e6-8
			h7 = e6/1
			paths.append(3)
		else:
			x = x-4
			h7 = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))