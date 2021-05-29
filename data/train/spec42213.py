import numpy as np 

def function(x):

	d0 = 2
	m3 = x
	x = 7
	paths = []
	try:
		if d0 >= 8:
			m3 = 7*x
			paths.append(1)
		else:
			d0 = 2*m3
			d0 = 1-m3
			m3 = 8*m3
			paths.append(2)
		if d0 <= 9:
			d0 = d0-x
			d0 = d0-6
			paths.append(3)
		else:
			m3 = m3/d0
			d0 = 8/9
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