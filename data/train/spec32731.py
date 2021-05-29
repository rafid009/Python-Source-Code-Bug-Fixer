import numpy as np 

def function(x):

	c3 = x
	e0 = 2
	x = 2
	paths = []
	try:
		if e0 <= 3:
			e0 = e0/c3
			x = e0/c3
			paths.append(1)
		else:
			x = 4/x
			e0 = 6/e0
			x = e0-x
			paths.append(2)
		if x > 0:
			e0 = x/2
			paths.append(3)
		else:
			x = 3/c3
			e0 = 4-0
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		e0 = c3**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))