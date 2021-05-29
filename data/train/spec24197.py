import numpy as np 

def function(x):

	d9 = 7
	u2 = 8
	paths = []
	try:
		if x <= 5:
			u2 = u2/2
			u2 = u2*u2
			u2 = 9/u2
			paths.append(1)
		else:
			d9 = d9-x
			x = d9-x
			paths.append(2)
		if x <= 8:
			d9 = d9-u2
			d9 = 3-d9
			d9 = 0+d9
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		x = d9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))