import numpy as np 

def function(x):

	m5 = 0
	f6 = 6
	paths = []
	try:
		if f6 < 1:
			x = x*4
			m5 = 2/f6
			f6 = x-6
			paths.append(1)
		else:
			m5 = m5+3
			paths.append(2)
		if m5 >= 1:
			f6 = 6*5
			m5 = 7/x
			paths.append(3)
		else:
			x = x-0
			m5 = 0-x
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