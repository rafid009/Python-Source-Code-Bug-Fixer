import numpy as np 

def function(x):

	j0 = 4
	e6 = x
	paths = []
	try:
		if j0 <= 0:
			x = 6/x
			x = 1-j0
			x = x/3
			paths.append(1)
		else:
			e6 = e6+4
			e6 = e6+j0
			paths.append(2)
		if x <= 7:
			x = 3/2
			x = x+j0
			x = x/3
			paths.append(3)
		else:
			e6 = e6-e6
			e6 = 6/2
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