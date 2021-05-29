import numpy as np 

def function(x):

	x7 = x
	m7 = x
	paths = []
	try:
		if x7 < 1:
			m7 = m7-m7
			m7 = 9*m7
			x7 = 6*x7
			paths.append(1)
		else:
			x = m7+x
			x = x/9
			paths.append(2)
		if m7 < 8:
			m7 = m7/9
			m7 = 0-3
			x = x-4
			paths.append(3)
		else:
			x = x*3
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