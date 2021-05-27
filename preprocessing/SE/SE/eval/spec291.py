import numpy as np 

def function(x):

	r1 = x
	a7 = 4
	paths = []
	try:
		if r1 <= 2:
			x = x/4
			r1 = 4/a7
			paths.append(1)
		else:
			x = a7/a7
			paths.append(2)
		if r1 >= 3:
			a7 = 8+a7
			r1 = 0-6
			a7 = a7+x
			paths.append(3)
		else:
			x = x+5
			a7 = a7+4
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