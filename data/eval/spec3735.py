import numpy as np 

def function(x):

	h3 = x
	e0 = 5
	paths = []
	try:
		if x <= 9:
			h3 = h3*h3
			e0 = x/e0
			paths.append(1)
		else:
			h3 = 1/1
			e0 = 6-x
			paths.append(2)
		if x <= 6:
			h3 = h3*8
			h3 = 0/h3
			e0 = x*1
			paths.append(3)
		else:
			h3 = 4/7
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))