import numpy as np 

def function(x):

	d0 = x
	m0 = 8
	paths = []
	try:
		if x < 1:
			m0 = 1-m0
			x = x/m0
			m0 = m0+4
			paths.append(1)
		else:
			d0 = 6-d0
			m0 = 8/d0
			x = x+m0
			paths.append(2)
		if x <= 2:
			m0 = 4/m0
			d0 = x-d0
			paths.append(3)
		else:
			d0 = d0/2
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		d0 = m0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))