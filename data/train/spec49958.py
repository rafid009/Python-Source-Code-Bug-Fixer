import numpy as np 

def function(x):

	j6 = x
	m8 = x
	paths = []
	try:
		if x <= 3:
			x = 2*m8
			x = 2*m8
			paths.append(1)
		else:
			x = x/1
			m8 = x/6
			x = 6-4
			paths.append(2)
		if x <= 9:
			j6 = 8/j6
			m8 = m8+6
			paths.append(3)
		else:
			x = 2*x
			x = 0-j6
			x = x+6
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