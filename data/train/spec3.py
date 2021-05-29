import numpy as np 

def function(x):

	d1 = x
	m2 = 5
	paths = []
	try:
		if m2 < 8:
			x = 1-x
			paths.append(1)
		else:
			x = x/m2
			paths.append(2)
		if x > 3:
			d1 = d1-0
			x = m2-0
			paths.append(3)
		else:
			x = d1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))