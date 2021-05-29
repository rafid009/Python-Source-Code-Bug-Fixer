import numpy as np 

def function(x):

	m5 = 0
	m9 = 6
	paths = []
	try:
		if m9 <= 1:
			m9 = 7*m9
			x = 1+m5
			paths.append(1)
		else:
			m5 = m5-6
			x = x-4
			paths.append(2)
		if m5 > 2:
			m9 = 7/m9
			paths.append(3)
		else:
			m5 = m5+m5
			x = 7-x
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