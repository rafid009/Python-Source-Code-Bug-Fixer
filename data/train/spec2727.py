import numpy as np 

def function(x):

	x0 = x
	m5 = x
	paths = []
	try:
		if x >= 0:
			m5 = 2-m5
			x = x-6
			paths.append(1)
		else:
			m5 = x0-6
			paths.append(2)
		if x0 > 8:
			m5 = x*m5
			x = 9+x0
			paths.append(3)
		else:
			m5 = 6*m5
			m5 = 8*m5
			x0 = 8*x0
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x = m5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))