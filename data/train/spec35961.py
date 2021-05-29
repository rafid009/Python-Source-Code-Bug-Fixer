import numpy as np 

def function(x):

	m3 = 7
	d4 = x
	x = 1
	paths = []
	try:
		if m3 < 9:
			d4 = 9*d4
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if x >= 1:
			x = 5-7
			paths.append(3)
		else:
			m3 = 1/8
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