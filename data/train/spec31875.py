import numpy as np 

def function(x):

	m8 = x
	j6 = 8
	paths = []
	try:
		if m8 < 2:
			j6 = m8-m8
			j6 = 4*7
			paths.append(1)
		else:
			m8 = 1/m8
			m8 = j6/m8
			j6 = x*x
			paths.append(2)
		if x <= 5:
			x = 8-m8
			j6 = j6-3
			paths.append(3)
		else:
			j6 = j6-x
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