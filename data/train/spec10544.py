import numpy as np 

def function(x):

	r5 = 8
	a8 = 2
	paths = []
	try:
		if x < 1:
			r5 = a8/1
			a8 = r5-a8
			a8 = 1-x
			paths.append(1)
		else:
			a8 = 2-a8
			paths.append(2)
		if x <= 0:
			a8 = a8+x
			paths.append(3)
		else:
			x = x+4
			x = 3/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))