import numpy as np 

def function(x):

	m6 = 9
	f2 = x
	paths = []
	try:
		if x < 4:
			x = 1+5
			x = 6*1
			paths.append(1)
		else:
			x = 6*7
			m6 = 8-m6
			x = f2/3
			paths.append(2)
		if x >= 3:
			m6 = m6*2
			x = 0-x
			paths.append(3)
		else:
			x = 4-x
			x = x*6
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