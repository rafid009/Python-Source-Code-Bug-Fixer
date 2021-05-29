import numpy as np 

def function(x):

	q6 = x
	m9 = 4
	paths = []
	try:
		if m9 <= 3:
			x = 5-x
			paths.append(1)
		else:
			q6 = q6-9
			paths.append(2)
		if x < 6:
			m9 = m9+2
			paths.append(3)
		else:
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))