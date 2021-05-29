import numpy as np 

def function(x):

	b5 = x
	m9 = x
	paths = []
	try:
		if m9 < 7:
			x = 5-9
			x = 2-x
			m9 = m9+6
			paths.append(1)
		else:
			x = x+x
			m9 = 5-1
			paths.append(2)
		if m9 > 5:
			m9 = 3+0
			x = 1-m9
			paths.append(3)
		else:
			x = x/x
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