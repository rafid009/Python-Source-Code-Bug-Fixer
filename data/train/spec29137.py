import numpy as np 

def function(x):

	e6 = 7
	j4 = 4
	paths = []
	try:
		if e6 < 9:
			x = x*7
			paths.append(1)
		else:
			x = 4*x
			x = 7/x
			x = 3-5
			paths.append(2)
		if e6 < 2:
			e6 = 8*e6
			e6 = e6/4
			j4 = 4/j4
			paths.append(3)
		else:
			j4 = j4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))