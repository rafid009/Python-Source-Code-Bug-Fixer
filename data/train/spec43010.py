import numpy as np 

def function(x):

	m0 = 8
	d7 = x
	paths = []
	try:
		if d7 <= 3:
			d7 = 8+7
			d7 = d7/x
			paths.append(1)
		else:
			d7 = d7*m0
			d7 = 5-d7
			paths.append(2)
		if d7 >= 9:
			m0 = 2+7
			paths.append(3)
		else:
			m0 = 4-x
			d7 = 8/m0
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m0 = x**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))