import numpy as np 

def function(x):

	a5 = x
	r7 = x
	paths = []
	try:
		if r7 < 4:
			r7 = a5-r7
			a5 = a5+r7
			paths.append(1)
		else:
			r7 = 9-r7
			paths.append(2)
		if a5 < 4:
			a5 = a5-2
			a5 = a5*a5
			x = x/6
			paths.append(3)
		else:
			r7 = 6-7
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