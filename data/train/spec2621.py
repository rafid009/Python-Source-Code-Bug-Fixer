import numpy as np 

def function(x):

	r8 = 8
	e6 = x
	paths = []
	try:
		if x <= 8:
			r8 = x/9
			x = 5/6
			e6 = 6/9
			paths.append(1)
		else:
			x = 6+x
			x = 3*x
			paths.append(2)
		if r8 < 6:
			x = x-9
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))