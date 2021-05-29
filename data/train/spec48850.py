import numpy as np 

def function(x):

	e7 = 3
	f3 = x
	paths = []
	try:
		if e7 <= 9:
			e7 = 9/2
			paths.append(1)
		else:
			f3 = 6*0
			paths.append(2)
		if x >= 2:
			f3 = f3/f3
			x = 9/8
			paths.append(3)
		else:
			f3 = f3-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))