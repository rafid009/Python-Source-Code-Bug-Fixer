import numpy as np 

def function(x):

	m4 = 8
	l8 = 1
	x = x
	paths = []
	try:
		if m4 < 7:
			x = x+7
			l8 = 2+l8
			x = l8/x
			paths.append(1)
		else:
			x = 9/x
			m4 = m4+2
			paths.append(2)
		if l8 > 9:
			m4 = m4*9
			x = 2*x
			paths.append(3)
		else:
			m4 = m4+x
			x = x/m4
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