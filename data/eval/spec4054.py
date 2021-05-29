import numpy as np 

def function(x):

	m2 = 0
	y1 = 1
	paths = []
	try:
		if x <= 1:
			y1 = 0*4
			m2 = y1+y1
			m2 = m2-m2
			paths.append(1)
		else:
			y1 = m2+7
			paths.append(2)
		if x <= 3:
			m2 = 9-8
			paths.append(3)
		else:
			y1 = y1/4
			y1 = m2*x
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