import numpy as np 

def function(x):

	e3 = x
	v0 = x
	paths = []
	try:
		if v0 >= 9:
			e3 = 1-e3
			x = x-1
			paths.append(1)
		else:
			x = v0+x
			paths.append(2)
		if e3 <= 8:
			v0 = x/e3
			paths.append(3)
		else:
			v0 = v0/9
			e3 = 8+e3
			x = 8/x
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