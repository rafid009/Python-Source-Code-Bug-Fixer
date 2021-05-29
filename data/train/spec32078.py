import numpy as np 

def function(x):

	m3 = x
	m8 = 1
	paths = []
	try:
		if x >= 9:
			x = 1/x
			x = 1+x
			paths.append(1)
		else:
			x = x/3
			m3 = m3*m8
			paths.append(2)
		if m8 > 3:
			m8 = 7+9
			paths.append(3)
		else:
			m8 = m8-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))