import numpy as np 

def function(x):

	m6 = x
	a0 = 5
	paths = []
	try:
		if m6 > 3:
			a0 = 8-4
			paths.append(1)
		else:
			m6 = m6+3
			x = x*7
			m6 = x-5
			paths.append(2)
		if a0 < 8:
			m6 = m6+8
			a0 = a0-6
			paths.append(3)
		else:
			m6 = m6/6
			m6 = m6-x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		x = a0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))