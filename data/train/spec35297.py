import numpy as np 

def function(x):

	m9 = x
	d4 = x
	paths = []
	try:
		if d4 <= 2:
			d4 = d4-0
			paths.append(1)
		else:
			d4 = d4/1
			x = m9/x
			x = x*x
			paths.append(2)
		if x >= 6:
			d4 = d4/2
			x = x-d4
			m9 = m9/1
			paths.append(3)
		else:
			m9 = m9*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))