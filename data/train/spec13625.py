import numpy as np 

def function(x):

	e3 = 5
	j4 = 5
	paths = []
	try:
		if x <= 8:
			e3 = 2+e3
			paths.append(1)
		else:
			j4 = 5-1
			paths.append(2)
		if e3 > 5:
			e3 = e3/4
			x = x+5
			paths.append(3)
		else:
			x = x+j4
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