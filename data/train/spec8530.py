import numpy as np 

def function(x):

	e3 = 2
	d1 = x
	paths = []
	try:
		if x <= 4:
			d1 = 0/d1
			x = x-8
			paths.append(1)
		else:
			d1 = d1/8
			paths.append(2)
		if x > 6:
			d1 = d1-6
			paths.append(3)
		else:
			e3 = 3/9
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))