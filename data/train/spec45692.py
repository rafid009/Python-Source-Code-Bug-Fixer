import numpy as np 

def function(x):

	u4 = x
	m6 = x
	paths = []
	try:
		if x <= 1:
			u4 = x/1
			m6 = 3/m6
			paths.append(1)
		else:
			m6 = 5-m6
			x = x+3
			x = x*1
			paths.append(2)
		if x > 8:
			m6 = m6-4
			paths.append(3)
		else:
			u4 = 4/6
			m6 = 2/m6
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