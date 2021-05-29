import numpy as np 

def function(x):

	e8 = 5
	j8 = x
	paths = []
	try:
		if x <= 4:
			e8 = e8*j8
			j8 = 2+j8
			e8 = e8+6
			paths.append(1)
		else:
			j8 = j8/3
			paths.append(2)
		if e8 < 1:
			e8 = e8+0
			paths.append(3)
		else:
			j8 = x+e8
			x = x/x
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))