import numpy as np 

def function(x):

	k7 = x
	m0 = x
	paths = []
	try:
		if m0 <= 5:
			x = 1-x
			k7 = k7/4
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if x <= 6:
			m0 = m0/k7
			paths.append(3)
		else:
			k7 = 3-k7
			x = x/x
			x = x-x
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