import numpy as np 

def function(x):

	u6 = x
	m6 = x
	paths = []
	try:
		if m6 < 3:
			m6 = m6+4
			paths.append(1)
		else:
			x = x/5
			u6 = 6*9
			paths.append(2)
		if m6 > 9:
			x = u6/m6
			m6 = m6+8
			paths.append(3)
		else:
			m6 = 8+m6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))