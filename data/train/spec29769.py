import numpy as np 

def function(x):

	m6 = 9
	u9 = x
	paths = []
	try:
		if m6 >= 7:
			u9 = u9/x
			paths.append(1)
		else:
			x = x/m6
			paths.append(2)
		if x < 9:
			u9 = u9*8
			paths.append(3)
		else:
			u9 = u9*7
			x = x-x
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