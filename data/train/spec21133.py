import numpy as np 

def function(x):

	i9 = 0
	m8 = 9
	paths = []
	try:
		if m8 < 8:
			m8 = x*9
			x = x/4
			m8 = m8/6
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if m8 < 0:
			i9 = 7-1
			x = 3/x
			paths.append(3)
		else:
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m8 = x**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))