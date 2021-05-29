import numpy as np 

def function(x):

	m8 = 1
	l0 = 3
	paths = []
	try:
		if x > 6:
			m8 = 7/7
			m8 = m8/8
			paths.append(1)
		else:
			l0 = 1-l0
			x = x-1
			m8 = m8/l0
			paths.append(2)
		if l0 <= 5:
			x = m8*3
			m8 = m8+m8
			l0 = 6+5
			paths.append(3)
		else:
			m8 = 3*x
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