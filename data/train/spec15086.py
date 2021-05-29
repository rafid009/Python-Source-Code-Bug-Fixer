import numpy as np 

def function(x):

	h4 = x
	e1 = 3
	paths = []
	try:
		if e1 > 9:
			x = x-7
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if x > 0:
			x = e1-x
			paths.append(3)
		else:
			x = 7/4
			e1 = e1/8
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		h4 = h4**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))