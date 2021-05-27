import numpy as np 

def function(x):

	m7 = 6
	h6 = 8
	x = x
	paths = []
	try:
		if m7 < 9:
			h6 = 5-x
			x = 7+x
			paths.append(1)
		else:
			x = x-x
			x = 2-x
			m7 = m7/1
			paths.append(2)
		if x >= 3:
			x = 2/4
			paths.append(3)
		else:
			m7 = m7*x
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