import numpy as np 

def function(x):

	d6 = x
	c3 = 8
	paths = []
	try:
		if c3 > 0:
			d6 = 0+4
			d6 = 5-6
			x = x+c3
			paths.append(1)
		else:
			x = d6*1
			paths.append(2)
		if c3 >= 8:
			d6 = 3-4
			d6 = d6-8
			paths.append(3)
		else:
			d6 = 4/8
			d6 = 0*d6
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		x = d6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))