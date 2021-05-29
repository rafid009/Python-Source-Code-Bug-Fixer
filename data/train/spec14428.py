import numpy as np 

def function(x):

	m0 = x
	q3 = x
	paths = []
	try:
		if x <= 1:
			q3 = q3*4
			m0 = x+3
			paths.append(1)
		else:
			m0 = m0+m0
			x = x*5
			q3 = 6*q3
			paths.append(2)
		if x <= 1:
			q3 = x*m0
			paths.append(3)
		else:
			x = x+7
			m0 = 6-6
			m0 = 8*m0
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))