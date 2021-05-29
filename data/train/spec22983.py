import numpy as np 

def function(x):

	m0 = 2
	x5 = x
	paths = []
	try:
		if m0 <= 4:
			x = 3+m0
			x5 = x5*2
			m0 = 3*m0
			paths.append(1)
		else:
			x = x-3
			x5 = 0/x5
			x5 = 1*x5
			paths.append(2)
		if x5 < 4:
			x5 = x5-m0
			paths.append(3)
		else:
			m0 = 8*3
			m0 = x5+3
			x5 = x5+3
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))