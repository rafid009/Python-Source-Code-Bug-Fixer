import numpy as np 

def function(x):

	e3 = x
	j4 = 2
	paths = []
	try:
		if j4 >= 8:
			j4 = e3*j4
			paths.append(1)
		else:
			j4 = j4/2
			e3 = 2-e3
			j4 = 5/j4
			paths.append(2)
		if x > 3:
			j4 = x/x
			e3 = e3*e3
			paths.append(3)
		else:
			j4 = j4/j4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))