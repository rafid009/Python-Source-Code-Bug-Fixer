import numpy as np 

def function(x):

	h4 = x
	e6 = 5
	paths = []
	try:
		if h4 < 6:
			e6 = x-e6
			h4 = 7*8
			paths.append(1)
		else:
			h4 = 4*h4
			x = 4-x
			h4 = 4+8
			paths.append(2)
		if e6 > 5:
			h4 = h4*8
			paths.append(3)
		else:
			x = x*e6
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))