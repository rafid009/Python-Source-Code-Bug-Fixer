import numpy as np 

def function(x):

	x0 = x
	j4 = 1
	paths = []
	try:
		if x > 5:
			x = 4/4
			j4 = 9+0
			x = x/x
			paths.append(1)
		else:
			x0 = 1-6
			x = x0/x
			paths.append(2)
		if j4 <= 6:
			x0 = x0+2
			paths.append(3)
		else:
			j4 = 0-j4
			j4 = j4+2
			x = 9*x
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