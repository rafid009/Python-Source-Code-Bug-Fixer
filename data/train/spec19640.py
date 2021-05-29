import numpy as np 

def function(x):

	i9 = x
	e3 = 8
	paths = []
	try:
		if x <= 7:
			e3 = i9+9
			i9 = i9-5
			x = 4+x
			paths.append(1)
		else:
			e3 = e3*1
			paths.append(2)
		if i9 <= 9:
			e3 = e3-5
			e3 = e3/e3
			paths.append(3)
		else:
			x = 2*9
			x = i9/x
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