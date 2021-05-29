import numpy as np 

def function(x):

	m1 = 4
	y6 = 6
	paths = []
	try:
		if x > 7:
			m1 = m1*y6
			paths.append(1)
		else:
			y6 = y6/x
			x = x-8
			paths.append(2)
		if m1 < 0:
			m1 = 7+6
			x = 2-x
			paths.append(3)
		else:
			m1 = y6+6
			y6 = y6*2
			x = 7+x
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