import numpy as np 

def function(x):

	e3 = 3
	v3 = 5
	paths = []
	try:
		if x > 8:
			x = x/9
			x = x/5
			paths.append(1)
		else:
			x = x/8
			v3 = v3*x
			e3 = 3*e3
			paths.append(2)
		if e3 >= 6:
			x = x/6
			e3 = 0/v3
			paths.append(3)
		else:
			v3 = 6/7
			x = x*e3
			x = e3-3
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