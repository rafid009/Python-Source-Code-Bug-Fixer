import numpy as np 

def function(x):

	j6 = 8
	e3 = 6
	paths = []
	try:
		if e3 >= 0:
			e3 = e3-8
			j6 = j6+j6
			paths.append(1)
		else:
			x = x+6
			paths.append(2)
		if e3 <= 8:
			e3 = e3/x
			e3 = e3-j6
			paths.append(3)
		else:
			j6 = j6+e3
			e3 = 1/e3
			j6 = 1/3
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