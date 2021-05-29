import numpy as np 

def function(x):

	m0 = x
	d5 = x
	x = x
	paths = []
	try:
		if d5 < 4:
			d5 = d5*6
			paths.append(1)
		else:
			m0 = 1-m0
			d5 = 1+d5
			paths.append(2)
		if x <= 3:
			m0 = 6-x
			paths.append(3)
		else:
			x = 6-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d5 = x**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))