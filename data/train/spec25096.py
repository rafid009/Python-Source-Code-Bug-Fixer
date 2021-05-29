import numpy as np 

def function(x):

	k3 = 6
	d7 = 9
	paths = []
	try:
		if d7 > 9:
			d7 = d7+1
			paths.append(1)
		else:
			k3 = 4/7
			x = x-4
			k3 = 7/x
			paths.append(2)
		if d7 >= 1:
			x = x-2
			k3 = 4*k3
			k3 = k3/3
			paths.append(3)
		else:
			x = d7*3
			d7 = x+3
			d7 = d7/4
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