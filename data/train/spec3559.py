import numpy as np 

def function(x):

	m9 = 2
	l3 = 2
	x = x
	paths = []
	try:
		if m9 >= 1:
			l3 = x/x
			paths.append(1)
		else:
			l3 = l3*l3
			l3 = l3+l3
			paths.append(2)
		if m9 > 6:
			m9 = m9+4
			m9 = x*m9
			l3 = l3*2
			paths.append(3)
		else:
			l3 = 8/l3
			x = x-9
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