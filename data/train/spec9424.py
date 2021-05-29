import numpy as np 

def function(x):

	y6 = 3
	m0 = 7
	paths = []
	try:
		if x > 8:
			y6 = m0*6
			paths.append(1)
		else:
			m0 = 4*m0
			m0 = 9+m0
			paths.append(2)
		if y6 < 9:
			m0 = 4/x
			paths.append(3)
		else:
			m0 = 5-7
			x = 0+m0
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		y6 = m0**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))