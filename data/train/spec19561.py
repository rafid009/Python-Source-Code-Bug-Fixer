import numpy as np 

def function(x):

	m6 = 7
	o3 = 4
	paths = []
	try:
		if o3 > 4:
			o3 = m6/2
			paths.append(1)
		else:
			o3 = m6-x
			x = x-6
			paths.append(2)
		if o3 > 8:
			x = x-x
			paths.append(3)
		else:
			o3 = o3/o3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m6 = x**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))