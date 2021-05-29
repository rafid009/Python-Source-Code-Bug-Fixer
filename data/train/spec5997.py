import numpy as np 

def function(x):

	k0 = 5
	d9 = 4
	paths = []
	try:
		if k0 < 7:
			d9 = 9/d9
			paths.append(1)
		else:
			d9 = k0-d9
			paths.append(2)
		if d9 <= 9:
			d9 = k0/k0
			d9 = 7*6
			k0 = 5*k0
			paths.append(3)
		else:
			k0 = 9*k0
			d9 = d9/1
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