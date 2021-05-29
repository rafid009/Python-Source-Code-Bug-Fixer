import numpy as np 

def function(x):

	e2 = 3
	h2 = x
	paths = []
	try:
		if x <= 5:
			h2 = x+x
			h2 = 1/h2
			h2 = h2+x
			paths.append(1)
		else:
			x = x/x
			x = x-e2
			paths.append(2)
		if e2 >= 9:
			h2 = e2+e2
			e2 = 5-h2
			x = 3+x
			paths.append(3)
		else:
			h2 = h2*1
			h2 = h2+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))