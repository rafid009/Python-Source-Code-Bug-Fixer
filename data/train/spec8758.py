import numpy as np 

def function(x):

	u7 = x
	m9 = x
	x = x
	paths = []
	try:
		if u7 < 4:
			x = m9+4
			x = 8/x
			paths.append(1)
		else:
			m9 = m9/u7
			m9 = u7/u7
			paths.append(2)
		if x <= 6:
			x = 7+x
			paths.append(3)
		else:
			m9 = 9+5
			u7 = 2+u7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))