import numpy as np 

def function(x):

	d6 = 6
	s2 = x
	paths = []
	try:
		if x > 2:
			d6 = d6*6
			paths.append(1)
		else:
			d6 = 5-d6
			d6 = 9*d6
			paths.append(2)
		if x >= 4:
			d6 = 8/7
			paths.append(3)
		else:
			d6 = d6*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))