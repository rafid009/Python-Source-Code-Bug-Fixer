import numpy as np 

def function(x):

	m5 = 9
	y6 = 3
	paths = []
	try:
		if y6 > 0:
			m5 = y6-m5
			paths.append(1)
		else:
			m5 = m5/x
			y6 = m5/y6
			x = x-5
			paths.append(2)
		if m5 <= 3:
			y6 = x-y6
			paths.append(3)
		else:
			y6 = 2+m5
			m5 = 9-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))