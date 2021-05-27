import numpy as np 

def function(x):

	v4 = 4
	m8 = x
	paths = []
	try:
		if v4 < 3:
			x = 8-8
			v4 = 4+8
			v4 = x+m8
			paths.append(1)
		else:
			v4 = 6+3
			x = 2-m8
			paths.append(2)
		if m8 <= 0:
			x = 5-x
			paths.append(3)
		else:
			m8 = m8*8
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