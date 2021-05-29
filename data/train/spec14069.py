import numpy as np 

def function(x):

	d9 = 4
	f0 = x
	x = 3
	paths = []
	try:
		if f0 < 8:
			x = 4-8
			f0 = 4/x
			paths.append(1)
		else:
			f0 = f0*x
			x = x-5
			d9 = d9+3
			paths.append(2)
		if d9 > 4:
			x = 3*x
			f0 = d9/f0
			x = x*9
			paths.append(3)
		else:
			x = x/4
			f0 = f0-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))