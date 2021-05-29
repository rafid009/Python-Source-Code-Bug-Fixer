import numpy as np 

def function(x):

	r7 = x
	a9 = 2
	paths = []
	try:
		if r7 <= 4:
			a9 = a9/r7
			x = x-3
			a9 = a9*x
			paths.append(1)
		else:
			a9 = r7/9
			paths.append(2)
		if a9 <= 8:
			r7 = 8*r7
			r7 = r7+x
			paths.append(3)
		else:
			x = 1*x
			x = x+r7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))