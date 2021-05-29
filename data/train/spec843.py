import numpy as np 

def function(x):

	f5 = x
	e0 = x
	paths = []
	try:
		if x < 8:
			e0 = e0*9
			f5 = f5+f5
			f5 = f5+1
			paths.append(1)
		else:
			e0 = e0-4
			x = x*3
			paths.append(2)
		if x <= 6:
			f5 = f5+e0
			f5 = f5*f5
			paths.append(3)
		else:
			f5 = 6-0
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