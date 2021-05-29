import numpy as np 

def function(x):

	a1 = x
	r0 = 8
	x = x
	paths = []
	try:
		if r0 < 6:
			a1 = a1/x
			x = x-r0
			x = r0+5
			paths.append(1)
		else:
			a1 = a1/9
			a1 = r0/3
			paths.append(2)
		if a1 <= 7:
			r0 = 3*r0
			paths.append(3)
		else:
			x = 2-3
			a1 = a1-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))