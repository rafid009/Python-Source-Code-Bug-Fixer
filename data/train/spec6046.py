import numpy as np 

def function(x):

	m9 = x
	y4 = 8
	paths = []
	try:
		if x >= 6:
			x = y4/y4
			paths.append(1)
		else:
			m9 = 5/7
			m9 = m9/m9
			m9 = m9/5
			paths.append(2)
		if y4 <= 2:
			y4 = m9*y4
			m9 = m9-1
			paths.append(3)
		else:
			m9 = 9+x
			y4 = y4+y4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))