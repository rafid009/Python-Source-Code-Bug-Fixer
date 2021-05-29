import numpy as np 

def function(x):

	m0 = 8
	x9 = 1
	paths = []
	try:
		if x9 > 2:
			x = 7*x
			x = 5+x
			x = x9+x
			paths.append(1)
		else:
			x9 = x9/x
			m0 = 9/m0
			paths.append(2)
		if x <= 9:
			x = m0*4
			paths.append(3)
		else:
			x = x-2
			x9 = x9/x9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))