import numpy as np 

def function(x):

	m2 = 8
	l8 = x
	paths = []
	try:
		if m2 <= 3:
			x = 9+3
			x = m2+1
			m2 = m2-2
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if x > 9:
			x = 9-x
			m2 = 9-m2
			x = 7-8
			paths.append(3)
		else:
			x = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))