import numpy as np 

def function(x):

	r8 = 7
	e2 = 1
	paths = []
	try:
		if x > 6:
			e2 = 9/8
			x = 3/e2
			paths.append(1)
		else:
			r8 = x+9
			x = 4+x
			paths.append(2)
		if e2 <= 1:
			r8 = 3-3
			e2 = 6/x
			r8 = r8-2
			paths.append(3)
		else:
			x = x*7
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