import numpy as np 

def function(x):

	m0 = x
	k5 = x
	paths = []
	try:
		if x <= 0:
			k5 = 8*k5
			x = k5-9
			paths.append(1)
		else:
			x = 6*x
			m0 = 8+m0
			k5 = k5+8
			paths.append(2)
		if k5 <= 1:
			x = 5+x
			paths.append(3)
		else:
			m0 = k5/m0
			m0 = 9*m0
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