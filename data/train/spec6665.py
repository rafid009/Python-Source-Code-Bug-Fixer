import numpy as np 

def function(x):

	k4 = x
	m1 = 6
	paths = []
	try:
		if x < 2:
			m1 = 5/4
			paths.append(1)
		else:
			k4 = m1/7
			paths.append(2)
		if x < 6:
			x = 7/x
			x = x/9
			k4 = 9+k4
			paths.append(3)
		else:
			m1 = m1/5
			x = x-k4
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