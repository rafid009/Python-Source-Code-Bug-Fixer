import numpy as np 

def function(x):

	m5 = 1
	u7 = 1
	paths = []
	try:
		if x < 1:
			u7 = u7-x
			m5 = m5/4
			paths.append(1)
		else:
			x = 9/x
			paths.append(2)
		if m5 > 1:
			m5 = 9+1
			paths.append(3)
		else:
			x = x-5
			x = u7-m5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m5 = x**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))