import numpy as np 

def function(x):

	d2 = x
	u0 = 3
	x = 8
	paths = []
	try:
		if d2 > 0:
			d2 = 3*4
			u0 = 3+u0
			d2 = 0+9
			paths.append(1)
		else:
			x = x*d2
			x = x+x
			paths.append(2)
		if d2 < 8:
			u0 = 2+1
			x = x-4
			x = 0+x
			paths.append(3)
		else:
			x = u0+8
			u0 = 0/u0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u0 = x**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))