import numpy as np 

def function(x):

	j8 = 3
	e0 = x
	paths = []
	try:
		if x > 7:
			j8 = e0*j8
			x = 8/5
			j8 = e0-9
			paths.append(1)
		else:
			x = x-x
			e0 = e0/4
			x = e0*j8
			paths.append(2)
		if j8 < 8:
			e0 = e0/6
			paths.append(3)
		else:
			e0 = e0*6
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		e0 = j8**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))