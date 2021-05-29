import numpy as np 

def function(x):

	m6 = 6
	u5 = x
	paths = []
	try:
		if m6 < 8:
			u5 = u5/4
			u5 = 4+m6
			u5 = x*1
			paths.append(1)
		else:
			m6 = 5+m6
			paths.append(2)
		if x <= 6:
			u5 = 2*m6
			paths.append(3)
		else:
			x = x-u5
			u5 = 7/u5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m6 = x**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))