import numpy as np 

def function(x):

	u5 = 1
	e3 = 0
	paths = []
	try:
		if u5 >= 2:
			x = x+x
			paths.append(1)
		else:
			e3 = 8+e3
			x = 3-6
			u5 = 3-3
			paths.append(2)
		if x >= 3:
			e3 = e3*u5
			u5 = u5*6
			paths.append(3)
		else:
			e3 = 4/e3
			u5 = u5+9
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