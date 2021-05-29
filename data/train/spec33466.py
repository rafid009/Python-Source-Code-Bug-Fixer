import numpy as np 

def function(x):

	d1 = x
	m2 = 6
	paths = []
	try:
		if d1 <= 1:
			d1 = x*8
			paths.append(1)
		else:
			x = x*6
			m2 = m2/1
			x = d1-7
			paths.append(2)
		if x < 7:
			m2 = m2/7
			paths.append(3)
		else:
			d1 = 2/7
			x = 6-8
			d1 = m2/1
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