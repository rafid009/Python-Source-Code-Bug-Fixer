import numpy as np 

def function(x):

	e0 = x
	f3 = 5
	x = x
	paths = []
	try:
		if f3 < 5:
			f3 = f3+5
			e0 = e0*e0
			f3 = 9-e0
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if f3 <= 8:
			e0 = e0+7
			f3 = f3/5
			e0 = 4*8
			paths.append(3)
		else:
			f3 = 9/8
			f3 = 4*f3
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