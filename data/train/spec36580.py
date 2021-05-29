import numpy as np 

def function(x):

	j4 = 7
	d7 = x
	x = x
	paths = []
	try:
		if x > 2:
			d7 = 3+5
			j4 = d7+7
			paths.append(1)
		else:
			d7 = 3*x
			j4 = 6/j4
			x = d7/1
			paths.append(2)
		if d7 < 1:
			j4 = 8-j4
			x = 5/x
			d7 = d7-8
			paths.append(3)
		else:
			d7 = d7*3
			j4 = d7/d7
			x = x/j4
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