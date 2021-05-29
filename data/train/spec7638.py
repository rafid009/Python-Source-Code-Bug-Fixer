import numpy as np 

def function(x):

	d0 = x
	m1 = x
	x = x
	paths = []
	try:
		if x < 1:
			d0 = 1/d0
			d0 = m1*3
			paths.append(1)
		else:
			x = 4*x
			d0 = d0+2
			x = x*x
			paths.append(2)
		if m1 < 8:
			m1 = m1-x
			x = x-2
			paths.append(3)
		else:
			x = d0/x
			x = x-m1
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))