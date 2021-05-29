import numpy as np 

def function(x):

	d6 = x
	a0 = x
	paths = []
	try:
		if x <= 6:
			x = d6+x
			paths.append(1)
		else:
			x = 1*x
			paths.append(2)
		if d6 >= 2:
			a0 = a0*a0
			d6 = 9-d6
			d6 = d6+a0
			paths.append(3)
		else:
			d6 = a0+d6
			d6 = 4+d6
			d6 = 0-d6
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