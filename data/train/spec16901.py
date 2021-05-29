import numpy as np 

def function(x):

	r2 = x
	e5 = x
	paths = []
	try:
		if x < 1:
			x = x+e5
			paths.append(1)
		else:
			r2 = r2/6
			x = x-2
			e5 = 6/4
			paths.append(2)
		if e5 <= 2:
			x = x*3
			r2 = 2*4
			r2 = r2+9
			paths.append(3)
		else:
			x = x+4
			e5 = e5/e5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))