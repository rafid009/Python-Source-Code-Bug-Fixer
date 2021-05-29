import numpy as np 

def function(x):

	k5 = x
	x0 = 9
	paths = []
	try:
		if x0 > 4:
			x = x*4
			k5 = k5/3
			k5 = k5-x
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if x < 4:
			x = 1-x
			k5 = x0*x0
			paths.append(3)
		else:
			x = x*0
			x0 = x0-x0
			x = x0*x
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