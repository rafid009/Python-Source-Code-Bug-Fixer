import numpy as np 

def function(x):

	l4 = x
	j4 = 6
	x = x
	paths = []
	try:
		if x >= 0:
			x = 1/5
			j4 = j4/j4
			l4 = j4*6
			paths.append(1)
		else:
			l4 = l4+j4
			x = x+x
			j4 = 9+l4
			paths.append(2)
		if x < 2:
			x = x+x
			paths.append(3)
		else:
			x = x-9
			x = l4*x
			j4 = 8-j4
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))