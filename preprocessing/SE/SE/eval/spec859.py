import numpy as np 

def function(x):

	l0 = x
	m8 = x
	paths = []
	try:
		if x <= 8:
			l0 = l0+2
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if x > 1:
			x = x+5
			m8 = 6-l0
			m8 = m8+4
			paths.append(3)
		else:
			m8 = m8+6
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		l0 = m8**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))