import numpy as np 

def function(x):

	x5 = 2
	v3 = 2
	paths = []
	try:
		if x5 > 6:
			x5 = x5*5
			v3 = v3/5
			paths.append(1)
		else:
			v3 = 3/v3
			v3 = 2*2
			paths.append(2)
		if x > 3:
			x = 0*x
			x5 = 2-7
			x5 = x5/8
			paths.append(3)
		else:
			x = x*6
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))