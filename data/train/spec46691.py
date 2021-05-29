import numpy as np 

def function(x):

	u5 = 7
	e0 = x
	paths = []
	try:
		if x < 4:
			e0 = e0*7
			e0 = 2*3
			x = 6/x
			paths.append(1)
		else:
			e0 = 2+8
			paths.append(2)
		if u5 > 2:
			x = u5/x
			paths.append(3)
		else:
			x = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))