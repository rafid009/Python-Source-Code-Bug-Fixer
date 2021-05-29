import numpy as np 

def function(x):

	d0 = 1
	u1 = 5
	x = 3
	paths = []
	try:
		if d0 < 9:
			u1 = u1/4
			x = 8-9
			u1 = u1/7
			paths.append(1)
		else:
			d0 = x-d0
			paths.append(2)
		if x < 2:
			d0 = x*d0
			paths.append(3)
		else:
			u1 = 7*u1
			d0 = 2/5
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		x = d0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))