import numpy as np 

def function(x):

	y1 = 2
	m0 = x
	paths = []
	try:
		if m0 <= 0:
			x = 4/m0
			y1 = y1+y1
			m0 = y1*1
			paths.append(1)
		else:
			y1 = y1+9
			m0 = m0*x
			paths.append(2)
		if m0 < 0:
			m0 = 1*4
			paths.append(3)
		else:
			m0 = y1*6
			x = x/9
			y1 = y1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y1 = x**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))