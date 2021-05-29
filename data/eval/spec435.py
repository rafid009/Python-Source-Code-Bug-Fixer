import numpy as np 

def function(x):

	e6 = 1
	f9 = x
	paths = []
	try:
		if e6 <= 6:
			e6 = e6/x
			x = x+7
			f9 = x+f9
			paths.append(1)
		else:
			e6 = 1-e6
			e6 = e6+8
			e6 = e6-1
			paths.append(2)
		if e6 < 9:
			x = f9/4
			paths.append(3)
		else:
			e6 = e6-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))