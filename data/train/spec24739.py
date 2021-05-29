import numpy as np 

def function(x):

	h3 = x
	e3 = 9
	paths = []
	try:
		if x <= 6:
			x = e3-6
			paths.append(1)
		else:
			h3 = h3/4
			h3 = h3*5
			paths.append(2)
		if e3 <= 0:
			h3 = 8*h3
			e3 = e3*8
			paths.append(3)
		else:
			h3 = h3+0
			e3 = 1-e3
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		h3 = h3**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))