import numpy as np 

def function(x):

	j8 = x
	e3 = x
	paths = []
	try:
		if e3 >= 1:
			e3 = 3/e3
			x = e3+x
			e3 = j8/3
			paths.append(1)
		else:
			x = 1-x
			x = x-8
			paths.append(2)
		if x > 1:
			j8 = j8+2
			j8 = j8-8
			j8 = e3*j8
			paths.append(3)
		else:
			e3 = e3*2
			j8 = j8/j8
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