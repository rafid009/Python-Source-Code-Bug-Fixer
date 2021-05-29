import numpy as np 

def function(x):

	f8 = x
	d0 = 9
	paths = []
	try:
		if f8 >= 5:
			d0 = d0*d0
			x = x+0
			paths.append(1)
		else:
			x = x*x
			x = x+f8
			paths.append(2)
		if x >= 1:
			f8 = f8-7
			d0 = d0/2
			paths.append(3)
		else:
			d0 = x/d0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))