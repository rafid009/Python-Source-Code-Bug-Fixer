import numpy as np 

def function(x):

	h2 = x
	e4 = 2
	paths = []
	try:
		if x <= 4:
			e4 = e4*x
			h2 = 6/h2
			h2 = 2+6
			paths.append(1)
		else:
			e4 = 0+1
			paths.append(2)
		if e4 < 2:
			e4 = 0+7
			x = x*7
			paths.append(3)
		else:
			x = 4+x
			x = 5+3
			h2 = x/h2
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