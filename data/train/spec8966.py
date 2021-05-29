import numpy as np 

def function(x):

	m6 = x
	x6 = 0
	paths = []
	try:
		if m6 >= 3:
			x6 = 4*4
			x6 = x6-x6
			paths.append(1)
		else:
			x6 = 7+x6
			x = 9+3
			paths.append(2)
		if m6 < 5:
			m6 = m6*6
			m6 = m6*x6
			x6 = 7-x6
			paths.append(3)
		else:
			m6 = m6/m6
			x = x6*x
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		x6 = m6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))