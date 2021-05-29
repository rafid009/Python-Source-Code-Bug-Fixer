import numpy as np 

def function(x):

	m4 = x
	x6 = 2
	paths = []
	try:
		if x < 3:
			x6 = x/x6
			m4 = 6*m4
			paths.append(1)
		else:
			x = 7-5
			paths.append(2)
		if x >= 0:
			x6 = m4+4
			m4 = 5-m4
			x6 = 9+x6
			paths.append(3)
		else:
			x = x+2
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))