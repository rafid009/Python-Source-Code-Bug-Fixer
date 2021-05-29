import numpy as np 

def function(x):

	k3 = 4
	d7 = 5
	paths = []
	try:
		if x < 7:
			d7 = d7+8
			paths.append(1)
		else:
			x = x*d7
			d7 = d7-3
			paths.append(2)
		if k3 > 5:
			d7 = d7+k3
			k3 = k3/d7
			k3 = k3-9
			paths.append(3)
		else:
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))