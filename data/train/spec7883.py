import numpy as np 

def function(x):

	l4 = x
	m3 = 4
	paths = []
	try:
		if x <= 0:
			l4 = m3-7
			l4 = l4+2
			paths.append(1)
		else:
			x = x/7
			l4 = l4/2
			m3 = m3+m3
			paths.append(2)
		if x > 1:
			x = m3-x
			x = 9-m3
			l4 = m3-l4
			paths.append(3)
		else:
			l4 = 4*l4
			l4 = l4+5
			l4 = 4-l4
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