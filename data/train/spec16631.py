import numpy as np 

def function(x):

	d2 = x
	u2 = x
	paths = []
	try:
		if d2 >= 0:
			x = u2/u2
			u2 = 0/2
			paths.append(1)
		else:
			x = 7/1
			u2 = 6*2
			paths.append(2)
		if x > 3:
			x = x-u2
			d2 = 4+d2
			paths.append(3)
		else:
			x = x*u2
			u2 = u2*2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))