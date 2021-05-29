import numpy as np 

def function(x):

	m0 = x
	x6 = x
	paths = []
	try:
		if x > 6:
			x = x+6
			x = x6*3
			paths.append(1)
		else:
			x = x*m0
			paths.append(2)
		if x6 < 0:
			m0 = 5*m0
			m0 = 1*x6
			x = x*5
			paths.append(3)
		else:
			x = 1/x
			m0 = m0/8
			x = x-0
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))