import numpy as np 

def function(x):

	m9 = x
	n7 = 2
	paths = []
	try:
		if x < 6:
			m9 = m9*n7
			m9 = 4/m9
			m9 = x/6
			paths.append(1)
		else:
			m9 = m9/8
			paths.append(2)
		if m9 > 4:
			x = 1+x
			x = x/2
			paths.append(3)
		else:
			x = x-5
			n7 = m9+n7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m9 = x**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))