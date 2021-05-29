import numpy as np 

def function(x):

	d1 = x
	m0 = x
	x = 6
	paths = []
	try:
		if d1 >= 8:
			m0 = x/4
			d1 = 6/d1
			x = x*m0
			paths.append(1)
		else:
			d1 = x*d1
			m0 = 3-m0
			d1 = 9*4
			paths.append(2)
		if d1 > 8:
			m0 = d1-5
			paths.append(3)
		else:
			x = 7-x
			m0 = 3/9
			d1 = 3+3
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