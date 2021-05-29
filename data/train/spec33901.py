import numpy as np 

def function(x):

	d0 = 2
	u6 = 8
	paths = []
	try:
		if x <= 4:
			u6 = u6*3
			x = x/u6
			paths.append(1)
		else:
			u6 = 9/u6
			u6 = x*u6
			paths.append(2)
		if u6 > 3:
			u6 = d0-u6
			paths.append(3)
		else:
			d0 = d0*d0
			x = x+1
			d0 = d0*7
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