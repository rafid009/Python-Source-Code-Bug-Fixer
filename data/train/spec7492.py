import numpy as np 

def function(x):

	x9 = x
	r7 = 2
	paths = []
	try:
		if x < 3:
			x = x9*x
			x9 = r7*x9
			x = 7+x9
			paths.append(1)
		else:
			x9 = x9-1
			x = x+x
			r7 = x9*r7
			paths.append(2)
		if x9 > 5:
			r7 = x9+1
			paths.append(3)
		else:
			x9 = 4-x9
			x9 = 0-x9
			r7 = 9/2
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