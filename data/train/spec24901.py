import numpy as np 

def function(x):

	l0 = 5
	m3 = x
	paths = []
	try:
		if m3 < 3:
			l0 = 8*9
			l0 = l0-x
			paths.append(1)
		else:
			m3 = m3*x
			paths.append(2)
		if l0 <= 9:
			l0 = 7/4
			paths.append(3)
		else:
			x = x/3
			m3 = m3/3
			x = x*l0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))