import numpy as np 

def function(x):

	d7 = 8
	m0 = x
	paths = []
	try:
		if d7 > 7:
			m0 = 7+m0
			d7 = x/5
			x = m0/x
			paths.append(1)
		else:
			d7 = d7*1
			m0 = x/m0
			x = 7-m0
			paths.append(2)
		if x >= 8:
			x = d7/x
			m0 = 4+m0
			paths.append(3)
		else:
			x = 1-3
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		x = d7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))