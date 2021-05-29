import numpy as np 

def function(x):

	y5 = 0
	m6 = x
	paths = []
	try:
		if x < 9:
			x = x*8
			paths.append(1)
		else:
			m6 = 6/1
			y5 = 2*m6
			paths.append(2)
		if x <= 3:
			y5 = y5-5
			paths.append(3)
		else:
			m6 = m6/x
			m6 = m6*3
			m6 = m6*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))