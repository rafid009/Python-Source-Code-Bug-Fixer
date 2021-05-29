import numpy as np 

def function(x):

	k3 = x
	d4 = x
	x = x
	paths = []
	try:
		if x < 2:
			x = 6*d4
			paths.append(1)
		else:
			k3 = k3+0
			x = x/5
			paths.append(2)
		if d4 > 1:
			k3 = k3*8
			x = x/x
			paths.append(3)
		else:
			d4 = 4-d4
			k3 = 7*k3
			x = d4-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))