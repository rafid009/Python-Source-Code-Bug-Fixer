import numpy as np 

def function(x):

	d9 = 5
	q3 = 1
	paths = []
	try:
		if d9 >= 0:
			x = d9/x
			x = x+2
			paths.append(1)
		else:
			d9 = d9*x
			q3 = q3+q3
			q3 = q3/1
			paths.append(2)
		if x >= 2:
			x = x+x
			q3 = d9+x
			paths.append(3)
		else:
			q3 = q3+3
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