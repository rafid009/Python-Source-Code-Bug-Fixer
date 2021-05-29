import numpy as np 

def function(x):

	d1 = x
	f9 = 1
	x = 1
	paths = []
	try:
		if f9 >= 4:
			f9 = x-9
			paths.append(1)
		else:
			x = f9-d1
			d1 = 7*d1
			d1 = d1+0
			paths.append(2)
		if d1 >= 7:
			f9 = f9*d1
			x = x/5
			paths.append(3)
		else:
			d1 = x-d1
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