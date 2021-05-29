import numpy as np 

def function(x):

	e3 = 2
	f9 = 6
	paths = []
	try:
		if e3 < 1:
			x = 5+2
			paths.append(1)
		else:
			x = 6+x
			x = x*3
			f9 = f9+1
			paths.append(2)
		if f9 > 3:
			f9 = f9+7
			x = x*e3
			f9 = f9*3
			paths.append(3)
		else:
			x = f9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))