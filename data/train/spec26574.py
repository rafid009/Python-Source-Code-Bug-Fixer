import numpy as np 

def function(x):

	a1 = 9
	x3 = 1
	paths = []
	try:
		if x <= 3:
			x = x3+x
			x3 = 6-2
			x3 = 5*x
			paths.append(1)
		else:
			a1 = x/2
			a1 = a1+x3
			a1 = a1-2
			paths.append(2)
		if a1 <= 8:
			x3 = 8*x
			x = x3/x
			paths.append(3)
		else:
			x3 = x3/6
			a1 = 5+3
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x = x3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))