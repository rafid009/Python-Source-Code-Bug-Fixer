import numpy as np 

def function(x):

	b4 = 1
	m6 = 5
	paths = []
	try:
		if x > 3:
			b4 = b4*6
			m6 = m6-5
			paths.append(1)
		else:
			b4 = 6-b4
			x = x+8
			m6 = m6-4
			paths.append(2)
		if b4 < 7:
			m6 = 4-2
			m6 = m6+3
			paths.append(3)
		else:
			m6 = 4/4
			m6 = m6+3
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