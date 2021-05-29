import numpy as np 

def function(x):

	e7 = x
	j5 = x
	paths = []
	try:
		if x >= 3:
			e7 = 1/e7
			e7 = 2+e7
			paths.append(1)
		else:
			j5 = j5*x
			j5 = x/6
			e7 = e7+6
			paths.append(2)
		if j5 > 4:
			j5 = j5+8
			j5 = j5*5
			e7 = e7/e7
			paths.append(3)
		else:
			j5 = j5-6
			e7 = 8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))