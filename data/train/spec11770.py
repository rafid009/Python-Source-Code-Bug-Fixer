import numpy as np 

def function(x):

	e0 = 1
	o0 = 7
	paths = []
	try:
		if e0 >= 3:
			e0 = 9+9
			x = x+5
			e0 = e0-x
			paths.append(1)
		else:
			x = x*e0
			paths.append(2)
		if e0 <= 0:
			x = x+7
			x = x/7
			paths.append(3)
		else:
			x = 8*x
			e0 = o0-o0
			o0 = 4*o0
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