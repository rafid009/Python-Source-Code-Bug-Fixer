import numpy as np 

def function(x):

	m9 = 6
	d2 = 7
	x = 1
	paths = []
	try:
		if m9 < 4:
			x = x-4
			d2 = 9-0
			x = 8+8
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if d2 > 2:
			x = 7/x
			m9 = 0/m9
			d2 = d2*6
			paths.append(3)
		else:
			m9 = 0+m9
			m9 = d2*d2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))