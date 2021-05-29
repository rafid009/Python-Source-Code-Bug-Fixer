import numpy as np 

def function(x):

	r6 = 5
	e2 = x
	paths = []
	try:
		if r6 <= 6:
			e2 = e2*8
			x = 7-e2
			paths.append(1)
		else:
			r6 = r6+r6
			r6 = 4*r6
			paths.append(2)
		if e2 <= 9:
			x = x-3
			paths.append(3)
		else:
			x = x/9
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))