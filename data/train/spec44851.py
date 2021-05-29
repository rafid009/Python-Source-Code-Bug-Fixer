import numpy as np 

def function(x):

	m0 = 3
	u6 = 5
	paths = []
	try:
		if u6 > 3:
			u6 = m0+4
			u6 = u6*5
			paths.append(1)
		else:
			m0 = 8-m0
			paths.append(2)
		if u6 < 5:
			m0 = 4/1
			u6 = 1/3
			x = x/u6
			paths.append(3)
		else:
			m0 = 9*4
			x = 1+x
			m0 = 2-m0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m0 = x**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))