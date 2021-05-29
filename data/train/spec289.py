import numpy as np 

def function(x):

	m1 = x
	d0 = 8
	paths = []
	try:
		if m1 <= 0:
			m1 = m1-3
			x = 7+x
			x = 2/x
			paths.append(1)
		else:
			d0 = 7*d0
			paths.append(2)
		if x >= 6:
			m1 = x-m1
			paths.append(3)
		else:
			m1 = 8-m1
			d0 = d0/x
			d0 = x/4
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		x = d0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))