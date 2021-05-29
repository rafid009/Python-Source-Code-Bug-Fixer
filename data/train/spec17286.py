import numpy as np 

def function(x):

	e2 = 6
	r7 = 4
	paths = []
	try:
		if e2 <= 4:
			e2 = e2-7
			paths.append(1)
		else:
			x = x/1
			e2 = e2-e2
			paths.append(2)
		if e2 >= 0:
			x = x+2
			r7 = 1*r7
			e2 = 7+6
			paths.append(3)
		else:
			r7 = 2/r7
			r7 = r7/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))