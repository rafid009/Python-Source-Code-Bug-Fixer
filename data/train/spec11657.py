import numpy as np 

def function(x):

	d7 = x
	m9 = 7
	paths = []
	try:
		if x >= 8:
			x = m9-x
			paths.append(1)
		else:
			d7 = m9-7
			paths.append(2)
		if x >= 4:
			m9 = 6*d7
			x = x*5
			d7 = x+3
			paths.append(3)
		else:
			d7 = 0*d7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))