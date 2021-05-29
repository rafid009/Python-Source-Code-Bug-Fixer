import numpy as np 

def function(x):

	d9 = 8
	m8 = x
	x = 9
	paths = []
	try:
		if x > 1:
			x = d9*1
			x = x-8
			x = m8/1
			paths.append(1)
		else:
			d9 = d9-8
			m8 = m8-m8
			x = m8*x
			paths.append(2)
		if x > 0:
			d9 = d9-d9
			paths.append(3)
		else:
			m8 = 0/m8
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