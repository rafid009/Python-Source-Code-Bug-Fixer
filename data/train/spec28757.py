import numpy as np 

def function(x):

	u0 = 5
	d9 = 0
	paths = []
	try:
		if d9 < 8:
			d9 = 0*0
			u0 = u0/4
			paths.append(1)
		else:
			d9 = 4*6
			x = 3-7
			x = x*2
			paths.append(2)
		if x > 6:
			x = 3*x
			x = 4*3
			paths.append(3)
		else:
			d9 = x*4
			d9 = d9-6
			d9 = u0-3
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