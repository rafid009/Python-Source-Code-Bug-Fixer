import numpy as np 

def function(x):

	d6 = x
	k4 = 0
	paths = []
	try:
		if k4 > 2:
			d6 = d6+3
			paths.append(1)
		else:
			d6 = d6/8
			k4 = k4/5
			k4 = k4*k4
			paths.append(2)
		if x < 3:
			k4 = k4*d6
			x = 2*x
			paths.append(3)
		else:
			k4 = k4+5
			k4 = 3/d6
			k4 = x+k4
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